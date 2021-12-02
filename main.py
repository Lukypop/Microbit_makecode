sound_value = 0
sound_lenght = 0
start = 0 
end = 0
def on_button_pressed_a():
    global sound_value, sound_lenght
    sound_value = randint(1, 8)
    sound_lenght = sound_value*250
    music.play_tone(Note.C, music.beat(sound_lenght))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global sound_lenght
    music.play_tone(Note.C, music.beat(sound_lenght))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_event_touched():
    start = control.millis()
    console.log_value("start", start)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_event_touched)

def on_logo_event_release():
    end = control.millis()
    console.log_value("end", end)
    time = start - end
    if time == sound_lenght:
        
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_event_release)

