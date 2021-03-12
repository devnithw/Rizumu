import os
import eel
import pygame

# Start up the application by loading the files
@eel.expose
def StartUp():
    # Create a list to store the names of the mp3 files
    global playlist 
    # Retrieve all the files in the directory
    userfolder = os.path.expanduser('~')
    userfolder = userfolder + "\Music"
    playlist = os.listdir(userfolder)
    global filepath
    filepath = userfolder + "\\"
    # Create a variable to store the state of the player and initialize it to false 
    global playing
    playing = False
    # Create a variable to store the index of the song currently playing (starts at 0)
    global i
    i = 0

    # Remove files which are not mp3 
    for item in playlist:
        if not item.endswith(".mp3"):
            playlist.remove(item)
    
    # Prints the playlist to the terminal
    print(playlist)

    # Initialize the pygame mixer
    pygame.mixer.init()
    
    # Load the first mp3 file, that is playlist[0], to pygame mixer and play it
    pygame.mixer.music.load(str(filepath + playlist[i]))
    pygame.mixer.music.play()
    print("Playing first")
    
    # Set playing variable to true
    playing = True


# Implements the play/pause button activity
@eel.expose
def PlayPause():
    global playing
    if playing == True:
        print("Pausing")
        playing = False
        pygame.mixer.music.pause()
    else:
        print("Playing")
        pygame.mixer.music.unpause()
        playing = True

# Implements the next button activity and plays the next song when current song finishes
@eel.expose
def nextTrack():
    global i
    i += 1
    pygame.mixer.music.load(str(filepath + playlist[i]))
    pygame.mixer.music.play()
    print("Playing next")

# Implements the previous button activity
@eel.expose
def previousTrack():
    global i
    if i > 0:
        i = i - 1
        pygame.mixer.music.load(str(filepath + playlist[i]))
        pygame.mixer.music.play()
        print("Playing previous")





# if __name__ == "__main__":

eel.init('web')
# Calls the start functions
StartUp()
# Renders the window
eel.start('index.html', block=False)

# Loop after loading the window
while True:
    # Check if music is not playing AND whether it wasn't forced by the user, If both of these conditions are true then the current song must be over
    if not pygame.mixer.music.get_busy() and playing:
        print("true")
        nextTrack()
    eel.sleep(2)

