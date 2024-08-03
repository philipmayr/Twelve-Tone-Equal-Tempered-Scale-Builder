def build_12_TET_chromatic_scale(base_pitch_frequency):
    starting_pitch_frequency = base_pitch_frequency / pow(2, 5)
    
    chromatic_scale = {
            # Pitch Number (A-1): Frequency
            "": ""
        }
        
    notes = ['A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭']

    half_step_counter = 0
    octave_counter = -1
    
    chromatic_scale.update({str(notes[half_step_counter]) + str(octave_counter): starting_pitch_frequency})
    # print(str(starting_pitch_frequency) + ' - ' + str(notes[half_step_counter]) + str(octave_counter))
    
    half_step_counter = 1
    
    for i in range(99):
        if half_step_counter == 3:
            octave_counter += 1
        if half_step_counter == 12:
            starting_pitch_frequency *= 2
            half_step_counter = 0
        note_frequency = starting_pitch_frequency * pow(2, half_step_counter/12)
        chromatic_scale.update({str(notes[half_step_counter]) + str(octave_counter): note_frequency})
        print(str(notes[half_step_counter]) + str(octave_counter), end='')
        if len(str(notes[half_step_counter])) == 1:
            print("    ", end='')
        print(" - " + str(note_frequency))
        half_step_counter += 1

    return chromatic_scale

# 440 Hz base pitch
twelve_tone_equal_tempered_chromatic_scale = build_12_TET_chromatic_scale(440)
