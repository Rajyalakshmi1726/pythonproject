import pyodbc

server = 'HCL-02-18\SQLEXPRESS'
database = 'FileSearchResults'
username = 'vyshu'
password = 'Vyshu@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

def show_file_search_results_fromdb():
    values = cursor.execute('select * from FileSearchResults_table')
    for fileInfo in values:
        print("File Name: {}".format(fileInfo.NameOfFile))
        print("File Location: {}".format(fileInfo.File_Location))

def upload_file_results_todb(fileName, fileLocation, searchCount):
    query = '''  
                INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                VALUES
                ('{0}',{1},'{2}')  '''

    insertQuery = query.format(fileLocation, searchCount, fileName)
    cursor.execute(insertQuery)
    cnxn.commit()
    print("New file search results committed to DB")

# searches for a file in db
# Input : Filename (string)
# output : True or False (Boolean)
def search_in_db_for_file(fileName):
    # select query
    query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
    searchQuery = query.format(fileName)
    values = cursor.execute(searchQuery)
    if(values):
        for fileInfo in values:
            print("==========================")
            print("File name: {}".format(fileInfo.NameOfFile))
            print("File path: {}".format(fileInfo.File_Location))
            print("==========================")
        return True
    return False