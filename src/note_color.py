#!/usr/bin/python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy

print("Note color handler imported!")

css_classes = [
    "banana-border",
    "banana-header-border",
    "banana-background",
    "banana-font",
    "strawberry-border",
    "strawberry-header-border",
    "strawberry-background",
    "strawberry-font",
    "lime-border",
    "lime-header-border",
    "lime-background",
    "lime-font",
    "blueberry-border",
    "blueberry-header-border",
    "blueberry-background",
    "blueberry-font",
]

def set_note_color(widget, color, note):

    note.color = color


    window_context = note.note_window.get_style_context()

    add_button_context = note.add_button.get_style_context()
    close_button_context = note.close_button.get_style_context()
    picker_button_context = note.picker_button.get_style_context()

    bold_button_context = note.bold_button.get_style_context()
    underline_button_context = note.underline_button.get_style_context()
    italic_button_context = note.italic_button.get_style_context()

    settings_button_context = note.settings_button.get_style_context()

    textview_context = note.note_text.get_style_context()

    headerbar_context = note.header_bar.get_style_context()

    popover_context = note.color_menu.get_style_context()

    if color == "banana":

        border = "banana-border"
        header_border = "banana-header-border"
        background = "banana-background"
        font = "banana-font"

    elif color == "strawberry":

        border = "strawberry-border"
        header_border = "strawberry-header-border"
        background = "strawberry-background"
        font = "strawberry-font"

    elif color == "lime":

        border = "lime-border"
        header_border = "lime-header-border"
        background = "lime-background"
        font = "lime-font"
    
    elif color == "blueberry":

        border = "blueberry-border"
        header_border = "blueberry-header-border"
        background = "blueberry-background"
        font = "blueberry-font"
    
    else:

        border = "banana-border"
        header_border = "banana-header-border"
        background = "banana-background"
        font = "banana-font"

    for x in window_context.list_classes():
        if x in css_classes:
            window_context.remove_class(x)

    window_context.add_class(border)
    window_context.add_class(background)

    for x in add_button_context.list_classes():
        if x in css_classes:
           add_button_context.remove_class(x)
    
    add_button_context.add_class(font)

    for x in close_button_context.list_classes():
        if x in css_classes:
           close_button_context.remove_class(x)

    close_button_context.add_class(font)

    for x in picker_button_context.list_classes():
        if x in css_classes:
           picker_button_context.remove_class(x)

    picker_button_context.add_class(font)

    for x in bold_button_context.list_classes():
        if x in css_classes:
           bold_button_context.remove_class(x)

    bold_button_context.add_class(font)

    for x in italic_button_context.list_classes():
        if x in css_classes:
           italic_button_context.remove_class(x)

    italic_button_context.add_class(font)

    for x in underline_button_context.list_classes():
        if x in css_classes:
           underline_button_context.remove_class(x)

    underline_button_context.add_class(font)

    for x in settings_button_context.list_classes():
        if x in css_classes:
           settings_button_context.remove_class(x)

    settings_button_context.add_class(font)
    print(settings_button_context.list_classes())

    for x in textview_context.list_classes():
        if x in css_classes:
           textview_context.remove_class(x)

    textview_context.add_class(background)
    textview_context.add_class(font)

    for x in headerbar_context.list_classes():
        if x in css_classes:
           headerbar_context.remove_class(x)

    headerbar_context.add_class(background)
    headerbar_context.add_class(header_border)

    for x in popover_context.list_classes():
        if x in css_classes:
           popover_context.remove_class(x)

    popover_context.add_class(background)
    popover_context.add_class(border)

def set_dialog_color(color, dialog):

    window_context = dialog.close_window.get_style_context()

    close_button_context = dialog.close_button.get_style_context()
    cancel_button_context = dialog.cancel_button.get_style_context()

    label_context = dialog.info_label.get_style_context()

    if color == "banana":

        border = "banana-border"
        background = "banana-background"
        font = "banana-font"

    elif color == "strawberry":

        border = "strawberry-border"
        background = "strawberry-background"
        font = "strawberry-font"

    elif color == "lime":

        border = "lime-border"
        background = "lime-background"
        font = "lime-font"
    
    elif color == "blueberry":

        border = "blueberry-border"
        background = "blueberry-background"
        font = "blueberry-font"
    
    else:

        border = "banana-border"
        background = "banana-background"
        font = "banana-font"

    for x in window_context.list_classes():
        if x in css_classes:
            window_context.remove_class(x)

    window_context.add_class(border)
    window_context.add_class(background)

    for x in close_button_context.list_classes():
        if x in css_classes:
           close_button_context.remove_class(x)

    close_button_context.add_class("smaller-font")
    close_button_context.add_class(font)

    for x in cancel_button_context.list_classes():
        if x in css_classes:
           cancel_button_context.remove_class(x)

    cancel_button_context.add_class("smaller-font")
    cancel_button_context.add_class(font)

    for x in label_context.list_classes():
        if x in css_classes:
           label_context.remove_class(x)

    label_context.add_class("smaller-font")
    label_context.add_class(font)

