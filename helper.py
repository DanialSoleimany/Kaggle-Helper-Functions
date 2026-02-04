import os
import shutil
from IPython.display import FileLink, display

def remove(path: str):
    """
    This function deletes a file or folder specified by the given path.
    If the path is a folder, all its contents will be deleted as well.
    If the path is a file, only the file will be deleted.

    Parameters:
    path (str): The path of the file or folder to delete.

    Example:
    remove('/kaggle/working/results/model_v13')  # To delete a folder
    remove('/kaggle/working/data.yaml')  # To delete a file
    """
    try:
        # Check if the path is a directory
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"The folder {path} and all its contents were successfully deleted.")
        # Check if the path is a file
        elif os.path.isfile(path):
            os.remove(path)
            print(f"The file {path} was successfully deleted.")
        else:
            print(f"The path {path} was not found or its type is undefined.")
    except Exception as e:
        print(f"Error deleting {path}: {e}")

def create_folder(path: str):
    """
    This function creates a new folder at the specified path.
    If the folder already exists, no error will be raised.

    Parameters:
    path (str): The path where the new folder will be created.

    Example:
    create_folder('/kaggle/working/predictions/part2')  # To create a folder
    """
    try:
        os.makedirs(path, exist_ok=True)  # Creates the folder if it doesn't exist
        print(f"A new folder has been created at {path}.")
    except Exception as e:
        print(f"Error creating folder at {path}: {e}")

def rename(old_path: str, new_path: str):
    """
    This function renames a file or folder from the old path to the new path.
    If the file or folder does not exist, an error message will be printed.

    Parameters:
    old_path (str): The current path of the file or folder.
    new_path (str): The new path to rename the file or folder to.

    Example:
    rename('/kaggle/working/results/model_v16', 
           '/kaggle/working/results/model1_part1')  # To rename a file or folder
    """
    try:
        # Check if the old path exists
        if not os.path.exists(old_path):
            print(f"The file or folder at {old_path} was not found.")
            return

        # Check if the new path already exists
        if os.path.exists(new_path):
            print(f"The destination {new_path} already exists. Rename failed.")
            return

        # Rename the file or folder
        os.rename(old_path, new_path)
        print(f"The file or folder has been renamed to {new_path}.")
        
    except Exception as e:
        print(f"Error renaming: {e}")

def pytorch_model_downloader(
    source_path: str,
    dest_filename: str = "best.pt"
):
    """
    Copies a PyTorch model file to Kaggle working directory and
    displays a clean download link showing only the model filename
    (without /kaggle/working in the link path).

    Parameters
    ----------
    source_path : str
        Full path to the source model file.

    dest_filename : str, optional
        Output filename shown for download (e.g. best.pt, last.pt).

    Returns
    -------
    str or None
        Absolute destination path if successful, otherwise None.
    """

    if not os.path.exists(source_path):
        print("Source model file not found. Please check the source path.")
        return None

    dest_path = os.path.join("/kaggle/working", dest_filename)

    shutil.copy(source_path, dest_path)
    print(f"Model file copied successfully: {dest_filename}")

    # IMPORTANT: show link using filename only
    display(FileLink(dest_filename))

    return dest_path

def move(src_path: str, dest_dir: str):
    """
    This function moves a file or folder from the source path to a destination directory.
    It automatically handles the creation of the destination folder if it does not exist
    and ensures the original file/folder name is preserved in the new location.

    Parameters:
    src_path (str): The current path of the file or folder to move.
    dest_dir (str): The path of the directory where the item should be moved to.

    Example:
    move('/kaggle/working/best.pt', '/kaggle/working/models/v1')  # To move a file
    move('/kaggle/working/temp_data', '/kaggle/working/archive')  # To move a folder
    """
    try:
        # Check if the source path exists
        if not os.path.exists(src_path):
            print(f"The source file or folder at {src_path} was not found.")
            return

        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir, exist_ok=True)
            print(f"Destination directory created at {dest_dir}.")

        # Determine the final destination path including the original filename/foldername
        base_name = os.path.basename(src_path)
        final_destination = os.path.join(dest_dir, base_name)

        # Move the file or folder
        shutil.move(src_path, final_destination)
        print(f"Successfully moved {base_name} to {dest_dir}.")

    except Exception as e:
        print(f"Error moving {src_path} to {dest_dir}: {e}")
