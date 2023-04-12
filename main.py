velocidad = 0
Ultrasonico = 0
pausa = 0

def on_button_pressed_a():
    global velocidad
    velocidad = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global velocidad
    velocidad = 200
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global Ultrasonico, pausa
    Ultrasonico = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    if Ultrasonico > 200 or Ultrasonico < 2:
        Ultrasonico = 150
    else:
        pausa = Math.map(Ultrasonico, 0, 200, 0, 2000)
        led.plot_bar_graph(Math.map(Ultrasonico, 0, 150, 150, 0), 150)
        robotbit.motor_run(robotbit.Motors.M1B, velocidad)
        music.set_volume(255)
        music.ring_tone(880)
        basic.pause(50)
        robotbit.motor_run(robotbit.Motors.M1B, 0)
        music.stop_all_sounds()
        basic.pause(pausa)
basic.forever(on_forever)
