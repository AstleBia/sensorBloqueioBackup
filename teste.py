import PySimpleGUI as sg

logo = './cesar.ico'

# Function to create a new window based on the current layout
def selecionarJanela(layout_name):
    if layout_name == 'pagInicial':
        layout = [
            [sg.Text('SENSOR DE BLOQUEIO', text_color='white', justification='center', size=(300, 1), background_color='#ff6600', font=('Helvetica', 24))],
            [sg.Text('Bem Vindo', justification='center', size=(300, 1), background_color='#ff6600', font=('Helvetica', 24))],
            [sg.Column([[sg.Button('Ativar'), sg.Button('Sair')]], justification='center', background_color='#ff6600')]
        ]
        return sg.Window('Sensor Bloqueio', layout, size=(600, 300), background_color='#ff6600', icon=logo, finalize=True)

    elif layout_name == 'pagSistema':
        layout = [
            [sg.Text('SENSOR RODANDO', text_color='white', justification='center', size=(300, 1), background_color='Green', font=('Helvetica', 24))],
            [sg.Text('Computador Protegido', justification='center', size=(300, 1), background_color='Green', font=('Helvetica', 18))],
            [sg.Column([[sg.Button('Parar')]], justification='center', background_color='Green')]
        ]
        return sg.Window('Sensor Bloqueio', layout, size=(600, 300), background_color='Green', icon=logo, finalize=True)

# Start with the initial window
layoutAtual = 'pagInicial'
window = selecionarJanela(layoutAtual)

while True:
    event, values = window.read()

    # Handle window close or 'Sair' button press
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    # When "Ativar" is pressed, switch to the running system layout
    elif event == 'Ativar' and layoutAtual == 'pagInicial':
        print('Ativar clicked!')
        window.close()  # Close the current window
        layoutAtual = 'pagSistema'  # Update the current layout
        window = selecionarJanela(layoutAtual)  # Create a new window with the updated layout

    # When "Parar" is pressed, switch back to the initial layout
    elif event == 'Parar' and layoutAtual == 'pagSistema':
        print("Parando system!")
        window.close()  # Close the current window
        layoutAtual = 'pagInicial'  # Update the current layout
        window = selecionarJanela(layoutAtual)  # Create a new window with the updated layout

window.close()

