import os
import getpass
import testSystem

def get_baseDirectory():
    """Description: This function takes nothing and returns the directory containing the data files
    Args: None
    Returns: Path of the directory containing the data files
    """
    #get the base directory path
    baseDirectory = testSystem.switch_system()[1]
    #source directory path where the files are located
    return os.path.join(baseDirectory, getpass.getuser(), "Python_Data", "filesToSort")

def check_ff_files(source_directory):
    """Description: This function reads the files in the data directory and determines if it contains data files starting with "ff_"
    Args: data directory path
    Returns: If directory contains data files starting with "ff_" return True otherwise False and also list of data files
    Raise: FileNotFoundError, PermissionError
    """
    try:
        files = os.listdir(source_directory)
        ff_files = [file for file in files if file.startswith("ff_")]
    except FileNotFoundError as e:
        print(f"Error: {e}. The specified directory does not exist.")
    except PermissionError as e:
        print(f"Error: {e}. Permission denied while trying to list files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    if len(ff_files)==0:
        return False, ff_files
    else:
        return True, ff_files


def createDirStructure(source_directory):
    """Description: This function read all the files in the data directory, and create a tree directory structure with year-> month-> day and places the files in it
    Args: Data directory
    Returns: Files are copied successfully to the tree directoty structure returns "Success" otherise "Fail"
    Raise: FileExistsError, general exception
    """
    #list of files starting with "ff_"

    ff_files_Exist, ff_files = check_ff_files(source_directory)
    if ff_files_Exist:
        # for each file in the direcory, read the first line and then create sub-directories if does not exist
        for ff_file in ff_files:
            source_file_path = os.path.join(source_directory,ff_file)
            try:
                with open(source_file_path, 'r') as f:
                    first_line = f.readline().strip()
                    date_parts = first_line.split("-")
                    current_directory = source_directory
                    for component in date_parts:
                        try:
                        # Attempt to create the directory
                            os.mkdir(os.path.join(current_directory, component))
                        except FileExistsError:
                        # Handle the case where the directory already exists
                            print(f"Directory '{component}' already exists.")
                        current_directory = os.path.join(current_directory, component)
                f.close()
                #the file is copied to the new directory location 
                destination_file_path = os.path.join(current_directory,ff_file)
                os.rename(source_file_path,destination_file_path)
            except Exception as e:
                print(f"Error processsing {ff_file}: {e}")
        print("Successfully created tree directory structure and copied the files")
    else:
        # Files starting with "ff" are not present, display the error message and quit the code
        print(f"Error: No files starting with 'ff' found. Copy the required files to the directory {source_directory}")

def main():
    """Description: This code determines the data directory path and places the data files in the tree like directory structure with year-> month-> day
    Args: None
    Returns: None
    """
    sourceDirectory = get_baseDirectory()
    createDirStructure(sourceDirectory)

if __name__ == "__main__":
    main()
