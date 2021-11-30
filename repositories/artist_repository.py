from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    # run sql returns a list of dictionaries
    results = run_sql(sql, values)
    # grab the id from the dictionary that the db created
    #  from the first element in results, and asign to our artist object
    artist.id = results[0]['id']
    #return the amended artist
    return artist