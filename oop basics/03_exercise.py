class Playlist:

    def __init__(self, title):
        # TODO: Store title and create a new empty songs list on this instance.
        self.title = title
        self.songs  = []

    def add_song(self, song):
        # TODO: Add song to this playlist's own songs list.
        self.songs.append(song)

    def summary(self):
        # TODO: Return the playlist title and its songs.
        songs = ", ".join(self.songs)
        return f"{self.title}: {songs}"


road_trip = Playlist("Road Trip")
road_trip.add_song("Go West")
road_trip.add_song("Open Road")

focus = Playlist("Focus")
focus.add_song("Deep Work")

print(road_trip.summary())
print(focus.summary())
print(f"Different song lists: {road_trip.songs is not focus.songs}")
