import os
import shutil

def organize_folder(target_path):
    # Change the current working directory to the target path
    if not os.path.exists(target_path):
        print("The specified path does not exist.")
        return

    # Define the mapping of extensions to folder names
    extension_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.tar', '.rar', '.7z'],
        'Executables': ['.exe', '.msi', '.dmg']
    }

    # Loop through all files in the directory
    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Find the appropriate folder
        moved = False
        for folder_name, extensions in extension_map.items():
            if extension in extensions:
                dest_folder = os.path.join(target_path, folder_name)
                
                # Create the folder if it doesn't exist
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                # Move the file
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                moved = True
                break
        
        # Optional: Move unknown files to an 'Others' folder
        if not moved and extension != '':
            other_folder = os.path.join(target_path, 'Others')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} -> Others/")

if __name__ == "__main__":
    # Replace this with the path to the folder you want to organize
    path_to_clean = input("Enter the full path of the folder to organize: ")
    organize_folder(path_to_clean)
    print("Organization complete!")
