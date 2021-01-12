import mysql.connector
import pandas as pd

db = mysql.connector.connect(user='root', password='password', host='localhost', database='ir_assignment')
cursor = db.cursor()

ratings = pd.read_csv('BX-Book-Ratings.csv', sep=";", encoding='ISO-8859-1')
books = pd.read_csv('BX-Books.csv', sep=";", encoding='ISO-8859-1')
users = pd.read_csv('BX-Users.csv', sep=";", encoding='ISO-8859-1')

for index, row in ratings.iterrows():
    if row['ISBN'][0] == "'":
        query = "INSERT INTO ratings VALUES (" + str(row['User-ID']) + ", " + str(row['ISBN']) + ", " + \
                str(row['Book-Rating']) + ");"
    else:
        query = "INSERT INTO ratings VALUES (" + str(row['User-ID']) + ", '" + str(row['ISBN']) + "', " + \
                str(row['Book-Rating']) + ");"

    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        print(row)
        print(index)
        print(query)
        input()
    if index % 1000 == 0:
        print(index)

db.commit()

for index, row in books.iterrows():
    query = "INSERT INTO books VALUES('" + str(row['ISBN']) + "', '" + str(row['Book-Title']) + "', '" + \
            str(row['Book-Author']) + "', " + str(row['Year-Of-Publication']) + ", '" + str(row['Publisher']) + \
            "', '" + str(row['Image-URL-S']) + "', '" + str(row['Image-URL-M']) + "', '" + str(row['Image-URL-L']) + \
            "');"
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        print(row)
        print(index)
        print(query)
        input()
    if index % 1000 == 0:
        print(index)

db.commit()

for index, row in users.iterrows():
    if pd.isnull(row['Age']):
        query = "INSERT INTO users VALUES(" + str(row['User-ID']) + ", '" + str(row['Location']) + "', " + \
                "NULL" + ");"
    else:
        query = "INSERT INTO users VALUES(" + str(row['User-ID']) + ", '" + str(row['Location']) + "', '" + \
                str(row['Age']) + "');"
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        print(row)
        print(index)
        print(query)
        input()
    if index % 1000 == 0:
        print(index)

db.commit()
