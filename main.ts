let velocidad = 0
let Ultrasonico = 0
let pausa = 0
input.onButtonPressed(Button.A, function () {
    velocidad = 0
})
input.onButtonPressed(Button.B, function () {
    velocidad = 200
})
basic.forever(function () {
    Ultrasonico = sonar.ping(
    DigitalPin.P1,
    DigitalPin.P2,
    PingUnit.Centimeters
    )
    if (Ultrasonico > 200 || Ultrasonico < 2) {
        Ultrasonico = 150
    } else {
        pausa = Math.map(Ultrasonico, 0, 200, 0, 2000)
        led.plotBarGraph(
        Math.map(Ultrasonico, 0, 150, 150, 0),
        150
        )
        robotbit.MotorRun(robotbit.Motors.M1B, velocidad)
        music.setVolume(255)
        music.ringTone(880)
        basic.pause(50)
        robotbit.MotorRun(robotbit.Motors.M1B, 0)
        music.stopAllSounds()
        basic.pause(pausa)
    }
})
