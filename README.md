<p align="center">
  <img src="https://github.com/erkielbrecht/sticky/blob/1951688c933b9577c7d2bed629c0e290870f9ff5/data/icons/app/128/com.github.erkielbrecht.sticky.svg" alt="Icon" />
</p>
<h1 align="center">Sticky</h1>
<h4 align="center">A simple sticky note app for your elementary os desktop.</h4>

<!--<p align="center">
  <a href="https://appcenter.elementary.io/..."><img src="https://appcenter.elementary.io/badge.svg" alt="Get it on AppCenter" /></a>
</p>-->

<p align="center">
  <a href="https://github.com/erkielbrecht/sticky/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-GPL3.0-blue.svg?style=for-the-badge">
  </a>
  <a href="https://github.com/erkielbrecht/sticky/releases">
    <img src="https://img.shields.io/badge/Release-v%201.0.2-blue.svg?style=for-the-badge">
  </a>
</p>
 ![Screenshot](https://github.com/erkielbrecht/sticky/blob/main/data/screenshots/screenshot1.png) 
 ![Screenshot](https://github.com/erkielbrecht/sticky/blob/main/data/screenshots/screenshot2.png) |

# Dependencies
  - `granite (>= 0.6.0)`
  - `libgtk-3-dev (>= 3.10)`
  - `python3 (>= 3.6)`
  - `python3-gi (3.36.0-1)`
  -  `gettext`
  -  `handy`
  -  `json`

# Building
  ```
    git clone https://github.com/ekrielbrecht/sticky.git
    cd sticky
    flatpak-builder build com.github.erkielbrecht.sticky.yml --user --install --force-clean
  ```
# Extras
   - Thanks to [Mirko Brombin](https://github.com/mirkobrombin) for the [template](https://github.com/mirkobrombin/ElementaryPython).
