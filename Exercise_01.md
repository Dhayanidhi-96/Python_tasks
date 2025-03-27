Accessed the folder using python os module and renamed multiple folder using for loop

```
    import os

# Step 1: Set folder path
folder_path = r"D:\Career\Python task"

# Step 2: List all files
files = os.listdir(folder_path)

# Step 3: Loop through files and rename
for index, file in enumerate(files):
    old_path = os.path.join(folder_path, file)
    new_file_name = f"new_{index + 1}.txt"
    new_path = os.path.join(folder_path, new_file_name)
    os.rename(old_path, new_path)

print("All files renamed successfully!")
```


import os <- imported os module for acessing the operating system

folder_path = r"D:\Career\Python task" <-  created a variable called folder_path and stored my folder path in that variable.

files = os.listdir(folder_path) <- A variable called files is created to list all the files in the folder

In step 3 used for loop to rename each file name first the old_path variable  makes the index od 0th item and file name of index 0 and rename it with new_1 and store it by removing the old file this code repeat it for each file in the folder


