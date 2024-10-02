import zipfile
import os

def unzip_file(zip_file, destination_dir):
    """Unzips a ZIP file to a specified destination directory.

    Args:
        zip_file (str): The path to the ZIP file.
        destination_dir (str): The path to the destination directory.
    """

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination_dir)

# Example usage:
zip_file_path = os.path.join(os.getcwd()+ "/twic920g.zip")
destination_directory = ""

unzip_file(zip_file_path, destination_directory)