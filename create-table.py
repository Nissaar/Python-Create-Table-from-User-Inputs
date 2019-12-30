import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="password", #MySQL server password
database="database" #database name
)

mycursor = mydb.cursor()

table_name = input("Name of Table: ")
primary_key = input("Name of Primary Key: ")
datatype_of_primary_key = input("Datatype of Primary Key: ")
primary_key_method = input("Primary Key method to be used (AUTO_INCREMENT for example): ")

sql = "CREATE TABLE " + table_name + " (" +" "+ primary_key +" "+ datatype_of_primary_key +" "+ primary_key_method +" "+ "PRIMARY KEY);"

mycursor.execute(sql)

print("Table "+table_name+"has been successfully created with primary key "+primary_key)

column_no = int(input("How many columns to be created ?"))

def add_column(table_name):
    column_name = input("Name of column: ")
    data_type = input("Datatype: ")
    sql1 = "ALTER TABLE " + table_name + " ADD " +column_name+" "+data_type+" ;"
    mycursor.execute(sql1)
    print(column_name + " Added Successfully")

for i in range(column_no):
    add_column(table_name)


check = input("Do you need more columns ? (y/n): ")

if check == "y" or check == "Y":
    more = int(input("How many more columns do you need ? : "))
    for i in range(more):
        add_column(table_name)
else :
    print("Columns added Successfully.")
