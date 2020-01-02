# AMSqlite Explorer

### Feather Set.
- Database Feathers
  - Add new database
  - Open existing databases
  - Add New Tables
    - supports default values,
    - DataTypes (also verifies Int, Floats and Varchars)
  - Drop tables
  - Add new data rows to table
  - Remove rows from table
- Options (config)
  - able to define sever address
  - able to define port
  - able to define timeout
  - add default db to load
  - able to add and removed data types
  
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

### Know Bugs
###### Major
[Fixed] Opening options crashes app  
[Fixed] Updating row crashes  
[Fixed] Fixed crash when there are not valueTypes in the config file (if theres event a config file)  



