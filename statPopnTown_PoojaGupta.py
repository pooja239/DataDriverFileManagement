import makeStructure_PoojaGupta
import getPopTown_PoojaGupta
import statPopnYear_PoojaGupta
import os


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
        town_dict = getPopTown_PoojaGupta.getFilePathinDict(index_filepath)
        selected_town = statPopnYear_PoojaGupta.inputValidation(list(town_dict.keys()), "town")
        get_population_data = getPopTown_PoojaGupta.retrieve_population(directory_path,town_dict[selected_town])
        population_data = [int(item.split(':')[1]) for item in get_population_data]
        print(selected_town+":")
        print(f"The total population is {statPopnYear_PoojaGupta.calculate_statistics(population_data, 'total')}.")
        print(f"The average population is {statPopnYear_PoojaGupta.calculate_statistics(population_data, 'average')}.")
        print(f"The minimum population is {statPopnYear_PoojaGupta.calculate_statistics(population_data, 'minimum')}.")
        print(f"The maximum population is {statPopnYear_PoojaGupta.calculate_statistics(population_data, 'maximum')}.")


if __name__ == "__main__":
    main()