# TODO - implement check_content_type everywhere
import csv

import mysql.connector


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


# ensures that csv fields are formatted correctly
def check_fields(fields):
    if fields[0] != "type" or fields[1] != "content" or fields[2] != "text" or len(fields) != 3:
        exit("Your spreadsheet must contain three fields: type, context, and text")


# prints help message in console
# TODO
def help_message():
    print("dog")


# insert a new module into the database
def add_module(filename):
    rows = read(filename)

    if len(rows) < 3:
        exit("File not correctly formatted")

    title = rows[0]
    image = rows[1]
    desc = rows[2]

    if title[0] != "module_title" or image[0] != "module_image" or desc[0] != "module_desc":
        exit("File not correctly formatted")

    if title[1] == "" or desc[1] == "":
        exit("File not correctly formatted")

    if title[2] != "" or image[2] != "" or desc[2] != "":
        exit("File not correctly formatted")

    mydb = mysql.connector.connect(
        host="34.69.95.10",
        user="root",
        passwd="PAGLIndia",
        database="pagl_india"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO modules (module_title, module_image, module_desc) values (%s, %s, %s)"
    val = (title[1], image[1], desc[1])
    mycursor.execute(sql, val)

    module_id = mycursor.lastrowid

    row = 3
    data_inserted = 0

    while row < len(rows):
        data = rows[row]
        if check_content_type(data[0]):
            sql = "INSERT INTO module_data (parent_module, content_type, content, text) values (%s, %s, %s, %s)"
            val = (module_id, data[0], data[1], data[2])
            mycursor.execute(sql, val)
            data_inserted += mycursor.rowcount
        row += 1

    mydb.commit()

    print ("1 module with module_id = %d and %d data inserted" % (module_id, data_inserted))


# insert new data into an existing module in the database
def add_data(module_id, filename):
    # initializing the titles and rows list
    rows = read(filename)

    mydb = mysql.connector.connect(
        host="34.69.95.10",
        user="root",
        passwd="PAGLIndia",
        database="pagl_india"
    )

    mycursor = mydb.cursor()

    data_inserted = 0

    for row in rows:
        sql = "INSERT INTO module_data (parent_module, content_type, content, text) values (%s, %s, %s, %s)"
        val = (module_id, row[0], row[1], row[2])
        mycursor.execute(sql, val)
        data_inserted += mycursor.rowcount

    mydb.commit()

    print(data_inserted, "data inserted.")


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

    if mycursor.rowcount == 0:
        exit("Module could not be found")

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

    if mycursor.rowcount == 0:
        exit("Data could not be found")

    print(mycursor.rowcount, " data removed.")


# show what is stored in an existing module in the database
def show_module(module_id):
    mydb = mysql.connector.connect(
        host="34.69.95.10",
        user="root",
        passwd="PAGLIndia",
        database="pagl_india"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM modules where module_id = %s"
    val = (module_id,)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchone()

    if mycursor.rowcount == 0:
        exit("Module could not be found")

    print("Module %d:\n" % myresult[0])
    print("   Module title: %s\n" % myresult[1])
    print("   Module image: %s\n" % myresult[2])
    print("   Module desc: %s\n\n" % myresult[3])

    sql = "SELECT * FROM module_data where parent_module = %s"
    val = (module_id,)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    for data in myresult:
        print("Data %d:\n" % data[0])
        print("   Data type: %s\n" % data[2])
        print("   Data content: %s\n" % data[3])
        print("   Data text: %s\n\n" % data[4])


# show all the modules and their related metadata
def show_all():
    mydb = mysql.connector.connect(
        host="34.69.95.10",
        user="root",
        passwd="PAGLIndia",
        database="pagl_india"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM modules")

    myresult = mycursor.fetchall()

    if mycursor.rowcount == 0:
        exit("Modules could not be found")

    for module in myresult:
        print("Module %d:\n" % module[0])
        print("   Module title: %s\n" % module[1])
        print("   Module image: %s\n" % module[2])
        print("   Module desc: %s\n\n" % module[3])


# update module with given input
def update_module(module_id, filename):
    rows = read(filename)

    if len(rows) > 1:
        exit("Can only update 1 module at a time")

    row = rows[0]

    if len(row) > 3 or row[2] != "":
        exit("Can only update 1 field of a module at a time")

    if row[0] != "module_title" and row[0] != "module_image" and row[0] != "module_desc":
        exit("Cannot use field '%s'" % row[0])

    mydb = mysql.connector.connect(
        host="34.69.95.10",
        user="root",
        passwd="PAGLIndia",
        database="pagl_india"
    )

    mycursor = mydb.cursor()

    sql = "UPDATE modules SET %s" % row[0]
    sql += " = %s WHERE module_id = %s"
    val = (row[1], module_id)
    mycursor.execute(sql, val)

    mydb.commit()

    if mycursor.rowcount == 0:
        exit("Module could not be found or no change was made")

    print(mycursor.rowcount, "data updated.")


# update data with given input
def update_data(data_id, filename):
    # initializing the titles and rows list
    rows = read(filename)

    if len(rows) > 1:
        exit("Can only update 1 piece of data at a time")

    mydb = mysql.connector.connect(
        host="34.69.95.10",
        user="root",
        passwd="PAGLIndia",
        database="pagl_india"
    )

    mycursor = mydb.cursor()

    row = rows[0]

    if check_content_type(row[0]):
        sql = "UPDATE module_data SET content_type = %s, content = %s, text = %s WHERE data_id = %s"
        val = (row[0], row[1], row[2], data_id)
        mycursor.execute(sql, val)
    else:
        exit()

    mydb.commit()

    if mycursor.rowcount == 0:
        exit("Data could not be found or no change was made")

    print(mycursor.rowcount, "data updated.")


# checks to ensure that the content_type is valid
def check_content_type(content_type):
    if content_type != "text" and content_type != "image" and content_type != "video" and content_type != "header":
        print("Cannot use type '%s'" % content_type)
        return False
    else:
        return True


