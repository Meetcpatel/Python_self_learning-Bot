import pymysql
con = pymysql.connect('localhost', 'root', '', 'bot')

b=0
def bus_timeing():
    cur = con.cursor()
    user = input()
    list1 = user.split()
    indexsource=list1.index('to')
    scity=Source=(list1[indexsource-1])
    dcity=Destination=(list1[indexsource+1])
    cur.execute("SELECT source, destination, time FROM `time table` WHERE source='"+scity+"' and destination='"+dcity+"' ")
    result = cur.fetchall()
    for rows in result:
        print('Bus from {0} to  {1} will come on {2}'.format(rows[0], rows[1], rows[2]))
        #print("{1} {2} {3}".format(row[1], row[2], row[3]))
def bus_fare():
    cur = con.cursor()
    user = input()
    list1 = user.split()
    indexsource=list1.index('to')
    scity=Source=(list1[indexsource-1])
    dcity=Destination=(list1[indexsource+1])
    cur.execute("SELECT source, destination, fare FROM `time table` WHERE source='"+scity+"' and destination='"+dcity+"' ")
    result = cur.fetchall()
    for rows in result:
        print('Bus from {0} to  {1} will cost you {2}'.format(rows[0], rows[1], rows[2]))

def bus_loc():
    cur = con.cursor()
    user = input()
    list1 = user.split()
    indexsource=list1.index('to')
    scity=Source=(list1[indexsource-1])
    dcity=Destination=(list1[indexsource+1])
    cur.execute("SELECT source, destination, location FROM `time table` WHERE source='"+scity+"' and destination='"+dcity+"' ")
    result = cur.fetchall()
    for rows in result:
        print('Bus from {0} to  {1} is in now {2}'.format(rows[0], rows[1], rows[2]))

while b==0:
    print('Hello!! What can I help you')
    print('Enter 1 for Knowing the timeing')
    print('Enter 2 for checking the fare')
    print('Enter 3 for bus location')
    print('Enter Y to continue')
    print('Press any key to exit')
    a=int(input('Enter your choice:'))
    if a==1:
        bus_timeing()
    elif a==2:
        bus_fare()
    elif a==3:
        bus_loc()
    else:
        b=1
        exit()
