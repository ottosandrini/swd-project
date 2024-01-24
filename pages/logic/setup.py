from tinydb import TinyDB, Query
db = TinyDB('database.json')
db.table('devices')
db.table('reservations')

print("Database generated!")
