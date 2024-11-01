from abc import ABC, abstractmethod

# Abstract Base Class for Media
class Media(ABC):
    def __init__(self, title, length):
        self.title = title
        self.__length = length  # Private attribute for encapsulation
        self.is_playing = False

    def get_length(self):
        return self.__length

    @abstractmethod
    def play(self):
        pass

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            print(f"{self.title} has been stopped.")
        else:
            print(f"{self.title} is not playing.")

# Song subclass with artist and album attributes
class Song(Media):
    def __init__(self, title, length, artist, album):
        super().__init__(title, length)
        self.artist = artist
        self.album = album

    # Polymorphic play method for Song
    def play(self):
        if not self.is_playing:
            self.is_playing = True
            print(f"Playing song: '{self.title}' by {self.artist} from album '{self.album}'. Duration: {self.get_length()} mins.")
        else:
            print(f"{self.title} is already playing.")

# Podcast subclass with host and episode attributes
class Podcast(Media):
    def __init__(self, title, length, host, episode):
        super().__init__(title, length)
        self.host = host
        self.episode = episode

    # Polymorphic play method for Podcast
    def play(self):
        if not self.is_playing:
            self.is_playing = True
            print(f"Playing podcast: '{self.title}', Episode {self.episode}, hosted by {self.host}. Duration: {self.get_length()} mins.")
        else:
            print(f"{self.title} is already playing.")

# System interaction to create media and perform actions
def main():
    print("Welcome to MUSIFY")
    
    # Create media items
    song = Song("That's so true", 3.5, "Gracie Abrams", "The Secret of Us")
    podcast = Podcast("Rotten Mango Podcast", 60, "Stephanie Soo", 1)
    
    # Demonstrate functionality
    print("\n--- Media Actions ---")
    song.play()
    song.stop()

    podcast.play()
    podcast.stop()

# Display options to user
    print("\n--- Select Media to Play ---")
    print("1. Play Song")
    print("2. Play Podcast")
    
    try:
        choice = int(input("Enter your choice (1 or 2): ").strip())
    except ValueError:
        print("Invalid input! Please enter a number (1 or 2).")
        return  # Exit if input is invalid

    if choice == "1":
        song.play()
    elif choice == "2":
        podcast.play()
    else:
        print("Invalid choice.")

    # Option to stop the media
    stop_choice = input("\nWould you like to stop the media? (yes or no): ").lower()
    if stop_choice == "yes":
        if choice == "1":
            song.stop()
        elif choice == "2":
            podcast.stop()

if __name__ == "__main__":
    main()
