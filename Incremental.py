import PySimpleGUI as sg
import math
import random

sg.theme("DarkAmber")

def window1():
    layout_column = [[sg.Text("Welcome to my simple Incremental Game!", font = ("Helvetica", 25))],
    [sg.Text("In this game your goal is to collect simple \"stats\" which will all increase your money gain.", font = ("Helvetica", 25))],
    [sg.Text("Some stats will reset others, so pay attention to what each stat does.", font = ("Helvetica", 25))],
    [sg.Text("This is just an experiment that I am building from the ground up, so it will be rather experimental.", font = ("Helvetica", 25))],
    [sg.Button("Next",font = ("Helvetica", 15))]
    ]
    layout = [[sg.Column(layout_column, element_justification='center')]]

    window = sg.Window("Intro", layout)

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Next":
            break
    window.close()

window1()