import PySimpleGUI as sg
import os
import pyautogui as p
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
sg.theme('DarkAmber')
i = 0
link1 = 'magnet:?xt=urn:btih:e80be514dba0112c3212f59817701d8a31ae4cb3'
link2 = 'magnet:?xt=urn:btih:4ab487771694cc485561798ab08e9764a000c4f6'
link3 = 'magnet:?xt=urn:btih:b7ab3c13cb94bf1541c09214f99cf82e91049a12'
link4 = 'magnet:?xt=urn:btih:796400af1c7bd0573195842e27b79b5d44fad41a'
link5 = 'magnet:?xt=urn:btih:e202d3bf5499b3579095fdf6ec335a2d9e2c222e'
link6 = 'magnet:?xt=urn:btih:42f9fdbfa3fc8a8c4509ab8d1ca27917807ea3a2'
link7 = 'magnet:?xt=urn:btih:88bf413ff25f25e4383a0075e207f70206abed40'

layout = [
    [sg.Text('Here list of Adobe programs for 2020 version!', font=('Helvetica', 25))],
    [sg.Button('Adobe Photoshop', size=(15, 4))],
    [sg.Button('Adobe Illustrator', size=(15, 4))],
    [sg.Button('Adobe Lightroom', size=(15, 4))],
    [sg.Button('Adobe Premier Pro', size=(15, 4))],
    [sg.Button('Adobe After Effects', size=(15, 4))],
    [sg.Button('Adobe InDesign', size=(15, 4))],
    [sg.Button('Adobe Dreamweaver', size=(15, 4))]
]

window = sg.Window("Wassup", layout, margins=(200, 200))

while True:
    event, status = window.read()
    if event == 'Adobe Photoshop':
        os.startfile(r'C:/uTorrent.lnk')
        x = 599
        y = 299
        time.sleep(5)
        p.moveTo(x, y)
        p.click()
        for i in range(len(link1)):
            keyboard.press(link1[i])
            keyboard.release(link1[i])
        keyboard.press(Key.enter)
    if event == 'Adobe Illustrator':
        os.startfile(r'C:/uTorrent.lnk')
        x = 599
        y = 299
        time.sleep(5)
        p.moveTo(x, y)
        p.click()
        for i in range(len(link2)):
            keyboard.press(link2[i])
            keyboard.release(link2[i])
        keyboard.press(Key.enter)
    if event == 'Adobe Lightroom':
        os.startfile(r'C:/uTorrent.lnk')
        x = 599
        y = 299
        time.sleep(5)
        p.moveTo(x, y)
        p.click()
        for i in range(len(link3)):
            keyboard.press(link3[i])
            keyboard.release(link3[i])
        keyboard.press(Key.enter)
    if event == 'Adobe Premier Pro':
        os.startfile(r'C:/uTorrent.lnk')
        x = 599
        y = 299
        time.sleep(5)
        p.moveTo(x, y)
        p.click()
        for i in range(len(link4)):
            keyboard.press(link4[i])
            keyboard.release(link4[i])
        keyboard.press(Key.enter)
    if event == 'Adobe After Effects':
        os.startfile(r'C:/uTorrent.lnk')
        x = 599
        y = 299
        time.sleep(5)
        p.moveTo(x, y)
        p.click()
        for i in range(len(link5)):
            keyboard.press(link5[i])
            keyboard.release(link5[i])
        keyboard.press(Key.enter)
    if event == 'Adobe InDesign':
        os.startfile(r'C:/uTorrent.lnk')
        x = 599
        y = 299
        time.sleep(5)
        p.moveTo(x, y)
        p.click()
        for i in range(len(link6)):
            keyboard.press(link6[i])
            keyboard.release(link6[i])
        keyboard.press(Key.enter)
    if event == 'Adobe Dreamweaver':
        os.startfile(r'C:/uTorrent.lnk')
        x = 599
        y = 299
        time.sleep(5)
        p.moveTo(x, y)
        p.click()
        for i in range(len(link7)):
            keyboard.press(link7[i])
            keyboard.release(link7[i])
        keyboard.press(Key.enter)