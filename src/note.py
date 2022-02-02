#!/usr/bin/python3

import gi, os, sys

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

launch_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Update sys.path to include modules
if launch_dir == "/usr/bin":
    data_path = "/usr/share/com.github.erkielbrecht.sticky/sticky"
else:
    data_path = launch_dir + "/sticky"

from gi.repository import Gtk, Gdk, Handy, Pango

print("Note class imported!")

class new_note():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(data_path + "/data/template/note.ui")

        self.note_window = self.builder.get_object("Note")
        self.note_window.set_skip_taskbar_hint(True)
        self.note_window.set_keep_below(True)
        self.note_window.set_decorated(True)
        #self.note_window.set_type_hint(Gdk.WindowTypeHint.DOCK)

        self.note_accelerators = Gtk.AccelGroup()
        self.note_window.add_accel_group(self.note_accelerators)

        self.key, self.mod = Gtk.accelerator_parse("<Control>q")

        self.note_text = self.builder.get_object("Tex")
        self.text_buffer = self.note_text.get_buffer()

        self.tag_bold = self.text_buffer.create_tag("bold", weight=Pango.Weight.BOLD)
        self.tag_italic = self.text_buffer.create_tag("italic", style=Pango.Style.ITALIC)
        self.tag_underline = self.text_buffer.create_tag("underline", underline=Pango.Underline.SINGLE)

        self.add_button = self.builder.get_object("AddButton")
        self.close_button = self.builder.get_object("ExitButton")
        self.picker_button = self.builder.get_object("PickerButton")

        self.bold_button = self.builder.get_object("BoldButton")
        self.italic_button = self.builder.get_object("ItalicButton")
        self.underline_button = self.builder.get_object("UnderlineButton")

        self.settings_button = self.builder.get_object("SettingsButton")

        self.header_bar = self.builder.get_object("Header")

        self.color_menu = self.builder.get_object("ColorMenu")

        self.color = "banana"

        self.banana_button = self.builder.get_object("BananaButton")
        self.strawberry_button = self.builder.get_object("StrawberryButton")
        self.lime_button = self.builder.get_object("LimeButton")
        self.blueberry_button = self.builder.get_object("BlueberryButton")

        self.banana_image = self.builder.get_object("BananaCircle")
        self.banana_image.set_from_file(data_path + "/data/icons/banana_circle.svg")

        self.blueberry_image = self.builder.get_object("BlueCircle")
        self.blueberry_image.set_from_file(data_path + "/data/icons/blueberry_circle.svg")

        self.strawberry_image = self.builder.get_object("BerryCircle")
        self.strawberry_image.set_from_file(data_path + "/data/icons/strawberry_circle.svg")

        self.lime_image = self.builder.get_object("LimeCircle")
        self.lime_image.set_from_file(data_path + "/data/icons/lime_circle.svg")
