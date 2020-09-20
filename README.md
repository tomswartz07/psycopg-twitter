# Tweet Importer

Import tweets into a PostgreSQL database for archival purposes.

Keeping the messages safe for review if the original tweets have been
deleted, removed, or if the account was made private.


# Using

First, you'll need a Twitter API key.

Log in and [get one](https://developer.twitter.com/en).

Enter the relevant info into the `python-fav-tweets.py` script.

Run the python script to get a CSV output, then run the SQL to import
the information in to the DB.

Creating the schema in the PG DB is an exercise left for the reader,
as this usually involves permissions and other information necessary.

At minimum, `create table tweets ...` with the columns listed on the CSV
file is necessary.
