"""import pyodbc
conn=pyodbc.connect('Driver={sql server};'
                    'server=LP-PF2835k3\SQL EXPRESS;'
                    'database=FilesearchResults;'
                    'Trusted_Connection=yes;')
cursor=conn.coursor()
cursor.execute('''INSERT INTO FILESearchResults_table(File_Location,searchCount,NameOfFile)
               VALUES
               ('C:\f1\sam.txt',1,'sam.txt')"""



# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'HCL-02-123\SQLEXPRESS'
database = 'FileSearchResults'
username = 'Rajyalakshmi'
password = 'Capstone@123'
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

print(cnxn)
cursor = cnxn.cursor()
print(cursor)

cursor.execute('''
                INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                VALUES
                ('F:\Apple\suresh\siva\muzzu\sun\Demo.txt',1,'Demos') ''')
cnxn.commit()

values=cursor.execute('select * from FileSearchResults_table')
for i in values:
    print(i)
