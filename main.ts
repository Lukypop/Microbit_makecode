let sound_value = 0
let sound_lenght = 0
let start = 0
let end = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    sound_value = randint(1, 8)
    sound_lenght = sound_value * 250
    music.playTone(Note.C, music.beat(sound_lenght))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    music.playTone(Note.C, music.beat(sound_lenght))
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_event_touched() {
    let start = control.millis()
    console.logValue("start", start)
})
input.onLogoEvent(TouchButtonEvent.Released, function on_logo_event_release() {
    let end = control.millis()
    console.logValue("end", end)
    let time = start - end
    if (time == sound_lenght) {
        led
    }
    
})
