import PySimpleGUI as sg
import os.path
from module.Process import Process
from module.Buffer import Buffer
from module.LexicalAnalyzer import LexicalAnalyzer

#
# LAYOUT
#
source_column = [
    [
        sg.Text("Load From File"),
        sg.In(size=(25, 1), enable_events=True, key="-FILENAME-"),
        sg.FileBrowse(key="browseFile", file_types=(
            ("Text Files", "*.txt, *.c"),)),
    ],
    [
        sg.Multiline(enter_submits=False, autoscroll=True, visible=True,
                     do_not_clear=True, size=(50, 30), key="source")
    ],
]

list_button = [
    [sg.Button("Process", pad=(0, 20), key='process')],
    [sg.Button("Reset", key='reset')]
]

output_column = [
    [
        sg.Text("Lexical Analysis", justification='center',
                font="Poppins", auto_size_text=True)
    ],
    [
        sg.Listbox(values=[], size=(50, 30), key="-FILE LIST-")
    ]
]

# ----- Full layout -----
layout = [
    [
        sg.Column(source_column),
        sg.VSeperator(),
        sg.Column(list_button),
        sg.VSeperator(),
        sg.Column(output_column),
    ]
]

window = sg.Window("FY Mini Compiler", layout)

#
# VARIABEL
#

Buffer = Buffer()
Process = Process()
Analyzer = LexicalAnalyzer()
result = []

# Program
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "process":
        filePath = values["-FILENAME-"]
        t, lex, lin, col, res = Process.process(
            path=filePath, Buffer=Buffer, Analyzer=Analyzer)
        result = res
        window.Element("-FILE LIST-").update(result)
    if event == "reset":
        window.Element("source").update("")
    if event == "-FILENAME-":
        filePath = values["-FILENAME-"]
        window.Element("source").Update(Buffer.load_file(path=filePath))

window.close()
