#!/usr/bin/python3

import gi, os, sys, locale, gettext

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

try:
    current_locale, encoding = locale.getdefaultlocale()
    current_locale = current_locale.split("_", 1)[0]
    locale_path = os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)
        ), 
        'locale'
    )
    translate = gettext.translation(
        "sticky", 
        locale_path, 
        [current_locale] 
    )
    _ = translate.gettext
except FileNotFoundError:
    _ = str


print("Close Dialog class imported!")

class new_close_dialog():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(data_path + "/data/template/close.ui")

        self.close_window = self.builder.get_object("CloseWindow")
        self.close_window.set_skip_taskbar_hint(True)
        self.close_window.set_decorated(True)

        self.info_label = self.builder.get_object("CloseMessage")
        self.info_label.set_text(_("Do you wish to close this note?\nIt will be deleted."))

        self.cancel_button = self.builder.get_object("CancelButton")

        self.close_button = self.builder.get_object("CloseButton")