def build_chromatic_scale(base_pitch_frequency, temperament):
    starting_pitch_frequency = base_pitch_frequency / pow(2, 5)
    print(starting_pitch_frequency)
    
    chromatic_scale = {
            # Pitch Number (A-1): Frequency
            "": ""
        }
        
    notes = ['A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭']
        
    chromatic_scale.update({"A-1": starting_pitch_frequency})
    chromatic_scale.update({"A♯-1": starting_pitch_frequency * pow(2, 1/12)})
    
    half_step_counter = 1
    octave_counter = -1
    
    for i in range(100):
        if half_step_counter == 5:
            octave_counter += 1
        if half_step_counter == 12:
            starting_pitch_frequency *= 2
            half_step_counter = 0
        note_frequency = starting_pitch_frequency * pow(2, half_step_counter/12)
        print(str(note_frequency) + ' - ' + str(notes[half_step_counter]))
        chromatic_scale.update({"": note_frequency})
        half_step_counter += 1
    
build_chromatic_scale(440, 0)
