#!/usr/bin/python3

import gi
import os, sys

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")
gi.require_version('Granite', "1.0")

from gi.repository import Gtk, Gdk, Handy, Granite

from note_handler import note_handler

launch_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Update sys.path to include modules
if launch_dir == "/usr/bin":
    data_path = "/usr/share/com.github.erkielbrecht.sticky/sticky"
else:
    data_path = launch_dir + "/sticky"

class Application(Gtk.Application):

    def do_activate(self):

        self.granite_settings = Granite.Settings()
        self.gtk_settings = Gtk.Settings.get_default()

        if self.granite_settings.get_prefers_color_scheme() == Granite.SettingsColorScheme.DARK:
            self.gtk_settings.set_property("gtk-application-prefer-dark-theme", True) 

        self.granite_settings.connect("notify::prefers-color-scheme", self.color_scheme_changed)

        print("App started!")

        Handy.init()

        print("Handy intitated!")

        self._note_handler = note_handler()

        print("Note handler decleared!")

        Gtk.main()

    def color_scheme_changed(self, *args):
        if self.granite_settings.get_prefers_color_scheme() == Granite.SettingsColorScheme.DARK:
            self.gtk_settings.set_property("gtk-application-prefer-dark-theme", True)
        else:
            self.gtk_settings.set_property("gtk-application-prefer-dark-theme", False)
    
    
def start():
    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path(data_path + "/data/note.css")
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    app = Application()
    app.run("")
