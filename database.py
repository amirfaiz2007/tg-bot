import sqlite3 as sq
db = sq.connect("data base1.db")
cur = db.cursor()

async def start_db():
    global db, cur
    cur.execute('CREATE TABLE IF NOT EXISTS person(user_id TEXT PRIMARY KEY, name TEXT, age TEXT, phone TEXT)')
    db.commit()

async def create_profile(id):
    user = cur.execute(f'SELECT 1 FROM person where user_id =={id}').fetchone()
    if not user:
        cur.execute("INSERT INTO person VALUES(?, ?, ?, ? )", (id, '', '', ''))
        db.commit()

async def edit_profile(id, name, age, phone):
    cur.execute(f'UPDATE person SET name = ?, age =?, phone =? WHERE user_id ==?', (name, age, phone, id))
    db.commit()






# cur.execute("CREATE TABLE IF NOT EXISTS person(user_id TEXT PRIMARY KEY, name TEXT, age TEXT, phone TEXT)")
# cur.execute("INSERT INTO person VALUES(?, ?, ?, ? )",(id, name, age, phone))
# db.commit()
# cur.execute(f'UPDATE person SET name = ?, age =?, phone =? WHERE user_id ==?',(name, age, phone, id))
# db.commit()