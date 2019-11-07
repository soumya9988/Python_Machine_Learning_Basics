import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    email = line.split()[1]
    org_id = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org_id,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org_id,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org_id,))
    conn.commit()

cur.close()