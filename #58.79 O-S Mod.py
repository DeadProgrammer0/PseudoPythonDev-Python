# OS Module

import os


# print(dir(os))

#* prints current working directory.
# print(os.getcwd())

#* changes current working directory.
# os.chdir("C://")
# print(os.getcwd())

#* prints content of directory.
# print(os.listdir(os.getcwd()))

#* makes a new directory.
# os.mkdir("This")
#* makes new directories.
# os.makedirs("This/That")

#* renames a file.
# os.rename("dict.txt","dict100.txt")

#* prints environment vars.
# print(os.environ.get('Path'))

#* joins two given directories.
# print(os.path.join("E://","/#Garbage"))

#* checks if directory exists.
# print(os.path.exists("C://Program Files"))

#* cheks if the directory is file.
# print(os.path.isfile("C://Program Files"))


#---------------------------------------------------Extra--------------------------------------------------------------------

#* prints os name.
# print(os.name)


#* opens the given file 
# file = os.popen("eyes.mp3")
# file.read()

