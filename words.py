'''import sqlite3
 
con = sqlite3.connect('chatbot.sqlite')

def sql_insert(con, entities):
     
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO words(word) VALUES(?)', entities)
    
    con.commit()
 
entities = ('surat to vadara')
 
sql_insert(con, entities)'''

import sqlite3
 
con = sqlite3.connect('chatbot.sqlite')
 
def sql_insert(con, entities):
 
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO words(word) VALUES(?)', entities)
    
    con.commit()
 
entities = ('surat to vadodara')
 
sql_insert(con, entities)
