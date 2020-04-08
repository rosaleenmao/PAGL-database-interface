import csv

import database_methods

import mysql.connector

import sys

# check_arguments ensures that args are formatted correctly and stores the correct action in to-do
todo = database_methods.check_arguments(sys.argv)

# csv file name
filename = "test.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

        # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

database_methods.check_fields("Dog")

# mydb = mysql.connector.connect(
#     host="34.69.95.10",
#     user="root",
#     passwd="PAGLIndia",
#     database="pagl_india"
# )
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO modules (module_title, module_desc) VALUES (%s, %s)"
# val = ("Test", "Test")
# mycursor.execute(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")
