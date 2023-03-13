import PySimpleGUI as sg
import math
import random
import Stats

pS = StatSheet()

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
            window.close()
            window2()
    window.close()

def window2():
    layout_column = [[sg.Text(f"Money:{money}")],
    [sg.Button("Dig")],
    [sg.Button("1 Dirt ($10)")]
    ]
    layout = [[sg.Column(layout_column, element_justification='center')]]

    window = sg.Window("Buttons", layout)

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Dig":
            if dirt > 0:
                money += dirt       
        if event == "1 Dirt ($10)":
            if money >= 0:
                dirt += 1
    window.close()

window1()