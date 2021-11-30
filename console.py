import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("Terrance and the Triggers")
artist_repository.save(artist_1)

album_1 = Album("Big Boys Run Wild", "Rock", artist_1)
album_repository.save(album_1)

pdb.set_trace()