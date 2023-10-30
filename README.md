# DataDriverFileManagement


**Content**

- Text files for project - zip file containing the data files. Each data file starts with "ff_xxxx" and it contains information in 4 lines as below:

yyyy-mm-dd <br />
Day <br />
Town name <br />
population value <br />

- makeStructure_PoojaGupta.py - This code read the data files in the flat structure directory, creates a tree structure directory as year->month->day and copy the data file in the appropriate directory.

- statPopnyear_PoojaGupta.py - This code reports the population statistics by year. User provide the year and the stats "total", "minimum", "maximum", "average", calculates the stats and displays it for the selected year.

- createTownIndex_PoojaGupta.py - This code creates and processes indexed file for the tree strcuture file system for quicker and more efficient way of searching through large numbers of files for predetermined data.

- statPopTown_PoojaGupta.py - This code reports yearly population data for list of towns provided by the user using index file information

- statPopnTown_PoojaGupta.py - This code reporting population statistics by town provided by the user using index file information

**Instructions to execute**
1) Unzip the "text file for project" and copy the data files in C:\User\<username>\Python_Data\filesToSort in Windows or User\Python_Data\filesToSort
2) Download the python files and execute
