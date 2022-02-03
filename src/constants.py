import gi
import os
print("troll")
import locale
print("troll")
import gettext
print("troll")

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
print("troll")
try:
    current_locale, encoding = locale.getdefaultlocale()
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

print("fakfak")
class App:
    application_shortname = "sticky"
    application_id = "com.github.erkielbrecht.sticky"
    application_name = "Sticky"
    application_description = _('Simple sticky notes for your desktop')
    application_version ="0.0.1"
    app_years = "2022"
    main_url = "https://github.com/erkielbrecht/sticky"
    bug_url = "https://github.com/erkielbrecht/sticky/issues"
    help_url = "https://github.com/erkielbrecht/sticky/issues"
    translate_url = "https://github.com/erkielbrecht/sticky"
    about_comments = application_description
    about_license_type = Gtk.License.GPL_3_0