import PySimpleGUI as sg
import os.path
import pandas as pd
import numpy as np
import datetime
import types
import csv

# Staffing Function
staff_count = 0



# Layout

layout = [[sg.Text("Welcome to DC Reporter")], [sg.Button("OK")]]


# Create the Window
# First the window layout in 2 columns
file_list_column = [
    [
        sg.Text('Title'),
        sg.InputText('SJC03 - Task List - Night-Shift - [date]')
    ],
    [
        sg.Text('Staffing', font=('Any 20'))
    ],
    [
        sg.InputText('employee 1', size=(20, 1)),
        sg.Checkbox('Checked In', size=(8, 1), default=False),
        sg.Checkbox('Call Out', size=(8, 1), default=False),
        sg.Checkbox('PTO', size=(8, 1), default=False),
        sg.Checkbox('Off', size=(8, 1), default=False)
    ], 
    [
        sg.InputText('employee 2', size=(20, 1)),
        sg.Checkbox('Checked In', size=(8, 1), default=False),
        sg.Checkbox('Call Out', size=(8, 1), default=False),
        sg.Checkbox('PTO', size=(8, 1), default=False),
        sg.Checkbox('Off', size=(8, 1), default=False)
    ], 
    [
        sg.InputText('employee 3', size=(20, 1)),
        sg.Checkbox('Checked In', size=(8, 1), default=False),
        sg.Checkbox('Call Out', size=(8, 1), default=False),
        sg.Checkbox('PTO', size=(8, 1), default=False),
        sg.Checkbox('Off', size=(8, 1), default=False)
    ], 
    [
        sg.InputText('employee 4', size=(20, 1)),
        sg.Checkbox('Checked In', size=(8, 1), default=False),
        sg.Checkbox('Call Out', size=(8, 1), default=False),
        sg.Checkbox('PTO', size=(8, 1), default=False),
        sg.Checkbox('Off', size=(8, 1), default=False)
    ], 
    [
        sg.InputText('employee 5', size=(20, 1)),
        sg.Checkbox('Checked In', size=(8, 1), default=False),
        sg.Checkbox('Call Out', size=(8, 1), default=False),
        sg.Checkbox('PTO', size=(8, 1), default=False),
        sg.Checkbox('Off', size=(8, 1), default=False)
    ],
    [
        sg.InputText('employee 6', size=(20, 1)),
        sg.Checkbox('Checked In', size=(8, 1), default=False),
        sg.Checkbox('Call Out', size=(8, 1), default=False),
        sg.Checkbox('PTO', size=(8, 1), default=False),
        sg.Checkbox('Off', size=(8, 1), default=False)
    ], 
    [
        sg.Text("Current Tasks", font=('Any 20'))
    ],
    [
        sg.InputText('[Task Name] [Ticket and/or Escalation]'),
        sg.InputText('Employee', size=(20, 1)) 
    ], 
    [
        sg.InputText('Transactions & Queues'),
        sg.InputText('All', size=(20, 1))
    ], 
    [
        sg.InputText('Hard Fail Servers'),
        sg.InputText('All', size=(20, 1))
    ], 
    [
        sg.InputText('Hard Fail Components'),
        sg.InputText('All', size=(20, 1))
    ], 
    [
        sg.InputText('Fast Server Pools '),
        sg.InputText('All', size=(20, 1))
    ], 
    [
        sg.InputText('Provision Readiness'),
        sg.InputText('All', size=(20, 1))
    ], 
    [
        sg.InputText('Think40'),
        sg.InputText('All', size=(20, 1))
    ], 
    [
        sg.InputText('Checkpoint'),
        sg.InputText('All', size=(20, 1))
    ], 
    [
        sg.Text('Job Tasks', font=('Any 20'))
    ], 
    [
        sg.Text('B.o.S Walkthrough: ', size=(15, 1)),
        sg.InputText('Employee', size=(20, 1))
    ],
    [
        sg.Text('E.o.S Walkthrough: ', size=(15, 1)),
        sg.InputText('Employee', size=(20, 1))
    ],
    [
        sg.Text('Hand-off Report: ', size=(15, 1)),
        sg.InputText('Employee', size=(20, 1))
    ],
    [
        sg.Text('E.o.S Check-out: ', size=(15, 1)),
        sg.InputText('Employee', size=(20, 1))
    ],
    [
        sg.Text('Maintenance(s)', font=('Any 20'))
    ], 
    [
        sg.InputText('[Ticket Link]'),
        sg.InputText('[Employee]', size=(20, 1))
    ],
    [
        sg.InputText('[Ticket Link]'),
        sg.InputText('[Employee]', size=(20, 1))
    ],
    [
        sg.Button('Create')
    ]
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Right Panel Viewer")],
    [sg.Text(size=(40, 1), key="-TOUT-")]
    
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Task List", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes the window or 
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()
