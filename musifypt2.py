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

    def play(self):
        if not self.is_playing:
            self.is_playing = True
            print(f"Playing podcast: '{self.title}', Episode {self.episode}, hosted by {self.host}. Duration: {self.get_length()} mins.")
        else:
            print(f"{self.title} is already playing.")

# Playlist to manage media items
class Playlist:
    def __init__(self):
        self.media_items = []

    def add_media(self, media):
        self.media_items.append(media)
        print(f"{media.title} added to playlist.")

    def update_media(self, index, new_media):
        if 0 <= index < len(self.media_items):
            self.media_items[index] = new_media
            print("Media item updated.")
        else:
            print("Invalid index. Update failed.")

    def delete_media(self, index):
        if 0 <= index < len(self.media_items):
            removed = self.media_items.pop(index)
            print(f"{removed.title} removed from playlist.")
        else:
            print("Invalid index. Deletion failed.")

    def play_media(self, index):
        if 0 <= index < len(self.media_items):
            self.media_items[index].play()
        else:
            print("Invalid index. Cannot play media.")

    def stop_media(self, index):
        if 0 <= index < len(self.media_items):
            self.media_items[index].stop()
        else:
            print("Invalid index. Cannot stop media.")

    def show_playlist(self):
        if not self.media_items:
            print("The playlist is empty.")
        else:
            print("\n--- Playlist ---")
            for idx, media in enumerate(self.media_items):
                media_type = "Song" if isinstance(media, Song) else "Podcast"
                print(f"{idx}. {media_type}: {media.title}")

# User interaction menu
def main():
    playlist = Playlist()
    while True:
        print("\nMusic Playing System")
        print("1. Add Song")
        print("2. Add Podcast")
        print("3. Update Media")
        print("4. Delete Media")
        print("5. Play Media")
        print("6. Stop Media")
        print("7. Show Playlist")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter song title: ")
            length = float(input("Enter song length (minutes): "))
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            song = Song(title, length, artist, album)
            playlist.add_media(song)
        
        elif choice == "2":
            title = input("Enter podcast title: ")
            length = float(input("Enter podcast length (minutes): "))
            host = input("Enter host: ")
            episode = int(input("Enter episode number: "))
            podcast = Podcast(title, length, host, episode)
            playlist.add_media(podcast)

        elif choice == "3":
            playlist.show_playlist()
            index = int(input("Enter index of media to update: "))
            media_type = input("Is it a Song or a Podcast? ").strip().lower()
            title = input("Enter new title: ")
            length = float(input("Enter new length (minutes): "))

            if media_type == "song":
                artist = input("Enter new artist: ")
                album = input("Enter new album: ")
                new_media = Song(title, length, artist, album)
            elif media_type == "podcast":
                host = input("Enter new host: ")
                episode = int(input("Enter new episode number: "))
                new_media = Podcast(title, length, host, episode)
            else:
                print("Invalid media type.")
                continue
            playlist.update_media(index, new_media)

        elif choice == "4":
            playlist.show_playlist()
            index = int(input("Enter index of media to delete: "))
            playlist.delete_media(index)

        elif choice == "5":
            playlist.show_playlist()
            index = int(input("Enter index of media to play: "))
            playlist.play_media(index)

        elif choice == "6":
            playlist.show_playlist()
            index = int(input("Enter index of media to stop: "))
            playlist.stop_media(index)

        elif choice == "7":
            playlist.show_playlist()

        elif choice == "8":
            print("Exiting Music Playing System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
