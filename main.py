import pynput.keyboard as keyboard
import pyautogui

# Configura la cantidad de píxeles a mover el cursor
PIXEL_STEP = 30

# Variable para saber si control esta presionado
ctrl_pressed = False

# Diccionario para mapear las teclas de flecha con las funciones de movimiento
MOVEMENT_KEYS = {
    keyboard.Key.up: (0, -PIXEL_STEP),    # Mover arriba
    keyboard.Key.down: (0, PIXEL_STEP),   # Mover abajo
    keyboard.Key.left: (-PIXEL_STEP, 0),  # Mover izquierda
    keyboard.Key.right: (PIXEL_STEP, 0),  # Mover derecha
}

# Función para manejar eventos de teclas presionadas
def on_press(key):
    global ctrl_pressed

    try:
        # Detecta si se presiona la tecla "Ctrl"
        if key in [keyboard.Key.ctrl_l]:
            ctrl_pressed = True

        # Si está presionada y una tecla de dirección es presionada, mueve el cursor
        if ctrl_pressed and key in MOVEMENT_KEYS:
            move_x, move_y = MOVEMENT_KEYS[key]
            pyautogui.move(move_x, move_y)

    except Exception as e:
        print(f"Error al manejar la tecla presionada: {e}")

# Función para manejar eventos de teclas soltadas
def on_release(key):
    global ctrl_pressed

    try:
        # Detecta si se suelta la tecla "Alt"
        if key in [keyboard.Key.ctrl_l]:
            ctrl_pressed = False

        # Detiene el listener si se presiona "esc"
        if key == keyboard.Key.esc:
            return False

    except Exception as e:
        print(f"Error al manejar la tecla soltada: {e}")

# Configurar el listener de teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
