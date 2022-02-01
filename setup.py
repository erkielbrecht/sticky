#!/usr/bin/python3
import sys
from distutils.core import setup
from distutils.command.install import install as _install


class install(_install):
    def run(self):
        _install.run(self)

install_data = [
    ('share/applications', ['data/com.github.erkielbrecht.sticky.desktop']),
    ('share/metainfo', ['data/com.github.erkielbrecht.sticky.appdata.xml']),
    ('share/icons/hicolor/128x128/apps',['data/icons/app/128/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/64x64/apps',['data/icons/app/64/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/48x48/apps',['data/icons/app/48/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/32x32/apps',['data/icons/app/32/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/24x24/apps',['data/icons/app/24/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/16x16/apps',['data/icons/app/16/com.github.erkielbrecht.sticky.svg']),
    ('bin/sitcky/data',['data/note.css']),
    ('bin/sitcky/data/icons',['data/icons/banana_circle.svg']),
    ('bin/sitcky/data/icons',['data/icons/blueberry_circle.svg']),
    ('bin/sitcky/data/icons',['data/icons/lime_circle.svg']),
    ('bin/sitcky/data/icons',['data/icons/strawberry_circle.svg']),
    ('bin/sitcky/data/template',['data/template/note.ui']),
    ('bin/sitcky/data/template',['data/template/close.ui']),
    ('bin/sitcky/data/template',['data/template/settings.ui']),
    ('bin/sitcky',['src/main.py']),
    ('bin/sitcky',['src/note_handler.py']),
    ('bin/sitcky',['src/note.py']),
    ('bin/sitcky',['src/note_color.py']),
    ('bin/sitcky',['src/settings_dialog.py']),
    ('bin/sitcky',['src/close_dialog.py']),
    ('bin/sitcky',['src/__init__.py']),
]

setup(  
    name='Sticky',
    version='0.0.1',
    author='Erki Elbrecht',
    description='Simple sticky notes for your desktop',
    url='https://github.com/erkielbrecht/sticky',
    license='GNU GPL3',
    scripts=['com.github.erkielbrecht.sticky'],
    packages=['src'],
    data_files=install_data,
    cmdclass={'install': install}
)