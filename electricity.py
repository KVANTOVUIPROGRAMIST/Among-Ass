import PySimpleGUI as s
import subprocess, time, random, sys
from multiprocessing import Process
import pyautogui as p

layout = [
    [s.Text("Try to click on each button!", font=("Helvetica", 25))],
    [s.Button("1")],
    [s.Button("2")],
    [s.Button("3")],
    [s.Button("4")],
    [s.Button("5")]
]

window = s.Window("get me", layout, margins=(300, 300))

def mouse_move():
    while True:
        x = random.randint(950, 970)
        y = random.randint(530, 550)
        p.moveTo(x, y)
        time.sleep(1)
def win():
    while True:
        event, values = window.read()
        if event == s.WIN_CLOSED:
            break
        elif event == '1':
            s.Popup('Keep going!')
            pass
        elif event == '2':
            s.Popup('Keep going!')
            pass
        elif event == '3':
            s.Popup('Keep going!')
            pass
        elif event == '4':
            s.Popup('Keep going!')
            pass
        elif event == '5':
            s.Popup('Good, test for good coordination passed!')
            time.sleep(2)
            subprocess.Popen('main_ui.py 1', shell=True)
            sys.exit(0)

def main():
    Process(target=win).start()
    Process(target=mouse_move).start()
    window.close()
if __name__ == '__main__':
    main()
