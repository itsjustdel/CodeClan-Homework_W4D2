from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    # our sql statement as a string
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    # values for the placeholders "%s"
    values = [artist.name]
    # run sql returns a list of dictionaries
    results = run_sql(sql, values)
    # grab the id from the dictionary that the db created
    # (from the first element in results), and asign to our artist object
    artist.id = results[0]['id']
    #return the amended artist
    return artist

def select(id):
    # we will return an artist
    artist = None        
    sql = "SELECT * FROM artists WHERE id = %s"    
    values = [id]
    # abstracting out to simplify for the brain box
    results = run_sql(sql, values)
    #result will hold the dictionary we were looking for
    result = results[0]

    # let's use it build an instance of the Artist class
    if result is not None:
        artist = Artist(result['name'], result['id'])
    
    # return the found artist 
    return artist

