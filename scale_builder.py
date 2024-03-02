def build_chromatic_scale(base_pitch_frequency, temperament):
    starting_pitch_frequency = base_pitch_frequency / pow(2, 5)
    print(starting_pitch_frequency)
    
    chromatic_scale = {
            # Pitch Number (A-1): Frequency
            "": ""
        }
        
    notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        
    chromatic_scale.update({"A-1": starting_pitch_frequency})
    chromatic_scale.update({"A♯-1": starting_pitch_frequency * pow(2, 1/12)})
    
    half_step_counter = 1
    
    for i in range(100):
        if half_step_counter == 13:
            starting_pitch_frequency *= 2
            half_step_counter = 1
        note_frequency = starting_pitch_frequency * pow(2, half_step_counter/12)
        print(note_frequency)
        chromatic_scale.update({"": note_frequency})
        half_step_counter += 1
    
build_chromatic_scale(440, 0)
