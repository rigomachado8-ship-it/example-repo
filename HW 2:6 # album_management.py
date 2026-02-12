# album_management.py

class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_song = number_of_songs
    
    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_song})"
    
# Create albums1 list and add five Album objects 
albums1 = [
    Album("Future Nostalgia" , "Dua Lipa", 11),
    Album("What's Your Pleasure?" , "Jessie Ware", 12),
    Album("Renaissance" , "Beyoncé", 16),
    Album("Something To Give Each Other" , "Troye Sivan", 10),
    Album("MAYHEM" , "Lady Gaga", 12)
]

print("albums1:")
for album in albums1:
    print(album)

# Sort albums1 by number of songs
albums1.sort(key=lambda album: album.number_of_song)

print("\nalbums1 sorted by number of songs:")
for album in albums1:
    print(album)

# Swap elements at index 1 with elements at index 3
albums1[1], albums1[3] = albums1[3], albums1[1]

print("\nalbums1 after swapping index 1 and index 3:")
for album in albums1:
    print(album)

#Create albums2 list 
albums2 = []

# Adding five albums object to album2
albums2.extend([
    Album("Louder, Please" , "Rose Gray" , 12),
    Album("Fancy That" , "PinkPantheress", 9),
    Album("The Rise and Fall of a Midwest Princess" , "Chappell Roan" , 14),
    Album("BRAT" , "Charli XCX", 15),
    Album("Midnight Sun" , "Zara Larsson" , 10)
])

print("\nalbums2:")
for album in albums2:
    print(album)

# Copy all albums from albums1 into albums2
albums2.extend(albums1)

#Adding these two albums
albums2.append(Album("Cowboy Carter" , "Beyonce", 27))
albums2.append(Album("Born This Way" , "Lady Gaga", 17))

# Sort albums2 alphabetically by album name
albums2.sort(key=lambda album: album.album_name)

print("\nalbums2 sorted alphabetically by album name:")
for album in albums2:
    print(album)

# Search for "Fancy That"
for index, album in enumerate(albums2):
    if album.album_name == "Fancy That":
        print(f"\nFound 'Fancy That' at index {index}: {album}")
        break

