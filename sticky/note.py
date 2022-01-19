#!/usr/bin/python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy, Pango

print("Note class imported!")

class new_note():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("sticky/template/note.ui")

        self.note_window = self.builder.get_object("Note")
        self.note_window.set_skip_taskbar_hint(True)
        self.note_window.set_keep_below(True)
        self.note_window.set_decorated(True)

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
