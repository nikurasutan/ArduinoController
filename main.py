from flask import Flask, render_template, url_for, flash  # Imports für Flask
import serial  # Serielle Schnittstelle
from arduinoFunctions import *  # eigenes Skript
from forms import * # eigenes Skript

app = Flask(__name__) # Name der Flask Anwendung wird auf den Dateinamen ohne Endung gesetzt

app.config['SECRET_KEY'] = '85e27c84f9ce488e85a383771f2a1c74' # Secret Key um gegen Hacks abzusichern


@app.route("/", methods=['GET', 'POST']) # Homepage Server Route
def home(): # Diese Funktion wird ausgeführt wenn diese Route angesteuert wird
    global arduinoData, allright # Globale Variabeln festlegen
    form = AuswalFormular() # Das Formular auswählen, das angezeigt werden soll
    if form.validate_on_submit(): # wenn das Formular bei einer Post-Anfrage korrekt ist tu das
        if form.aktion.data == 'verbinden': # Wenn Verbinden ausgewählt
            arduinoData = serial.Serial(form.serialDevice.data, 9600) # Setze die Eckdaten der Seriellen Verbindung fest
            allright = True # Da Funktion valide
        elif form.aktion.data != 'verbinden' and arduinoData is None: # Wenn etwas anderes als verbinden ausgewählt wurde und die Eckdaten der Verbindung noch nicht festgelegt sind.
            allright = False # Nicht valide Funktion
        elif form.aktion.data == 'dreh' and arduinoData is not None: # Wenn dreh ausgewählt und Eckdaten der Verbindung sind eingetragen
            drehen(arduinoData) # sende drehen Signal an den Arduino
            allright = True # valide Funktion

        if allright:
            flash(f'Es wurde das Signal {form.aktion.data} an den Arduino geschickt!', 'success') # Wenn Funktion valide
        else: # wenn nicht valide
            flash(
                'Den Arduino ist noch nicht verbunden, bitte erst mittels der Funktion Verbinden den Arduino mit dem Server verbinden.', 'warning') # sende eine Warnung

    return render_template('home.html', form=form) # Render das Template Home


@app.route("/about") # /about Server Route
def about(): # Diese Funktion wird ausgeführt wenn diese Route angesteuert wird
    return render_template('about.html') # Render das About Template


if __name__ == '__main__': # Main-Methode
    app.run(debug=True) 
