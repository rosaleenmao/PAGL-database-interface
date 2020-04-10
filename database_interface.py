import database_methods

import sys

# check_arguments ensures that args are formatted correctly and stores the correct action in to-do
todo = database_methods.check_arguments(sys.argv)

if todo == "help":
    database_methods.help_message()
elif todo == "show all":
    database_methods.show_all()
elif todo == "show module":
    database_methods.show_module(sys.argv[2])
elif todo == "add module":
    database_methods.add_module(sys.argv[2])
elif todo == "add data":
    database_methods.add_data(sys.argv[2], sys.argv[3])
elif todo == "remove module":
    database_methods.remove_module(sys.argv[2])
elif todo == "remove data":
    database_methods.remove_data(sys.argv[2])
elif todo == "update module":
    database_methods.update_module(sys.argv[2], sys.argv[3])
elif todo == "update data":
    database_methods.update_data(sys.argv[2], sys.argv[3])
