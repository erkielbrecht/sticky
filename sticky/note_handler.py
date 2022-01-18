#!/usr/bin/python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy
from collections import OrderedDict

import note
import close_dialog
import note_color

print("Note handler imported!")

class note_handler():
    note_list = OrderedDict()
    counter = 0

    def note_check(self):
        if len(self.note_list) == 0:
            Gtk.main_quit()

    def make_new_note(self, widget):

        self.counter += 1

        new_note = note.new_note()
        new_note.add_button.connect("clicked", self.make_new_note)
        new_note.close_button.connect("clicked", self.close_note, self.counter)
        new_note.note_window.present()

        new_note.banana_button.connect("clicked", note_color.set_note_color, "banana", new_note)
        new_note.strawberry_button.connect("clicked", note_color.set_note_color, "strawberry", new_note)
        new_note.lime_button.connect("clicked", note_color.set_note_color, "lime", new_note)
        new_note.blueberry_button.connect("clicked", note_color.set_note_color, "blueberry", new_note)

        self.note_list[self.counter] = new_note

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

            _close_dialog.close_window.set_transient_for(c_note_window)

            _close_dialog.close_window.present()
            
            _close_dialog.cancel_button.connect("clicked", destroy_dialog)

            _close_dialog.close_button.connect("clicked", destroy_dialog_note)


    def __init__(self):
        self.make_new_note(None)