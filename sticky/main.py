import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')
gi.require_version('Handy', "1")

from gi.repository import Gtk, Gdk, Handy

note_count = 0

Handy.init()


def note_check():
    global note_count
    if note_count == 0:
        Gtk.main_quit()


def make_new_note(widget):
    global note_count
    globals()[f"note_{note_count}"] = new_note()
    globals()[f"note_{note_count}"].note_window.present()
    note_count += 1


class new_note():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("sticky/template/note.ui")

        self.note_window = self.builder.get_object("Note")
        self.note_window.set_skip_taskbar_hint(True)
        self.note_window.set_keep_below(True)
        self.note_window.set_decorated(True)

        self.add_button = self.builder.get_object("AddButton")
        self.add_button.connect("clicked", make_new_note)

        self.close_button = self.builder.get_object("ExitButton")
        self.close_button.connect("clicked", self.close_note)

    def close_note(self, widget):
        global note_count
        self.note_window.destroy()
        note_count -= 1
        note_check()


screen = Gdk.Screen.get_default()
provider = Gtk.CssProvider()
provider.load_from_path("sticky/template/note.css")
Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
make_new_note(None)


Gtk.main()
