from db.run_sql import run_sql

from models.album import Album

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

    sql = "SELECT * FROM users"
    # we don't need to pass any values since we are just retreiving everything
    results = run_sql(sql)

    # grab our queried result and build Album objects with the dictionary we received back
    # for row in results:
    #     album = Album(row['title'], row['genre'], )


