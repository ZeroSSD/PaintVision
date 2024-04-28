import soundcard as sc
microphones = sc.all_microphones()

# Print the names of all microphones
for mic in microphones:
    print(mic.name)