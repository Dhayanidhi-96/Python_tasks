CODE FOR CREATING SEPERATE FOLDERS FOR EXTENSION

```
import os
import shutil

folder_path = "D:\Career\Python task"

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path,file_name)
    if os.path.isfile(file_path):
        _, extension = os.path.splitext(file_name)
        extension = extension[1:]

        if extension:
            new_folder_path = os.path.join(folder_path,extension)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            shutil.move(file_path,os.path.join(new_folder_path,file_name))
print("Files have been sorted by extension!")

```

step 1 : Imported os library and shutil for os operations and moving files to folders
step 2 : Created a folder_path variable to store the folder path which contain the different file types
step 3 : Used for loop to iterate each file to move it to its extension folder
step 4 : created a variable to store a new folder according to its extension type
step 5 : If the folder contains a file it checks wheather its a file or not it file then it reperates the extension name (ie abc.pdf , "abc",".pdf") then check for the pdf folder if not it creates a folder named pdf and move the filr to the folder .
