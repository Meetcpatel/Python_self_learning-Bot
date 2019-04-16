import sqlite3
 
con = sqlite3.connect('chatbot.sqlite')
 
def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT * FROM words')
 
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        print(row)
 
sql_fetch(con)

'''import sqlite3
 
con = sqlite3.connect('mydatabase.db')
 
def sql_insert(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()
 
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
 
sql_insert(con, entities)'''