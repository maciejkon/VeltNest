import sqlite3


def connect():
    conn = sqlite3.connect('figures.db')
    return conn


def clean_db():
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


def add_everything(path, points, number_of_elements):
    conn = connect()

    c = conn.cursor()
    c.execute("Insert into elements (path, points, numberOfElements) VALUES (?,?,?)", (path, points, number_of_elements))

    conn.commit()
    conn.close()


def add_path_of_file(path):
    conn = connect()

    c = conn.cursor()
    c.execute("""UPDATE elements
                    SET path = ?
                    WHERE id = 1 """, (path,))
    conn.commit()
    conn.close()


def add_points(points):
    conn = connect()

    c = conn.cursor()

    c.execute("""UPDATE elements
                    SET points = ?
                    WHERE id = 1 """, (points,))

    conn.commit()
    conn.close()


def add_number_of_elements(number_of_elements):
    conn = connect()

    c = conn.cursor()
    c.execute("""UPDATE elements
                    SET numberOfElements = ?
                    WHERE id = 1 """, (number_of_elements,))

    conn.commit()
    conn.close()

def get_name():
    conn = connect()

    c = conn.cursor()
    c.execute("Select path from elements")
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return str(rows)

def get_points():
    conn = connect()

    c = conn.cursor()
    c.execute("Select points from elements")
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return str(rows)

def get_number_of_elements():
    conn = connect()

    c = conn.cursor()
    c.execute("Select numberOfElements from elements")
    rows = c.fetchall()

    conn.commit()
    conn.close()
    return str(rows)