import sqlite3


def connect():
    conn = sqlite3.connect('figures.db')
    return conn


def cleanDb():
    conn = connect()
    c = conn.cursor()
    c.execute("""Drop table if exists elements;""")

    c.execute("""Create table if not exists elements (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            path BLOB DEFAULT 'nothing' not null,
                            points BLOB DEFAULT 'nothing' not null,
                            numberOfElements INTEGER DEFAULT 'nothing' not null
                    );""")
    c.execute("Insert into elements (path, points, numberOfElements) VALUES ('DEFAULT','DEFAULT','DEFAULT')")
    conn.commit()
    conn.close()


def addEverything(path, points, numberOfElements):
    conn = connect()

    c = conn.cursor()
    c.execute("Insert into elements (path, points, numberOfElements) VALUES (?,?,?)", (path, points, numberOfElements))

    conn.commit()
    conn.close()


def addPath(path):
    conn = connect()

    c = conn.cursor()
    #c.execute("Insert into elements (path) VALUES (?)",(path,))
    c.execute("""UPDATE elements
                    SET path = ?
                    WHERE id = 1 """, (path,))
    conn.commit()
    conn.close()


def addPoints(points):
    conn = connect()

    c = conn.cursor()

    c.execute("""UPDATE elements
                    SET points = ?
                    WHERE id = 1 """, (points,))

    conn.commit()
    conn.close()


def addNumberOfElements(numberOfElements):
    conn = connect()

    c = conn.cursor()
    c.execute("""UPDATE elements
                    SET numberOfElements = ?
                    WHERE id = 1 """, (numberOfElements,))

    conn.commit()
    conn.close()

def getPoints():
    conn = connect()

    c = conn.cursor()
    c.execute("Select points from elements")
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return str(rows)

def getNumberOfElements():
    conn = connect()

    c = conn.cursor()
    c.execute("Select numberOfElements from elements")
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return str(rows)