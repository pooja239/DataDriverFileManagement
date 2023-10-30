import os
import makeStructure_PoojaGupta
import statPopnYear_PoojaGupta

def main():
    """Description: This code create a index file listing all the town and the corresponding path of its data file
    Args: None
    Returns: None
    """
    directory_path=makeStructure_PoojaGupta.get_baseDirectory()

    ff_files_Exist = makeStructure_PoojaGupta.check_ff_files(directory_path)[0]
    if ff_files_Exist:
        print(f"Error: Directory {directory_path} contains data file \"ff_\".\nSolution: Run makeStructure_PoojaGupta.py to place these data files in the appropriate sub-directories")
    else:
        town_index = []

        # Create a dictonary with town as key and list of file paths as value
        town_index=statPopnYear_PoojaGupta.process_directory(directory_path, town_index, "Town")
        
        # Sort the towns alphabetically
        sorted_town_index = sorted(town_index)
        sorted_town_index = [item.replace(directory_path, ".") for item in sorted_town_index]

        index_filepath = os.path.join(directory_path, "townFileIndex.txt")
        if os.path.exists(index_filepath):
            os.remove(index_filepath)

        # Write the index to a file
        with open(index_filepath, 'w') as index_file:
            for town in sorted_town_index:
                index_file.write(f"{town}\n")
        print(f"Successfully created the index file at {index_filepath}")

if __name__ == "__main__":
    main()