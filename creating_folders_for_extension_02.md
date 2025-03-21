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