# Run this script, in this folder, if the Database was deleted

from tinydb import TinyDB, Query
import os
db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'))
db.table('devices')
db.table('reservations')

print("Database generated!")
