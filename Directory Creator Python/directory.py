import os


# function to get inputs 
def get_input():
    print(" ==== WELCOME TO DIRECTORY CREATOR ==== \n")

    file_name = input("Enter the name of the file: ")
    option = input("Do you want to create a single or multiple file/s? (Enter s for single, m for multiple) ")

    #statemtets to assess wheter you want to create a single file or multiple files
    if option == "s":
        single_create_file(file_name)
    elif option =="m":
        start_number = int(input("Enter the start_number to start with: "))
        end_number = int(input("Enter the end_number to end with: "))
        for number in range(start_number, end_number+1):
            mulitple_create_files(file_name, number)
        
    else:
        print("Good")

# function to create a single file
def single_create_file(file_name):
    path = f"../100-Days-of-Code-Complete-Python-Pro-by-Angela-Yu/{file_name}"
    try:
        os.mkdir(path)
        print( f"{file_name} Folder Created in {path}")
    except FileExistsError:
        print("Folder %s already exists" % path)
#function to create multiple files
def mulitple_create_files(file_name, file_number):
    path = f"../100-Days-of-Code-Complete-Python-Pro-by-Angela-Yu/{file_name} {file_number}"
    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
        
        
if __name__ == '__main__':
    get_input()