import random, time, sys, subprocess
import PySimpleGUI as s

f = open('txt.txt', 'w')
i = 0
b = None
m = None
n = 0
g = 0
c = []
l = []
h = []


def write_pass_file():
    i = 0
    while i != 5:
        b = str(random.randint(0, 5))
        f.write(b)
        i += 1
        h.append(b)
    f.close()


def check_pass(value):
    for g in range(4):
        if value[g] != h[g]:
            s.Popup('Password incorect')
            sys.exit(0)
        else:
            pass

def main():
    write_pass_file()
    value = s.PopupGetText('Enter pass from txt file', 'Checking you!')
    check_pass(value)
    s.Popup('Good, downloading...')
    layout = [[s.ProgressBar(100, orientation='h', size=(50, 20), key='progressbar')]]
    window = s.Window('Progress').Layout(layout)
    progress_bar = window.FindElement('progressbar')
    for i in range(10000):
        event, values = window.Read(timeout=0)
        progress_bar.UpdateBar(i + 2)
    time.sleep(1)
    window.Close()
    s.Popup('Done!')
    subprocess.Popen('main_ui.py 1', shell=True)
    sys.exit(0)
