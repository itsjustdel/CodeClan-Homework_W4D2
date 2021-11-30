from db.run_sql import run_sql

from models.album import Album

# CREATE
def save(album):
    sql = "INSERT INTO album (title, genre, artist) VALUES (%s, %s, %s) RETURNING *" 
    values = [album.title, album.genre, album.artist]
    results = run_sql[sql, values]
    # save the id the database created for us in our album object
    album.id = results[0]['id']
    # return the amended album
    return album




