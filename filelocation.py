import os#search ,update ,access
import re#
import win32api#connect drives ->pycharm
import concurrent.futures#multithreading
import uploadfiles

class FindFileLocation:###1)search for a file in our local drives by using multi-threading
    #2) This class then calls UploadFilesToDB to store file search results in sql db
    def find_file(self, root_folder, rex):##1)search for a file in our "local drive"
           #2) Input: This method accepts drive and "filename as parameter"

        for root, dirs, files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                if result:
                    print("File name: {} - File location: {}".format(f, root))
                    print("File location: {}".format(root))
                    # call to method insert_file_search_results to upload file search results to db
                    self.insert_file_search_results(root, f, 0)
                    break  # if you want to find only one

    # Method find_file_in_all_drives is used to get all the available drives in our local system/VM
    def find_file_in_all_drives(self, file_name):
        # create a regular expression for the file
        rex = re.compile(file_name)

        drives = [drivestr for drivestr in  win32api.GetLogicalDriveStrings().split('\000')[:-1]]
        print(drives)
        # concurrency call to acheive multi-threading
        with concurrent.futures.ThreadPoolExecutor() as executor:
            [executor.submit(self.find_file, drive, rex) for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]]

    # Method insert_file_search_results is used to  call method upload_file_results_todb which is in class "UploadFilesToDB"
    def insert_file_search_results(self, fileLocation, fileName, searchCount = 0):
        uploadObject.upload_file_results_todb(fileName, fileLocation, searchCount)


    # input: accepts filename as input
    # this method internally call method search_in_db_for_file which is in class UploadFilesToDB
    def search_forfile_indb(self, fileName):###1)search file results in db.
        # call method search_in_db_for_file to
        uploadObject.search_in_db_for_file(fileName)###search for a file result in db
        print("File search results from local drive")
        self.find_file_in_all_drives(fileName)

# required objects of class
locationObject = FindFileLocation()
locationObject.find_file_in_all_drives("newFile.txt")
uploadObject = uploadfiles.UploadFilesToDB()
fileToSearch = input()
locationObject.search_forfile_indb(fileToSearch)

####The win32api module provides various libraries and objects utilized
# to deal with the Windows system’s Application Programming Interface (API).

##The PyWin32 library, which is already a part of the Python extension, enables the win32api module in Python.

