# automation_Estimation
Just a Horrible mess

Focus of this is to create a standard method for estimating sutomation based off of volumetrics provided in xml,cvs or flat text file

Git repo set up

Python venv created to reactive
source /venv/bin/activate

following Packages installed:
- Numpy
- Pandas
- scikit Learn
- npyscreen, used for TUI generation


Src directoy
- Main -- will start all the functions, and load data
- Product_Fit -- complete the checks that the products fit within the system -- add unit selector
- Data _filter -- need this to be variable having the ability to add new filter points
- Bin count -- actually collate the data and use the the products volumes and stock holding to generate the bin count for AS 
- TUI -- simplist terminal interface to speed up getting results
- Test cases -- complete tests to confirm no data loss and ensure code accuracy
Leave room for expansion and modification

