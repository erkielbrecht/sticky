#!/usr/bin/python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy

print("Note class imported!")

class new_note():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("sticky/template/note.ui")

        self.note_window = self.builder.get_object("Note")
        self.note_window.set_skip_taskbar_hint(True)
        self.note_window.set_keep_below(True)
        self.note_window.set_decorated(True)

        self.note_text = self.builder.get_object("Tex")

        self.add_button = self.builder.get_object("AddButton")

        self.close_button = self.builder.get_object("ExitButton")
