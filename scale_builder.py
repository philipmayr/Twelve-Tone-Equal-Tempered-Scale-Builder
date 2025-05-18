def build_twelve_tone_equal_tempered_chromatic_scale(base_pitch_frequency):
    starting_pitch_frequency = base_pitch_frequency / pow(2, 5)
    
    # Key-Value Pair Dictionary
    chromatic_scale = {
            # Tone Name and Octave Number (A-4) - Frequency in Hertz (440)
            '': ''
        }
        
    notes = ['A', "A♯/B♭", 'B', 'C', "C♯/D♭", 'D', "D♯/E♭", 'E', 'F', "F♯/G♭", 'G', "G♯/A♭"]
    
    half_step_counter = 0
    octave_counter = -1
    
    chromatic_scale.update({notes[half_step_counter] + str(octave_counter): starting_pitch_frequency})
    # print(notes[half_step_counter] + str(octave_counter) + "     - " + str(starting_pitch_frequency))
    
    half_step_counter = 1
    
    for i in range(123):
        if half_step_counter == 3:
            octave_counter += 1
        elif half_step_counter == 12:
            starting_pitch_frequency *= 2
            half_step_counter = 0
            
        note_frequency = starting_pitch_frequency * pow(2, half_step_counter / 12)
        
        note = notes[half_step_counter]
        
        chromatic_scale.update({note + str(octave_counter): note_frequency})
        
        print(note + str(octave_counter), end='')
        if len(note) == 1: 
            print("    ", end='')
        print(" - " + str(note_frequency))
        
        half_step_counter += 1
        
    return chromatic_scale

# 440 Hz (Hertz) Base Pitch Frequency
twelve_tone_equal_tempered_chromatic_scale = build_twelve_tone_equal_tempered_chromatic_scale(440)
