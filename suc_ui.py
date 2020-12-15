import random, time, sys, subprocess
import PySimpleGUI as s

f = open('txt.txt', 'w')
i = 0
b = None
m = None
g = 0
c = []
n = []
l = []


def write_pass_file():
    i = 0
    while i != 5:
        b = str(random.randint(0, 5))
        f.write(b)
        i += 1
        c.append(b)
    f.close()


def check_pass(c):
    for g in range(4):
        if c[g] != l[g]:
            s.Popup('Password incorect')
            sys.exit(0)
        else:
            pass


write_pass_file()
value = s.PopupGetText('Enter pass from txt file', 'Checking you!')
print(value)
n = str(value)
l = list(n)
check_pass(c)
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