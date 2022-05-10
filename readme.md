# Vayyar Exercise

## Author(s): 
- Mike Lasry

### Installation
```
$ git clone https://github.com/mikelasry/VayyarEx.git
```
### Running the project
```
$ cd VayyarEx
$ python ./solution.py
```

### General Info
The project is divided to different files
- another_solution.py is the file to contain the solution which takes in account two frames in a row inside the section, in order to aggregate 0.1 seconds (commented out)
- classes.py is the file to contain the Frame class which defines single frame's (sensor snapshot) data members (coords) and functionalities
- constants.py is the file to define all constants for reusability and better readability of the code
- explore.py is the file to better understand the data e.g. check if "Targets" attribute may be ignored, incontinuous frames etc.
- functions.py is the file to contain all stand-alone functions and their docstrings
- solution.py is the file which calculate and print the duration inside the closed section to the console
- testing.py is the file to test the main function (isInChairArea) by generating all possible frames in the room, then write them to the mathcing file, then test them (prints to console). Running this file generates directory names testFiles which will contain the true log file as well as the false log file to be checked.
- tracker_log.log is the file given by Vayyar Imaging to parse and calculate duration
