logging = False

def on_button_pressed_a():
    global logging
    logging = not (logging)
    if logging:
        basic.show_icon(IconNames.SQUARE)
        music._play_default_background(music.built_in_playable_melody(Melodies.NYAN),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_every_interval():
    if logging:
        datalogger.log(datalogger.create_cv("temp", input.temperature()),
            datalogger.create_cv("light", input.light_level()))
loops.every_interval(60000, on_every_interval)
