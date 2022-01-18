#!/usr/bin/python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy

from note_handler import note_handler

class Application(Gtk.Application):

    def do_activate(self):
        print("App started!")

        Handy.init()

        print("Handy intitated!")

        self._note_handler = note_handler()

        print("Note handler decleared!")

        Gtk.main()
    
    
def start():
    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path("sticky/template/note.css")
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    app = Application()
    app.run("")
