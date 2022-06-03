#os stands for operating system, this module provides  a way of using os dependant functionality to steal all the moneys
import os
#this module provides functions and operation on files ( copying removing)
import shutil
import time



def main():
    path = "/pathToDelete"
    days = 30
    deletedFolders = 0
    deletedFiles = 0

    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):

            if seconds>=get_file_or_folder_age(rootFolder)  :
                remove_folder(rootFolder)
                deletedFolders+=1
                break
            
            else: 
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)

                    
                    if seconds>=get_file_or_folder_age(folderPath)  :
                        remove_folder(folderPath)
                        deletedFolders+=1

                for file in files: 
                    filePath = os.path.join(rootFolder, file)        

                    if seconds>=get_file_or_folder_age(filePath)  :
                        remove_file(filePath)
                        deletedFiles+=1

        else: 
            if seconds>get_file_or_folder_age(path):
                remove_file(path)
                deletedFiles+=1       

    else:
        print("Path is not found")
        deletedFiles+=1

    print("Total folders deleted: ", deletedFolders) 
    print("Total files deleted: ", deletedFiles)
    print("Thank you for all of your credentials! :)")   


def remove_file (path):
    if not os.remove(path):
        print("The path has been removed sucessfully: "+path)

    else:
        print("Unable to remove the "+path)
        
def remove_folder (path):
    if not shutil.rmtree(path):
        print("The path has been removed sucessfully: "+path)

    else:
        print("Unable to remove the "+path)

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_time
    return ctime

if __name__== '__main__':
    main()       








