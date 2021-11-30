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

def select_all():
    # we will return a list of artists
    artists = []
    sql = "SELECT * FROM artists"
    # run_sql returns a list of dictionaries
    results = run_sql(sql)

    # for each dictionary returned in the results list, build an Artist,
    # and add to the list we will return
    # Note we do not need to check for None because if there is nothing in the list
    # it will just skip over
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)

    return artists

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

def delete_all():
    #run the sql, we don't need a variable to store any results, it is just a simple action
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    # value for placeholder %s - must be in a list even if only one value
    values = [id]
    # run the sql, we don't need a variable to store any results, it is just a simple action
    # but we do need to pass the "id" held in "values"
    run_sql(sql, values)

def update(artist):
    # update artist row
    # note - if only one change being made, do not use () after SET
    sql = "UPDATE artists SET name = (%s) WHERE id = %s"
    # replace placeholders with these values
    values = [artist.name, artist.id]
    # send to db
    run_sql(sql, values)


