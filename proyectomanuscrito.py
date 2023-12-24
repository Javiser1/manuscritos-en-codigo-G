import serial
import time
from pynput import keyboard
# Mapa de caracteres a sus equivalentes G-code (esto es un ejemplo básico)
key_to_gcode = {
    'a': 'X10',  # La tecla 'a' podría representar un movimiento en el eje X de 10 unidades
    'b': 'Y10',  # La tecla 'b' podría representar un movimiento en el eje Y de 10 unidades
    # Agrega más mapeos según sea necesario
}

# Lista para almacenar las teclas presionadas
pressed_keys = []

# Función para manejar las pulsaciones de teclas
def on_key_press(key):
    try:
        if hasattr(key, 'char'):
            if key.char == '\r':  # Si se presiona la tecla Enter (o Intro)
                construct_gcode_command()
                return False  # Detiene el listener
            else:
                pressed_keys.append(key.char)
    except AttributeError:
        pass

# Construye el comando G-code a partir de las teclas presionadas
def construct_gcode_command():
    gcode_command = 'G1 ' + ' '.join(key_to_gcode.get(key, '') for key in pressed_keys)
    print(f"Código G-code construido: {gcode_command}")
    # Aquí podrías enviar el comando G-code a UGS a través de la conexión serial
    # Por ejemplo:
    # ser.write((gcode_command + '\n').encode())

# Configura el listener para las pulsaciones de teclas
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()