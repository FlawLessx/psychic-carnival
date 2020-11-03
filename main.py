import PySimpleGUI as sg
import os.path
from module.Process import Process
from module.Buffer import Buffer
from module.LexicalAnalyzer import LexicalAnalyzer
from numpy.matlib import rand

#
# VARIABEL
#

Buffer = Buffer()
Process = Process()
Analyzer = LexicalAnalyzer()
result = []

#
# LAYOUT
#
source_column = [
    [
        sg.Text("Load From File"),
        sg.In(size=(25, 1), enable_events=True, key="-FILENAME-"),
        sg.FileBrowse(key="browseFile", file_types=(
            ("Text Files", "*.txt"), ("Python Code", "*.py"), ("C Code", "*.c"), ("C++ Code", "*.cpp"))),
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
                auto_size_text=True)
    ],
    [
        sg.Listbox(values=[], size=(80, 30), key="Output")
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
# FUNCTION
#
def processFunc():
    filePath = ''
    fileSplit = ''
    extension = ''
    if values['-FILENAME-'] != '':
        filePath = values["-FILENAME-"]
        fileSplit = str(filePath).split('/')
        extension = fileSplit[len(fileSplit)-1].split('.')[1]
    else:
        extension = sg.PopupGetText('Input langguange (c, cpp, py): ',)

    code = str(values["source"])
    t, tType, lex, lin, col, res = Process.process(
        Buffer=Buffer, Analyzer=Analyzer, code=code.splitlines(), lang=extension)
    result = res
    window.Element("Output").update(result)


def resetFunc():
    window.Element("source").update("")
    window.Element("Output").update("")
    window.Element("-FILENAME-").update("")


def getFile():
    filePath = values["-FILENAME-"]
    window.Element("source").Update(Buffer.load_file(path=filePath))


#
# Run Program
#
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "process":
        processFunc()
    if event == "reset":
        resetFunc()
    if event == "-FILENAME-":
        getFile()

window.close()
