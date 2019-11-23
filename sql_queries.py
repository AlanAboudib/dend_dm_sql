# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays CASCADE;"
user_table_drop = "DROP TABLE IF EXISTS users CASCADE;"
song_table_drop = "DROP TABLE IF EXISTS songs CASCADE;"
artist_table_drop = "DROP TABLE IF EXISTS artists CASCADE;"
time_table_drop = "DROP TABLE IF EXISTS time CASCADE;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays(
    songplay_id SERIAL PRIMARY KEY,
    start_time BIGINT REFERENCES time(start_time),
    user_id TEXT NOT NULL REFERENCES users(user_id),
    level TEXT,
    song_id TEXT  REFERENCES songs(song_id),
    artist_id TEXT  REFERENCES users(user_id),
    session_id TEXT,
    location TEXT,
    user_agent TEXT
);
""")

user_table_create = ("""
CREATE TABLE users(
    user_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender CHAR(1),
    level TEXT
);
""")

song_table_create = ("""
CREATE TABLE songs(
    song_id TEXT PRIMARY KEY,
    title TEXT,
    artist_id TEXT,
    year integer,
    duration NUMERIC
);
""")

artist_table_create = ("""
CREATE TABLE artists(
    artist_id TEXT PRIMARY KEY,
    name TEXT,
    location TEXT,
    lattitude NUMERIC,
    longitude NUMERIC 
);
""")

time_table_create = ("""
CREATE TABLE time(
    start_time BIGINT PRIMARY KEY,
    hour integer,
    day integer,
    week integer,
    month integer,
    year integer,
    weekday integer
);
""")


# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays ( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES ( %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, lattitude, longitude)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id 
FROM songs s JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title = %s 
AND a.name = %s 
AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [ user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
