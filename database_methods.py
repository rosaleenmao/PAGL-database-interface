import csv

import mysql.connector


# parses a csv and returns the data : fields and rows
def read(filename):
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

    check_fields(fields)

    return rows


# ensures arguments are passed in correctly
# returns string that represents that the main method should do
def check_arguments(argv):
    n = len(argv)

    # not help message and doesn't have right number of arguments
    if n < 2 or n > 4:
        exit("Incorrect number of inputs : %d. "
             "First include what you want to use, then the file or title your module" % (n - 1))

    # meets conditions to display help message
    if n == 2:
        if (argv[1] == "help") or (argv[1] == "-h") or (argv[1] == "-help"):
            return "help"

        # check if user wants to show all modules
        elif (argv[1] == "show_all") or (argv[1] == "-sa"):
            return "show all"

    # check if user wants to add module
    if n == 3:
        if (argv[1] == "add_module") or (argv[1] == "-am"):
            check_csv(argv[2])
            return "add module"

        # check if user wants to remove module
        elif (argv[1] == "remove_module") or (argv[1] == "-rm"):
            check_int(argv[2])
            return "remove module"

        # check if user wants to remove data
        elif (argv[1] == "remove_data") or (argv[1] == "-rd"):
            check_int(argv[2])
            return "remove data"

        # check if user wants to show a specific module
        elif (argv[1] == "show_module") or (argv[1] == "-sm"):
            check_int(argv[2])
            return "show module"

    if n == 4:
        # check if user wants to add data
        if (argv[1] == "add_data") or (argv[1] == "-ad"):
            check_int(argv[2])
            check_csv(argv[3])
            return "add data"

        # check if user wants to add data
        elif (argv[1] == "update_module") or (argv[1] == "-um"):
            check_int(argv[2])
            check_csv(argv[3])
            return "update module"

        # check if user wants to add data
        if (argv[1] == "update_data") or (argv[1] == "-ud"):
            check_int(argv[2])
            check_csv(argv[3])
            return "update data"

    # at this point, we know the user hasn't entered a valid command
    else:
        exit("You did not give a valid action. "
             "If you want to see the possible commands, try this command : $ %s help" % argv[0])


# ensures that argument is csv
def check_csv(csv_file):
    if csv_file[-4:] != ".csv":
        exit("To add data or a module, you have to pass in a csv file")


# ensures that argument is an int
def check_int(int_to_check):
    if int_to_check.isdigit() is False:
        exit("To remove or view a module or its data, you have to pass in its id")


# prints help message in console
# TODO
def help_message():
    print("dog")


# ensures that csv fields are formatted correctly
def check_fields(fields):
    if fields[0] != "type" or fields[1] != "content" or fields[2] != "text" or len(fields) != 3:
        exit("Your spreadsheet must contain three fields: type, context, and text")


# insert a new module into the database
# TODO
def add_module(cat):
    print("am")


# insert new data into an existing module in the database
# TODO
def add_data(module_id, filename):
    # initializing the titles and rows list
    rows = []

    rows = read(filename)

    print("\n")
    print(rows)
    print("\n")


# remove a module from the database
def remove_module(module_id):
    mydb = mysql.connector.connect(
        host="34.69.95.10",
        user="root",
        passwd="PAGLIndia",
        database="pagl_india"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM modules WHERE module_id = %s"
    val = (module_id,)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "module removed.")


# remove data from an existing module in the database
def remove_data(data_id):
    mydb = mysql.connector.connect(
        host="34.69.95.10",
        user="root",
        passwd="PAGLIndia",
        database="pagl_india"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM module_data WHERE data_id = %s"
    val = (data_id,)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, " data removed.")


# show what is stored in an existing module in the database
# TODO
def show_module(cat):
    print("sm")


# show all the modules and their related metadata
# TODO
def show_all():
    print("sa")


# update module with given input
# TODO
def update_module(module_id, filename):
    print("um")


# update data with given input
# TODO
def update_data(data_id, filename):
    print("ud")
