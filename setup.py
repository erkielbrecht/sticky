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
    ('share/icons/hicolor/128x128@2/apps',['data/icons/app/128/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/64x64@2/apps',['data/icons/app/64/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/48x48@2/apps',['data/icons/app/48/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/32x32@2/apps',['data/icons/app/32/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/24x24@2/apps',['data/icons/app/24/com.github.erkielbrecht.sticky.svg']),
    ('share/icons/hicolor/16x16@2/apps',['data/icons/app/16/com.github.erkielbrecht.sticky.svg']),
    ('bin/sticky/data',['data/note.css']),
    ('bin/sticky/data/icons',['data/icons/banana_circle.svg']),
    ('bin/sticky/data/icons',['data/icons/blueberry_circle.svg']),
    ('bin/sticky/data/icons',['data/icons/lime_circle.svg']),
    ('bin/sticky/data/icons',['data/icons/strawberry_circle.svg']),
    ('bin/sticky/data/template',['data/template/note.ui']),
    ('bin/sticky/data/template',['data/template/close.ui']),
    ('bin/sticky',['src/constants.py']),
    ('bin/sticky',['src/main.py']),
    ('bin/sticky',['src/note_handler.py']),
    ('bin/sticky',['src/note.py']),
    ('bin/sticky',['src/note_color.py']),
    ('bin/sticky',['src/close_dialog.py']),
    ('bin/sticky',['src/__init__.py']),
    ('bin/sticky/locale/et/LC_MESSAGES', ['po/et/LC_MESSAGES/sticky.po'])
]

setup(  
    name='Sticky',
    version='0.0.3',
    author='Erki Elbrecht',
    description='Simple sticky notes for your desktop',
    url='https://github.com/erkielbrecht/sticky',
    license='GNU GPL3',
    scripts=['com.github.erkielbrecht.sticky'],
    packages=['src'],
    data_files=install_data,
    cmdclass={'install': install}
)