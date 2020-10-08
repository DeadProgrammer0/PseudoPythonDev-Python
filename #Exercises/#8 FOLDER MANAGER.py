# Imports
import os
import json
from os import rename
import shutil


# Main
if __name__ == "__main__":
    ext = 0
    def folder_manager(path,exception_file,extentions,rename):
        global ext
# Doing intial checks whether  all inputs are valid or not.
#----------------------------------------------------------------------------------------------------------------
        # Importing content of Exception file into a set.
        with open(exception_file,'r',encoding='utf-8') as exct_file:
            execptions = exct_file.read()
        execptions = set(execptions.split('\n'))

        # Changing directory to give path.
        if os.path.isdir(path):
            os.chdir(path)

        # Checking if input extention is list or not.
        if type(extentions) is not list:
            raise Exception('Expected a list object.')
        extentions = set(extentions)

# Capitalizing all files except the Exceptions. (Folders remains untouched)
#----------------------------------------------------------------------------------------------------------------
        # Generating a list of all files in path folder except Exceptions.
        all_files = {file.lower() for file in os.listdir(path) if os.path.isfile(file)}
        all_files = all_files - execptions

        # Capitalizing all file names in all_files list.
        for file in all_files:
            _name, _ext = os.path.splitext(file)
            os.rename(os.path.join(path,file),('.'.join([_name.title(),_ext[1:]])))


#----------------------------------------------------------------------------------------------------------------
        # Generating a list of files which needs to be renamed as numbers. (i.e. is input extentions)
        rename_files = {file for file in all_files if file.split('.')[1] in extentions}

        # Creating a folder named according to the file extentions and dumping the files in the folder.
        for file_ in rename_files:
            # Needed Variables
            name, ext = os.path.splitext(file_)
            ext = ext[1:]
            folder_name = f'(byscript) {ext}'


            # Code that creates a folder and dump the files in it.
            if ext == '':
                continue

            if os.path.exists(os.path.join(path,ext)):
                os.rename(os.path.join(path,ext),os.path.join(path,ext))
                shutil.move(os.path.join(path,file_),os.path.join(path,ext,file_))
                
            else:
                if os.path.exists(os.path.join(path,folder_name)):
                    shutil.move(os.path.join(path,file_),os.path.join(path,folder_name,file_))

                else:
                    os.makedirs(os.path.join(path,folder_name))
                    shutil.move(os.path.join(path,file_),os.path.join(path,folder_name,file_))

# Deleting Empty Folders, Non-empty Folders are untouched and clearing up some mess created earlier.
#----------------------------------------------------------------------------------------------------------------------

        for folder in os.listdir(path):
            # Deleted Empty folders
            if os.path.isdir(folder):
                if len(os.listdir(os.path.join(path,folder))) == 0:
                    os.rmdir(os.path.join(path,folder))
                    continue

                # Renamed the files of folders which are created earlier as numbers from 1 to the number of files.
                # Not recommended to use because it got some issues.
                if rename == True:
                    if len(os.listdir(os.path.join(path,folder))) > 0 and folder.startswith('(byscript) '):
                        for num,file in zip(range(1,len(os.listdir(os.path.join(path,folder)))+1),os.listdir(os.path.join(path,folder))):
                            os.rename(os.path.join(path,folder,file),os.path.join(path,folder,f"{num}{os.path.splitext(file)[-1]}"))
                
                # Removing "(byscript)" tag from files and folders 
                for file in os.listdir(folder):
                    os.rename(os.path.join(path,folder,file),os.path.join(path,folder,file.replace('(byscript) ','')))
                if os.path.isdir(os.path.join(path,folder.replace('(byscript) ',''))) == False:
                    os.rename(os.path.join(path,folder),os.path.join(path,folder.replace('(byscript) ','')))




#----------------------------------------------------------------------------------------------------------------------


def code_runner():

# Taking user input for Path.
#----------------------------------------------------------------------------------------------------------------------
    path = input('\nEnter the Path of folder you want to Manage.\nPlease make sure what this script does by reading the Readme.md file.\nEnter Here : ')
    while os.path.isdir(path) == False:
        print('The given path is not valid! Please enter a correct Path.')
        path = input('\nEnter the Path of folder you want to Manage.\nPlease make sure what this script does by reading the Readme.md\nEnter Here : ')
        if os.path.isdir(path) == True:
            break

# Taking user input for Exception file.
#----------------------------------------------------------------------------------------------------------------------
    exception_file = input('\nEnter the path of Exception file.\nEnter here : ')
    while os.path.isfile(exception_file) == False:
        print('The given path is not valid! Please enter a correct Path.')
        exception_file = input('\nEnter the path of Exception file.\nEnter here : ')
        if os.path.isfile(exception_file) == True:
            break

# Taking user input for Extentions.
#----------------------------------------------------------------------------------------------------------------------
    with open('all-file-extensions.json','r') as json_pointer:
        json_file_exts = json.load(json_pointer)

    extentions = input('\nEnter Extentions of files you want to dump.\nExample - \"dll,exe,txt\" .Don\'t enclose in Inverted commas and seperate extentions with comma.\nEnter here : ')
    extentions = extentions.replace(' ','')
    extentions = extentions.split(',')

    for ext in extentions:
        ext_json = ext.upper()
        while ext_json not in json_file_exts:
            print(f'{ext} is a Invalid Extention! Please Enter a valid Extention.')
            extentions = input('\nEnter Extentions of files you want to dump.\nExample - \"dll,exe,txt\" .Don\'t enclose in Inverted commas and seperate extentions with comma.\nEnter here : ')
            extentions = extentions.replace(' ','')
            extentions = extentions.split(',')
            for ext in extentions:
                ext_json = ext.upper()
                if ext_json in json_file_exts:
                    break
    
    renameinp = input('\nEnter \"False\" to disallow the program from changing the filenames to serial number.\nEnter \"True\" to allow the program to change the filenames to serial numbers.\nIt\'s not recommended to use \"True\" because it only works for one time in one folder, Read README.md for more info.\nEnter Here : ').title()
    
    while renameinp not in ('True','False'):
        renameinp = input('\nEnter \"False\" to disallow the program from changing the filenames to serial number.\nEnter \"True\" to allow the program to change the filenames to serial numbers.\nIt\'s not recommended to use \"True\" because it only works for one time in one folder, Read README.md for more info.\nEnter Here : ').title()
        if renameinp not in ('True','False'):
            break
    
    if renameinp == 'True':
        renameinp == True
    elif renameinp == 'False':
        renameinp == False

    folder_manager(path=path,exception_file=exception_file,extentions=extentions,rename=renameinp)

code_runner()
