'''
import sqlite3
db = sqlite3.connect("surfersDB.sdb")

db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("select * from surfers")
rows = cursor.fetchall()
for row in rows:
    if row['id'] == 102:
        print("ID is " + str(row['id']))
        print("Name is " + row['name'])
        print("Board-type is " + row['board'])
        #print(row)
#print(rows)
#cursor.close()
'''
import sqlite3

def find_details(id2find):
    #Grab all the surfer data from the database, as opposed to the file
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    #print('a')
    for row in rows:
        if row['id'] == id2find:
            s = {}
            s['id'] = str(row['id'])
            s['name'] = row['name']
            s['country'] = row['country']
            s['average'] = str(row['average'])
            s['board'] = row['board']
            s['age'] = str(row['age'])
            cursor.close()
            #print(row['id'])
            #print('b')
            return(s)
    cursor.close()
    return({})

lookup_id = int(input("Enter the id of the surfer: "))
surfer = find_details(lookup_id)
if len(surfer) > 0:
    print("ID:          " + surfer['id'])
    print("Name:        " + surfer['name'])
    print("Country:     " + surfer['country'])
    print("Average:     " + surfer['average'])
    print("Board Type:  " + surfer['board'])
    print("Age:         " + surfer["age"])

#print(lookup_id)
#print(surfer)
#print(type(lookup_id))
#print(type(surfer))