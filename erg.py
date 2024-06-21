import sqlite3 as sq

db = sq.connect("data base.db")
cur = db.cursor()
async def get_photo(name):
    return cur.execute(f"SELECT id FROM images where name == '{name}'").fetchone()[0]
