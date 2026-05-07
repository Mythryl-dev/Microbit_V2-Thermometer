input.onButtonPressed(Button.A, function () {
    pause2 = 1
    basic.clearScreen()
    basic.showString("" + input.temperature())
    pause2 = 0
})
input.onButtonPressed(Button.AB, function () {
    music.setBuiltInSpeakerEnabled(true)
    pause2 = 0
    music.setVolume(75)
})
input.onButtonPressed(Button.B, function () {
    music.setBuiltInSpeakerEnabled(false)
    pause2 = 0
    music.setVolume(0)
})
let repeat = 0
let repeat_2 = 0
let pause2 = 0
music.setBuiltInSpeakerEnabled(true)
pause2 = 0
music.setVolume(75)
basic.forever(function () {
    if (pause2 == 0) {
        if (input.temperature() == 50) {
            basic.showIcon(IconNames.Skull)
        } else {
            led.plotBarGraph(
                input.temperature(),
                             50
            )
        }
    }
})
basic.forever(function () {
    if (input.temperature() == 50) {
        basic.showIcon(IconNames.Skull)
        for (let index = 0; index < 4; index++) {
            music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
        }
    }
})
basic.forever(function () {
    if (input.temperature() >= 30 && input.temperature() <= 40) {
        for (let index = 0; index < repeat_2; index++) {
            music.playMelody("F D E F A D F E ", 120)
        }
    }
    if (input.temperature() >= 30 && input.temperature() <= 40) {
        repeat_2 += 1
    } else {
        repeat_2 = 0
    }
})
basic.forever(function () {
    if (input.temperature() >= 30 && input.temperature() <= 40) {
        pins.analogWritePin(AnalogPin.P1, 1023)
    } else {
        pins.analogWritePin(AnalogPin.P1, 0)
    }
})
basic.forever(function () {
    if (input.temperature() >= 40 && input.temperature() <= 49) {
        music.setVolume(255)
        for (let index = 0; index < repeat; index++) {
            music.playMelody("C5 B C5 B C5 B C5 B ", 500)
        }
    }
    if (input.temperature() >= 40 && input.temperature() <= 49) {
        repeat += 1
    } else {
        repeat = 0
    }
})
