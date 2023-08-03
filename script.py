import os
import shutil

# Coded by Sathira Sri Sathsara (sathirasrisathsara.github.io)

def organize_files(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        file_extension = os.path.splitext(file)[1][1:]
        folder_name = file_extension.upper()+ "_Files"


        if not os.path.exists(os.path.join(folder_path, folder_name)):
            os.makedirs(os.path.join(folder_path, folder_name))

        shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, folder_name, file))

    print("File Organization complete !!")

folder_path = "C:\\Users\\User\\Downloads"

organize_files(folder_path)
