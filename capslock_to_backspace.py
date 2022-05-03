import keyboard

def unpress_caps(a):
    keyboard.send("caps lock")

keyboard.on_release_key("caps lock", unpress_caps)

while True:
    keyboard.wait("caps lock")
    keyboard.send("backspace")
