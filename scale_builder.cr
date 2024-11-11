def build_twelve_tone_equal_tempered_chromatic_scale(base_pitch_frequency)
    starting_pitch_frequency = base_pitch_frequency / (1 << 5)

    # Key-Value Dictionary of Tone Names with Octave Numbers as Keys for Frequencies in Hertz as Values
    chromatic_scale = {"" => 0.0}
  
    notes = ["A", "A♯/B♭", "B", "C", "C♯/D♭", "D", "D♯/E♭", "E", "F", "F♯/G♭", "G", "G♯/A♭"]
 
    half_step_counter = 0
    octave_counter = -1
    
    chromatic_scale[notes[half_step_counter] + octave_counter.to_s] = starting_pitch_frequency
  
    half_step_counter += 1
  
    123.times do
        if half_step_counter == 3
            octave_counter += 1
        elsif half_step_counter == 12
            starting_pitch_frequency *= 2
            half_step_counter = 0
        end

        note = notes[half_step_counter]
  
        note_frequency = starting_pitch_frequency * (2 ** (half_step_counter / 12))
  
        chromatic_scale[note + octave_counter.to_s] = note_frequency
  
        puts note + octave_counter.to_s + " - " + note_frequency.to_s
        
        half_step_counter += 1
    end
 
    return chromatic_scale
end

# 440 Hz (Hertz) Base Pitch Frequency
twelve_tone_equal_tempered_chromatic_scale = build_twelve_tone_equal_tempered_chromatic_scale(440)
