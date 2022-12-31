class Music():
    
    def __init__(self,performer, song, album, year):
        self.performer=performer
        self.song=song
        self.album=album
        self.year=year

    def __str__(self):
        return f'Performer:{self.performer} \nSong: {self.song}\nAlbum: {self.album} \nYear: {self.year}'

m=Music('Ed sheeran', 'heartgfsa', 'divide',2017)
print(m)