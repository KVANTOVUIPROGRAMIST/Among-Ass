import time, random
import PySimpleGUI as sg
def wave(height):
    while True:
        a = 0
        b = 0

        while a != height:
            print(' '*a + '-')
            a+=1
            time.sleep(0.02)
        if a == height:
            while a != 0:
                print(' '*a + '-')
                a-=1
                time.sleep(0.02)
x = random.randint(1, 100)
wave(x)
sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()