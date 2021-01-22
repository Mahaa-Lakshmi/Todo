import PySimpleGUI as sg
from last import process
tasks =[]

layout = [
    [sg.Text('ToDo')],
    [sg.InputText('', key='todo_item'),sg.Button('Chat'),  ],
    [sg.Listbox(values=tasks, size=(40, 10), key="items"),sg.Button(button_text='Meaning', key="add_save"),sg.Button('Synonym'), sg.Button('Antonym')],
]

window = sg.Window('ToDo App', layout)
while True:
    event, values = window.Read()
    if event == "add_save":
        tasks.append(process(values['todo_item'],1))
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_save').Update("Meaning")
    elif event == "Synonym":
        tasks.append(process(values['todo_item'], 2))
        window.FindElement('items').Update(values=tasks)

    elif event == "Antonym":
        tasks.append(process(values['todo_item'], 3))
        window.FindElement('items').Update(values=tasks)
    elif event=="Chat" :
        if(values['todo_item']=='hello'):
            tasks.append('hello,happy to see you')
            window.FindElement('items').Update(values=tasks)
        else:
            tasks.append('bye,Meet u soon\nmiss you')
            window.FindElement('items').Update(values=tasks)
    elif event == None:
        break

window.Close()
