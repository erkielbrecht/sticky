#!/usr/bin/python3

import gi, os, sys

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy

launch_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Update sys.path to include modules
if launch_dir == "/usr/bin":
    data_path = "/usr/share/com.github.erkielbrecht.sticky/sticky"
else:
    data_path = launch_dir + "/sticky"

print("Settings Dialog class imported!")

class new_settings_dialog():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(data_path + "/data/template/settings.ui")

        self.settings_window = self.builder.get_object("SettingsWindow")

        self.title_label = self.builder.get_object("TitleLabel")

        title_context = self.title_label.get_style_context()

        title_context.add_class("settings-label")

        self.settings_window.set_skip_taskbar_hint(True)
        self.settings_window.set_decorated(True)

        self.settings_label = self.builder.get_object("SettingsLabel")

        label_context = self.settings_label.get_style_context()
        label_context.add_class("settings-label")

        self.close_button = self.builder.get_object("CloseButton")
        self.close_button.connect("clicked", self.close_window)

        close_context = self.close_button.get_style_context()
        close_context.add_class("settings-label")

        self.settings_switch = self.builder.get_object("SettingsSwitch")

        self.settings_switch.connect("state-set", self.handle_signal)

    def close_window(self, *args):
        self.settings_window.destroy()

    def handle_signal(self, widget, state):
        print(state)