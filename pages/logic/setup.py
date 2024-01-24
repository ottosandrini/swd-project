# Run this script, in this folder, if the Database was deleted

from tinydb import TinyDB, Query
db = TinyDB('database.json')
db.table('devices')
db.table('reservations')

print("Database generated!")
