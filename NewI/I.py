import pymysql

print('Hello!! What can I help you')
    
uinput=input('')
    

con = pymysql.connect('localhost', 'root', '', 'bot')

do{
    with con: 
    
    cur = con.cursor()
    scity=input("Enter City Name")
    dcity=input("Enter Destination city ")
    cur.execute("SELECT source, destination, time FROM `time table` WHERE source='"+scity+"' and destination='"+dcity+"' ")

    result = cur.fetchall()

    for rows in result:
        print('Bus from {0} to  {1} will come on {2}'.format(rows[0], rows[1], rows[2]))
        #print("{1} {2} {3}".format(row[1], row[2], row[3]))
    print('Do you need more information ?')
    coninput=input('Y or N')

}while(coninput=='Y');
