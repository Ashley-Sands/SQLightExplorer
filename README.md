# AMSqlite Explorer

### Running AMSqlite
Run '/build/main.exe' to run the standalone build of the AMSqlite  
The AMSqlite has been build using PyInstaller 3.5  
To run AMSqlite from source run main.py using python 3.7 with PyQt5 (version 5.13.2) installed  

### Features Set.
- Database Features
  - Add new database
  - Open existing databases
  - Add New Tables
    - supports default values,
    - max value length,
    - and DataTypes (also verifies Int, Floats and Varchars)
  - Drop tables
  - Add new data rows to table
  - Remove rows from table
  - update tables
- Options (config)
  - able to define sever address,
  - define port,
  - define timeout,
  - add default db to load
  - and add data types

### Using AMSqlite
To open a table in a new tab, double click on the table name listed below 
database (left side) (also refreshes table view if open)   
Double click on a table cell to edit the value  
When added a new table any column names left empty will NOT be added  
To changes the app's settings go to ```Options``` located in ```File``` in the tool bar
 
### NOTES
This has been designed to work with a backend server (Git repo: https://github.com/Ashley-Sands/Comp-280-PythonServer)

Column data needs to have editable added server end  
if using sqlite don't forget to add the default column 'rowid' for the unique key, and it should be set to NOT editable 

### TODO
[WIP] New Table  
[ ] Destroy Database  
[C] Fix major issues  
[C] Add row  
[C] Refactor  
-[C] Actions  
-[C] table tabs  
[ ] Undo steps?
[ ] Update text in dialogue windows

### Know Bugs
###### Major
[Fixed] Opening options crashes app  
[Fixed] Updating row crashes  
[Fixed] Fixed crash when there are not valueTypes in the config file (if theres event a config file)  
[Fixed] Fix crash when removing the last row from table
[ ] Fix tab not reopening once closed

