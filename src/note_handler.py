#!/usr/bin/python3

from textwrap import indent
import gi

import os, sys

import json

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy
from collections import OrderedDict

import note
import close_dialog
import settings_dialog
import note_color

launch_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Update sys.path to include modules
if launch_dir == "/usr/bin":
    data_path = "/usr/share/com.github.erkielbrecht.sticky/sticky"
else:
    data_path = launch_dir + "/sticky"

save_path = os.path.expanduser('~') + "/.var/app/com.github.erkielbrecht.sticky/data/"

print("Note handler imported!")

class note_handler():
    note_list = OrderedDict()
    counter = 0

    def quit_app(self, *args):
        self.save_notes(None)
        Gtk.main_quit()

    def note_check(self):
        self.save_notes(None)
        if len(self.note_list) == 0:
            Gtk.main_quit()

    def make_new_note(self, widget):

        self.counter += 1

        new_note = note.new_note()

        new_note.add_button.connect("clicked", self.make_new_note)
        new_note.close_button.connect("clicked", self.close_note, self.counter)

        new_note.bold_button.connect("clicked", self.set_text_tag, new_note, new_note.tag_bold)
        new_note.underline_button.connect("clicked", self.set_text_tag, new_note, new_note.tag_underline)
        new_note.italic_button.connect("clicked", self.set_text_tag, new_note, new_note.tag_italic)

        new_note.settings_button.connect("clicked", self.open_settings)

        new_note.note_window.present()

        new_note.note_accelerators.connect(new_note.key, new_note.mod, 0, self.quit_app)

        new_note.note_window.connect("focus-in-event", self.handle_focus, True, new_note)
        new_note.note_window.connect("focus-out-event", self.handle_focus, False, new_note)

        note_color.set_note_color(None, new_note.color, new_note)

        new_note.banana_button.connect("clicked", note_color.set_note_color, "banana", new_note)
        new_note.strawberry_button.connect("clicked", note_color.set_note_color, "strawberry", new_note)
        new_note.lime_button.connect("clicked", note_color.set_note_color, "lime", new_note)
        new_note.blueberry_button.connect("clicked", note_color.set_note_color, "blueberry", new_note)

        self.note_list[self.counter] = new_note

    def handle_focus(self, widget, other, in_focus, _note):
        if in_focus:
            _note.bold_button.show()
            _note.underline_button.show()
            _note.italic_button.show()
            _note.settings_button.show()
        else:
            self.save_notes(None)
            _note.bold_button.hide()
            _note.underline_button.hide()
            _note.italic_button.hide()
            _note.settings_button.hide()


    def set_text_tag(self, widget, _note, tag):
        bounds = _note.text_buffer.get_selection_bounds()
        if len(bounds) != 0:
            start, end = bounds
            if start.has_tag(tag) and end.has_tag(tag) or end.ends_tag(tag):
                _note.text_buffer.remove_tag(tag, start, end)
            else:
                _note.text_buffer.apply_tag(tag, start, end)

    def save_notes(self, widget):
        note_save = {}
        for i in self.note_list:
            _note = self.note_list[i]

            note_info = {}

            note_info["color"] =(_note.color)

            note_info["size"] = (_note.note_window.get_size())

            note_info["position"] = (_note.note_window.get_position())

            note_buffer =  _note.note_text.get_buffer()

            start_iter = note_buffer.get_start_iter()
            end_iter = note_buffer.get_end_iter()

            format = note_buffer.register_serialize_tagset()
            save = note_buffer.serialize(note_buffer, format, start_iter, end_iter)
            note_info["content"] = save.decode("latin1")

            note_save[i] = note_info

        save_string = json.dumps(note_save, indent=4)
        save_file = open(save_path + "saved_notes.json","w")
        save_file.write(save_string)
        save_file.close()
        print("Saving Done!")
        

    def load_notes(self):
        save_file = open(save_path + "saved_notes.json","r")
        save_string = save_file.read()

        notes = json.loads(save_string)

        for i in notes:
            self.make_new_note(None)
            new_note = self.note_list[self.counter]
            new_note.color = notes[i]["color"]
            note_color.set_note_color(None, new_note.color, new_note)
            new_note.note_window.resize(notes[i]["size"][0], notes[i]["size"][1])
            new_note.note_window.move(notes[i]["position"][0], notes[i]["position"][1])

            note_buffer = new_note.note_text.get_buffer()

            start_iter = note_buffer.get_start_iter()

            format = note_buffer.register_deserialize_tagset()
            print(notes[i]["content"].encode("latin1"))
            note_buffer.deserialize(note_buffer, format, start_iter, notes[i]["content"].encode("latin1"))

        save_file.close()

    def open_settings(self, *args):
        _settings_dialog = settings_dialog.new_settings_dialog()

        _settings_dialog.settings_window.present()

    def close_note(self, widget, parent):

        c_note_window = self.note_list[parent].note_window

        note_buffer = self.note_list[parent].note_text.get_buffer()

        start_iter = note_buffer.get_start_iter()
        end_iter = note_buffer.get_end_iter()
 
        text = note_buffer.get_text(start_iter, end_iter, True) 

        def destroy_dialog(widget):
            _close_dialog.close_window.destroy()

        def destroy_note(widget):
            self.note_list[parent].note_window.destroy()
            self.note_list.pop(parent)
            self.note_check() 

        def destroy_dialog_note(widget):
            destroy_dialog(None)
            destroy_note(None)

        if text == "":
            destroy_note(None)
        else:
            _close_dialog = close_dialog.new_close_dialog()

            note_color.set_dialog_color(self.note_list[parent].color, _close_dialog)

            _close_dialog.close_window.set_transient_for(c_note_window)

            _close_dialog.close_window.present()
            
            _close_dialog.cancel_button.connect("clicked", destroy_dialog)

            _close_dialog.close_button.connect("clicked", destroy_dialog_note)


    def __init__(self):
        if os.path.exists(save_path + "saved_notes.json"):
            note_save_file = open(save_path + "saved_notes.json", "r")
            content =  note_save_file.read()
            note_save_file.close()
        else:
            content = ""


        print(content)

        if content == "{}" or content == "":
            self.make_new_note(None)
        else:
            self.load_notes()