let logging = false
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    logging = !logging
    if (logging) {
        basic.showIcon(IconNames.Square)
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Nyan), music.PlaybackMode.UntilDone)
    } else {
        basic.clearScreen()
    }
    
})
loops.everyInterval(60000, function on_every_interval() {
    if (logging) {
        datalogger.log(datalogger.createCV("temp", input.temperature()), datalogger.createCV("light", input.lightLevel()))
    }
    
})
