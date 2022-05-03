# capslock-to-backspace
A Python script that will replace each instance of Caps Lock with Backspace.

I find this is helpful for typing fast and reducing pinkey strain. PowerToys is better for this problem but cannot be installed without admin access.

## Installation/Use
Place the .py in a folder of choice (I created one in Appdata/Roaming). You can add a shortcut to this file in shell:startup so it will start automatically when Windows is started. By changing the properties of the shortcut, you can have it start minimized so you don't have to minimize it every time. Alternatively, you can have it run in the background as a .pyw (untested)

## Known Issue
If you roll from Caps Lock to the next key (example: I typed "Pythom", then hit Caps Lock to delete the m and started to press n before releasing Caps Lock), the letter will be capitalized. This rolling is a good thing since it helps one type faster so it's a shame this is an issue, but I don't have the time to fix this issue right now. Pull requests/suggestions welcome!
