# Project: Data Modeling with Postgres
## The Data Analyst NanoDegree
--------------

### 1- Summary of the Project

A company called Sparkify, in the music streaming industry, needs to build some analytics out of the data it is collecting from uses. Such data take the form of song details, user details, artist details and logs of when users listen to some songs.

Such analytics would be useful to better understand users behavious and thus be able to provide a better service.

The problem is that such data is stored as .json files that are not easy to manipulate directly to create analytics and visualisations.

The purpose of this project is to help the company organize their data in a relational database (Postgres in our case). Such a database is easier to query to create customizable, fast analytics and eventually visualisations.

The ETL process, is the process that moves data from the .json files to the Postgres database, will be facilitated with the Pandas library.

This project is a really simple usecase meant to familiarize the students with the concept of relational databases and ETLing.

### 2- Project folder contents

The submitted folder contains a few files and scripts that implements the process of creating the database and the process of populating the database (ETL). Here is an overview of these files:

- **sql_queries.py:** All of the SQL queries for creating the database schema are included in this file.
- **create_tables.py:** The code for connecting to the database and running the queries in `sql_queries.py` that create the schema is included here. There script should be run first.
- **etl.py:** The code for loading .json files into Pandas dataframe, and then using those dataframes to populate the Postgres database is implemented here. Or in other words: the ETL process is implemented here. This is the second script to run after `create_tables.py`.
- **test.ipynb:** This is a provided jupyter notebook that contains some simple sanity checks for connecting to the database and performing some queries to view the contents of table after `etl.py` is run.

### 3. The database schema

Since the SQL schema is meant to perform analysis, it is organized as a star schema which is a more adapted architecture to perform analytics since it minimizes the number of required joins in the worst case.

the fact table at the center of the star schema is the `songplay` table where song listening events are stored. This table has four reference keys to the four dimension tables: 'start_time' referencing the `time` table, 'song_id' referening the `song` table, 'artist_id' referencing the `artist` table and finally the 'user_id' referencing the `user` table.


### 4. Running the scripts:

After you setup a working Postgres database server on your machine, you can easily run the project by running:

```
$ python create_tables.py && python etl.py
```

### 5. A final word

This project was a great occasion for me to appreciate why ETL is used in practice. Although this is a toy usecase, it is obvious that this project can be extrapolated to more sophisticated tools using data warehouse or datalakes and we will see in future chapters.
