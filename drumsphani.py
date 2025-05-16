import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the mixer
pygame.mixer.init()

# Load drum sounds
kick_sound = pygame.mixer.Sound("kick.wav")  # Replace with your kick sound file path
snare_sound = pygame.mixer.Sound("snare.wav")  # Replace with your snare sound file path
hihat_sound = pygame.mixer.Sound("hihat.wav")  # Replace with your hi-hat sound file path

# Set up the display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Drum Machine")

# Function to play drum sounds
def play_sound(sound):
    sound.play()

# Main loop
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Press 'A' for kick
                    play_sound(kick_sound)
                elif event.key == pygame.K_s:  # Press 'S' for snare
                    play_sound(snare_sound)
                elif event.key == pygame.K_d:  # Press 'D' for hi-hat
                    play_sound(hihat_sound)

        # Clear the screen
        screen.fill((255, 255, 255))
        pygame.display.flip()

except KeyboardInterrupt:
    pygame.quit()
    sys.exit()