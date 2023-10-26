class Song:
    
    count = 0
    artists = []
    genres = ['Rap', 'Rock', 'Pop']
    artist_count = {}
    genre_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.add_artist(self.artist)
        Song.update_artist_songs(self.artist)
        Song.update_genre_songs(self.genre)
    
    @classmethod
    def add_artist(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def update_artist_songs(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] = cls.artist_count[artist] + 1
        else:
            cls.artist_count[artist] = 1
    
    @classmethod
    def update_genre_songs(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] = cls.genre_count[genre] + 1
        else:
            cls.genre_count[genre] = 1
        

