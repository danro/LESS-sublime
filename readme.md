# LESS syntax package for Sublime Text 2

Provides syntax highlighting for `.less` files + support for comment-toggle commands.

## Installing

**With the Package Control plugin:** The easiest way to install this package is through Package Control, which can be found at this site: [http://wbond.net/sublime_packages/package_control](http://wbond.net/sublime_packages/package_control)

Once you install Package Control, restart ST2 and bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select `LESS` when the list appears.

**Without Git:** Download the latest source zip from [github](https://github.com/danro/LESS-sublime/zipball/master) and extract the files to your Sublime Text "Packages" directory, into a new directory named `LESS`.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/danro/LESS-sublime.git LESS

The "Packages" directory is located at:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`

## Color Scheme

Some snippets to use in your favorite `.tmTheme` file.

```xml
<dict>
  <key>name</key>
  <string>css.id</string>
  <key>scope</key>
  <string>meta.selector.css entity.other.attribute-name.id</string>
  <key>settings</key>
  <dict>
    <key>foreground</key>
    <string>#E5D56D</string>
  </dict>
</dict>
<dict>
  <key>name</key>
  <string>css.class</string>
  <key>scope</key>
  <string>entity.other.attribute-name.class</string>
  <key>settings</key>
  <dict>
    <key>foreground</key>
    <string>#A0C25F</string>
  </dict>
</dict>
<dict>
  <key>name</key>
  <string>less.mixin</string>
  <key>scope</key>
  <string>entity.other.less.mixin</string>
  <key>settings</key>
  <dict>
    <key>foreground</key>
    <string>#98E124</string>
  </dict>
</dict>
<dict>
  <key>name</key>
  <string>css.element</string>
  <key>scope</key>
  <string>keyword.control.html.elements</string>
  <key>settings</key>
  <dict>
    <key>foreground</key>
    <string>#DA4632</string>
  </dict>
</dict>
<dict>
  <key>name</key>
  <string>css.string</string>
  <key>scope</key>
  <string>meta.attribute-selector.css string</string>
  <key>settings</key>
  <dict>
    <key>foreground</key>
    <string>#FF950A</string>
  </dict>
</dict>
```
[Copied from my Sublime theme](https://github.com/danro/refined-theme/blob/master/Color%20Schemes/Danro.tmTheme)