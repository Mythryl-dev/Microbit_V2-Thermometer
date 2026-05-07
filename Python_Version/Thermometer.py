def on_button_pressed_a():
    global pause2
    pause2 = 1
    basic.clear_screen()
    basic.show_string("" + str(input.temperature()))
    pause2 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global pause2
    music.set_built_in_speaker_enabled(True)
    pause2 = 0
    music.set_volume(75)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global pause2
    music.set_built_in_speaker_enabled(False)
    pause2 = 0
    music.set_volume(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

repeat = 0
repeat_2 = 0
pause2 = 0
music.set_built_in_speaker_enabled(True)
pause2 = 0
music.set_volume(75)

def on_forever():
    if pause2 == 0:
        if input.temperature() == 50:
            basic.show_icon(IconNames.SKULL)
        else:
            led.plot_bar_graph(input.temperature(), 50)
basic.forever(on_forever)

def on_forever2():
    if input.temperature() == 50:
        basic.show_icon(IconNames.SKULL)
        for index in range(4):
            music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
                    5000,
                    0,
                    255,
                    0,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                SoundExpressionPlayMode.UNTIL_DONE)
basic.forever(on_forever2)

def on_forever3():
    global repeat_2
    if input.temperature() >= 30 and input.temperature() <= 40:
        for index2 in range(repeat_2):
            music.play_melody("F D E F A D F E ", 120)
    if input.temperature() >= 30 and input.temperature() <= 40:
        repeat_2 += 1
    else:
        repeat_2 = 0
basic.forever(on_forever3)

def on_forever4():
    if input.temperature() >= 30 and input.temperature() <= 40:
        pins.analog_write_pin(AnalogPin.P1, 1023)
    else:
        pins.analog_write_pin(AnalogPin.P1, 0)
basic.forever(on_forever4)

def on_forever5():
    global repeat
    if input.temperature() >= 40 and input.temperature() <= 49:
        music.set_volume(255)
        for index3 in range(repeat):
            music.play_melody("C5 B C5 B C5 B C5 B ", 500)
    if input.temperature() >= 40 and input.temperature() <= 49:
        repeat += 1
    else:
        repeat = 0
basic.forever(on_forever5)
