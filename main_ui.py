import PySimpleGUI as sg
import subprocess as s
import suc_ui

layout = [
    [sg.Text(" Among US with you and your PC!",font=("Helvetica", 25))],
    [sg.Button("Emengercy exit!")],
    [sg.Button("Task 1")],
    [sg.Button("Task 2")],
    [sg.Button("Task 3")]
]

window = sg.Window("Main", layout, margins=(300, 300))

while True:
    event, values = window.read()
    if event == "Emengercy exit!" or event == sg.WIN_CLOSED:
        break
    elif event == "Task 1":
        s.Popen('suc_ui.py 1', shell=True)
        suc_ui.main()
    elif event == "Task 2":
        s.Popen('medbay.py 1', shell=True)

window.close()
