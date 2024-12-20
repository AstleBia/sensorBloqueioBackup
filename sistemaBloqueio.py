import subprocess
import serial

def bloquearPc():
    subprocess.run("rundll32.exe user32.dll,LockWorkStation", shell=True)

def distancia(dist):
    if dist > 60:
        print("Longe")
        bloquearPc()
        return 1
    else:
        print("Perto")
        return 0

def iniciar_sistema():
    print('Inicio do codigo')
    while True: #Loop para a conexão com o Arduino
        try:  #Tenta se conectar, se conseguir, o loop se encerra
            arduino = serial.Serial('COM4', 9600)
            print('2')
            print('Arduino conectado')
            break
        except Exception as e: print(e)
            # pass
    print('Depois do while true')
    while True: #Loop principal
        msg = str(arduino.readline()) #Lê os dados em formato de string
        msg = msg[21:-8] #Fatia a string
        msg = float(msg)
        #print("Mensagem: {:.2f}".format(msg)) #Imprime a mensagem
        #msg = float(msg)
        distancia(msg)
        #if distancia(msg) == 1:
            #break.
        #print(msg,"cm.")
        arduino.flush() #Limpa a comunicação
