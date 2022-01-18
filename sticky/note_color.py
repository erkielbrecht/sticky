#!/usr/bin/python3

from re import match
import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy

print("Note color handler imported!")

def set_note_color(widget, color, note):
    window_context = note.note_window.get_style_context()
    if color == "strawberry":
        window_context.add_class("funny")
    print("hello")
