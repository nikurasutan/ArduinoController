def drehen(arduinoData): # Sende Signal an den Arduino
    arduinoData.write('1'.encode())
