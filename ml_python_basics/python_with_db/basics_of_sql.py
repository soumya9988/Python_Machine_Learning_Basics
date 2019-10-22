import mysql.connector

word = input('Enter the word whose meaning has to be found: ')

con = mysql.connector.connect(
                                user= 'ardit700_student',
                                password = 'ardit700_student',
                                host =  '108.167.140.122',
                                database = 'ardit700_pm1database'
)

cursor = con.cursor()

query = cursor.execute(" SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    print('Possible meanings of %s are:\n' % word)
    for result in results:
        print(result[1])
else:
    print('No results found')