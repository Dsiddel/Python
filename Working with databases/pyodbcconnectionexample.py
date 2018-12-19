# Example of connecting to Azure SQL Database

import pyodbc

param_server = 'x'
param_database = 'y'
param_username = 'z'
param_password = '1!'
param_driver= '{ODBC Driver 13 for SQL Server}' # for connecting to Azure SQL

def dbcon(server, database, password, driver):
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cursor


dbconnect = dbcon(param_server, param_database, param_password, param_driver)
for res in output["value"]: #runs through an API result and records details, this exmample is a result of list of resource groups in azure
    dbconnect.execute("{CALL UpdateResourceGroups (?,?,?)}", res["name"], res["location"], Client.Subscription) #calls stored procedure that dumps name, location and subscription into database table
    dbconnect.commit() #must commit before closing
dbconnect.close()