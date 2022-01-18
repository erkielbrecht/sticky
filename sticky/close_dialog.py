#!/usr/bin/python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy

print("Close Dialog class imported!")

class new_close_dialog():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("sticky/template/close.ui")

        self.close_window = self.builder.get_object("CloseWindow")
        self.close_window.set_skip_taskbar_hint(True)
        self.close_window.set_decorated(True)

        self.cancel_button = self.builder.get_object("CancelButton")

        self.close_button = self.builder.get_object("CloseButton")