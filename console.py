import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# Delete all Albums - need to do before deleting artists because artists have ref's to albums
album_repository.delete_all()
# Delete all Artists
artist_repository.delete_all()

# Create artist and save on db
artist_1 = Artist("Terrance and the Triggers")
artist_repository.save(artist_1)

artist_2 = Artist("Mr Serious and the Clowns")
artist_repository.save(artist_2)

# Create album and save on db
album_1 = Album("Big Boys Run Wild", "Rock", artist_1)
album_repository.save(album_1)

album_2 = Album("A Nice Flan", "Jazz", artist_2)
album_repository.save(album_2)

# Edit artist
# first make a change in our python instance
artist_1.name = "Terrance Goes Solo"
# make the change on the db
artist_repository.update(artist_1)

# Edit album
album_1.title = "Big Boys Run Wild!!!!!"
album_1.genre = "Hard Rock"
# make the change
album_repository.update(album_1)

# All Albums by Artist
albums_by_Terry = album_repository.all_by_artist(artist_1)

# Select artist by id
found_artist_by_id = artist_repository.select(artist_1.id)

# Select album by id
found_album_by_id = album_repository.select(album_1.id)

# Delete an artist by id
album_repository.delete(artist_1.id)

# Find all artists
all_artists = artist_repository.select_all()

# Delete an album by id
album_repository.delete(album_1.id)

# Find all albums 
all_albums = album_repository.select_all()

pdb.set_trace()