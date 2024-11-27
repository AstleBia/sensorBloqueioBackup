import PySimpleGUI as sg
from sensor import main, read_arduino
import time

logo = './cesar.ico'

def selecionarJanela(nomeLayout):
    if nomeLayout == 'pagInicial':
        layout = [[sg.Text('SENSOR DE BLOQUEIO', text_color='white', justification='center', size=(300,1), background_color='#ff6600', font=('Helvetica', 24))],
          [sg.Text('Bem Vindo', justification='center',size=(300,1),background_color='#ff6600',font=('Helvetica', 24))],
          [sg.Column([[sg.Button('Ativar'), sg.Button('Sair')]], justification='center',background_color='#ff6600')]]
        return sg.Window('Sensor Bloqueio', layout, size=(600, 300), background_color='#ff6600', icon=logo, finalize=True)
    elif nomeLayout == 'pagSistema':
        layout = [[sg.Text('SENSOR RODANDO', text_color='white', justification='center', size=(300,1), background_color='Green', font=('Helvetica', 24))],
          [sg.Text('Computador Protegido', justification='center',size=(300,1),background_color='Green',font=('Helvetica', 18))],
          [sg.Column([[sg.Button('Parar')]], justification='center',background_color='Green')]]
        return sg.Window('Sensor Bloqueio', layout, size=(600, 300), background_color='Green', icon=logo, finalize=True)

layoutAtual = 'pagInicial'
window = selecionarJanela(layoutAtual)
sistemaInicializado = False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif event == 'Ativar' and layoutAtual == 'pagInicial':
        print('Ok!')
        window.close()
        layoutAtual = 'pagSistema'
        window = selecionarJanela(layoutAtual)
        arduino = main()
        if arduino:
            while True:
                if not read_arduino(arduino):
                    break

    if event == 'Parar' and layoutAtual == 'pagSistema':
        print("Parando")
        if arduino:
            arduino.close()
        window.close()
        layoutAtual = 'pagInicial'
        window = selecionarJanela(layoutAtual)

window.close()