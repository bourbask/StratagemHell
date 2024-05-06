import pygame
import os
from dotenv import load_dotenv
import threading

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
MUSIC_BASEPATH = os.getenv("MUSIC_BASEPATH")

def play_music_in_loop():
    # Initialize Pygame
    pygame.init()

    # Set up Pygame mixer
    pygame.mixer.init()

    # Get the list of WAV files in the current directory
    wav_files = [file for file in os.listdir(MUSIC_BASEPATH) if file.endswith(".wav")]

    # Load each WAV file into Pygame mixer and play them in sequence
    sounds = []
    for wav_file in wav_files:
        sound = pygame.mixer.Sound(MUSIC_BASEPATH + wav_file)
        sounds.append(sound)

    # Play sounds in loop
    def play_music():
        current_index = 0
        while True:
            sounds[current_index].play()
            while pygame.mixer.get_busy():
                pygame.time.Clock().tick(30)  # Control the frame rate
            current_index = (current_index + 1) % len(sounds)  # Move to the next sound file

    # Start music playing thread
    music_thread = threading.Thread(target=play_music)
    music_thread.start()