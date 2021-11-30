from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository

# CREATE
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *" 
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    # save the id the database created for us in our album object
    album.id = results[0]['id']
    # return the amended album
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    # we don't need to pass any values since we are just retreiving everything
    results = run_sql(sql)

    # grab our queried result and build Album objects with the dictionary we received back    
    for row in results:
        # we need to pass in an artist object to create an album
        # we locate our artist by using the id of the artist
        artist = artist_repository.select(row['artist_id'])
        # now create our instance
        album = Album(row['title'], row['genre'], artist)
        #and add it the list we will return
        albums.append(album)

    return albums

def select(id):
    # we will return an album
    album = None        
    sql = "SELECT * FROM albums WHERE id = %s"    
    values = [id]
    # abstracting out to simplify for the brain box
    results = run_sql(sql, values)
    #result will hold the dictionary we were looking for
    result = results[0]

    # let's use it build an instance of the Album class
    if result is not None:
        # find the artist with the method we made for finding with artist_id
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'],result['genre'],artist,result['id'])
    
    # return the found album
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    # value for placeholder %s - must be in a list even if only one value
    values = [id]
    # run the sql, we don't need a variable to store any results, it is just a simple action
    # but we do need to pass the "id" held in "values"
    run_sql(sql, values)

def update(album):
    # we will change title, genre and artist (all properties except its id)
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    # replace placeholders - note the row in the album table only wants to know the artist's id, it can't store an artist object as a whole
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)

def all_by_artist(artist):
    # we want to access the album table and match against the passed artist's id
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        #build an instance of the album class from the found dictionaries
        # note we can pass in the passed artist, no need to search anywhere for it
        album = Album(row['title'], row['genre'], artist, row['id'])
        # add to the list we will return
        albums.append(album)

    # return the albums we found
    return albums



