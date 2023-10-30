import os
import makeStructure_PoojaGupta

resultList = []

def calculate_statistics(numbers, keyword):
    """Description: This function calculates the total, average, minimum, and maximum of a list of numbers
    Args: Takes list of numbers and the keyword "total", "average", "minimum", and "maximum"
    Returns: Calculated stat
    """
    statistics_functions = {
        "total": sum,
        "average": lambda nums: round(sum(nums) / len(nums)),
        "minimum": min,
        "maximum": max
    }
    return statistics_functions[keyword](numbers)
    
def process_directory(directory_path, resultList, selectOption="None"):
    """Description: This functions recursively read all the data files within tree like directory structure and return a list as 
    per the selected option
    Args: It takes tree structure directory path, an empty result list, an option either be "town" or "Stats"
    Return: It returns the list containing result. If selected option is "town", it returns the list of corresponding file path and
    if selected option is "Stats", it returns the list of population numbers.
    """
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            # If it's a directory, recursively process it
            process_directory(item_path, resultList, selectOption)
        elif os.path.isfile(item_path) and item.startswith("ff"):
            # If it's a file starting with "ff," perform the desired operation
            with open(item_path, 'r') as ff:
                lines = ff.readlines()
                if selectOption == "Town":
                    resultList.append(lines[2].strip() + ":" + item_path)
                elif selectOption == "Stats":
                    resultList.append(int(lines[3].strip()))
            ff.close()
    return resultList

def inputValidation(available_options, type):
    """ Description: This function determine if the user's input is within the available option. If not then it keep
    prompting user to provide a valid option
    Args: List of available options from which user can make selection, type of option
    Returns: User's selected option
    """
    print(f"Available {type}: ", end="")
    for option in available_options:
        print(option,end=" ")
        # Get a valid year from the operator
    while True:
        selected_option = input(f"\nEnter a {type}: ")
        if selected_option in available_options:
            break
        else:
            print("ERROR: Invalid {type}. Please select a valid {type} from the list.")
    return selected_option
    

def main():
    """ Description: A user can select a year and available stats "total, "average", "minimum", "maximum", "all". This 
    code calculate the selected stats for the user selected year and displays it.
    Args: None
    Returns: None
    """
    #source directory path where the files are located
    directory_path = makeStructure_PoojaGupta.get_baseDirectory()

    ff_files_Exist = makeStructure_PoojaGupta.check_ff_files(directory_path)[0]
    if ff_files_Exist:
        print(f"Error: Directory {directory_path} contains data file \"ff_\".\nSolution: Run makeStructure_PoojaGupta.py to place these data files in the appropriate sub-directories")
    else:
        # Create a list of available years from the directory structure
        year_options = [year for year in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, year))]
        selected_year = inputValidation(year_options, "year")

        stat_options = ["total", "average", "minimum", "maximum", "all"]
        selected_stat = inputValidation(stat_options, "stats")

        year_path = os.path.join(directory_path, selected_year)
        population_data = process_directory(year_path,resultList,"Stats")
    
        if len(population_data) == 0:
            print("No population data found for the selected year.")
            return
        if selected_stat == "all":
            print(f"The total population of the year {selected_year} was {calculate_statistics(population_data, 'total')}.")
            print(f"The average population of the year {selected_year} was {calculate_statistics(population_data, 'average')}.")
            print(f"The minimum population of the year {selected_year} was {calculate_statistics(population_data, 'minimum')}.")
            print(f"The maximum population of the year {selected_year} was {calculate_statistics(population_data, 'maximum')}.")
        else:
            result = calculate_statistics(population_data, selected_stat)
            print(f"The {selected_stat} population of the year {selected_year} was {result}.")

if __name__ == "__main__":
    main()
