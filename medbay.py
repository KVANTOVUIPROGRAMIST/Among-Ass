import sys, os, random, subprocess
from PIL import Image
from PIL import ImageDraw
import PySimpleGUI as s

a = 0
b = random.randint(1, 3)
layout = [
    [s.Text("Check your eyes, what color do you see?", font=("Helvetica", 25))],
    [s.Button("Red")],
    [s.Button("Green")],
    [s.Button("Blue")]
]

window = s.Window("med", layout, margins=(300, 300))

if b == 1:
    color = (255, 0, 0)
if b == 2:
    color = (0, 255, 0)
if b == 3:
    color = (0, 0, 255)

img = Image.new('RGB', (100, 50), color)
imgDrawer = ImageDraw.Draw(img)
img.save("1.png")

os.system("1.png")

while True:
    event, values = window.read()
    if event == s.WIN_CLOSED:
        break
    elif event == "Red" and b == 1:
        s.Popup("All clear u can go")
        subprocess.Popen('main_ui.py 1', shell=True)
        sys.exit(0)
    elif event == "Green" and b == 2:
        s.Popup("All clear u can go")
        subprocess.Popen('main_ui.py 1', shell=True)
        sys.exit(0)
    elif event == "Blue" and b == 3:
        s.Popup("All clear u can go")
        subprocess.Popen('main_ui.py 1', shell=True)
        sys.exit(0)
    else:
        s.Popup("test not passed!")
        sys.exit(0)
window.close()
