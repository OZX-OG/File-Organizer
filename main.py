import os
import shutil

print(f"- Default path: {os.getcwd()}\n")

def organize_files(folder_path, output_path, default):
    # List all files and folders in the specified directory
    try:
        if folder_path == "": files = os.listdir()
        else: files = os.listdir(folder_path)

    except (FileNotFoundError, OSError): return "Path you Enter is NOT Found."
    
    # Iterate over each file
    for file in files:
        # Check if script here 
        if default and file == os.path.basename(__file__): continue

        # Create the full path of the file
        file_path = os.path.join(folder_path, file)

        # Skip if the current item is a folder
        if os.path.isdir(file_path): continue

        # Get the file extension
        _, ext = os.path.splitext(file)
        if ext == "": ext = ".others"

        # Create the directory for the specific file extension
        destination_folder = os.path.join(output_path, ext[1:])
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file to the destination folder
        destination_path = os.path.join(destination_folder, file)
        shutil.move(file_path, destination_path)
    return "File organization complete."

while True:
    
    # Prompt the user to enter the input and output paths
    input_path = input("Enter the input folder path (press Enter for default): ")
    output_path = input("Enter the output folder path (press Enter for default): ")
    
    if input_path == "" or input_path== os.getcwd(): default = True
    else: default = False

    print(f"\n{organize_files(input_path, output_path, default)}", end="\n")
    print("-  -  -  -  -  -\n")




