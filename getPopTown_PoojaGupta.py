# Reporting Yearly Population Data Town Using Index File Information
import makeStructure_PoojaGupta
import os

# Define a function to retrieve population data for a given town
def retrieve_population(directory_path, town_files):
    """Description: This function read the data files for a town and determine the population for a date
    Args: data file directoy, list of data file paths
    Returns: list in the format (date:population value)
    """
    townStats = []
    
    #change the current working directory to the data file directory
    os.chdir(directory_path)
    for file in town_files:
        with open(file, 'r') as data_file:
            lines = data_file.readlines()
            if lines:
                townStats.append(lines[0].strip()+":"+lines[-1].strip())
    return townStats
       
def getFilePathinDict(index_filepath):
    """ Description: This function read the index file "townFileIndex.txt" to store the towns and file path in a dictionary
    Args: file path of index file "townFileIndex.txt"
    Returns: dictonary containing town name as key and list of file paths as value
    """
    town_dict = {}
    with open(index_filepath, 'r') as index_file:
        for line in index_file:
            # Split the line into key and value based on the ':' character
            key, value = line.strip().split(':')
            # Check if the key is already in the dictionary
            if key in town_dict:
                # If the key is present, append the value to the list
                town_dict[key].append(value)
            else:
                # If the key is not present, create a new list with the value
                town_dict[key] = [value]
    index_file.close()
    return town_dict

def main():    
    directory_path = makeStructure_PoojaGupta.get_baseDirectory()
    town_index_file = 'townFileIndex.txt'
    index_filepath = os.path.join(directory_path, town_index_file)

    ff_files_Exist = makeStructure_PoojaGupta.check_ff_files(directory_path)[0]
    if ff_files_Exist:
        print(f"Error: Directory {directory_path} contains data file \"ff_\".\nSolution: Run makeStructure_PoojaGupta.py to place these data files in the appropriate sub-directories")
    elif not os.path.exists(index_filepath):
        print(f"Error: Index file {town_index_file} does not exist in {directory_path}.\nSolution: Run createTownIndex_PoojaGupta.py first to create the index file")
    else:
        # Ask the user to input town names
        input_towns = input("Enter town name(s) separated by commas: ").split(',')

        #Read the index file and create a dictonary of town as key and list of file paths as value
        town_dict = getFilePathinDict(index_filepath)
        
        # Retrieve population data for each specified town
        for town in input_towns:
            town = town.strip()
            if town in town_dict.keys():
                result = retrieve_population(directory_path, town_dict[town])
                print(town+":")
                [print(element) for element in result]
            else:
                print(f"{town}:\nCannot find this town in the current records.")
    
if __name__ == "__main__":
    main()