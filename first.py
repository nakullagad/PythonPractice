#Find all files in directory with extension .py/.sh/.txt



import os

req_path= input("Enter your Path: ")

if os.path.isfile(req_path):
    print("This is not Directory path, please give directory path")

else:
    all_fi_di= os.listdir(req_path)
    if all_fi_di==0:
        Print(" This Directory is empty")

    else:
        req_ext= input(" Please give required extension: ")
        req_storage= []

        for each_file in all_fi_di:
            if each_file.endswith(req_ext):
                req_storage.append(each_file)

        if req_storage==0:
            print(f"There is no {req_ext} file in {req_path})

        else:
            print(f" There are {len(req_storage)} in {req_path} for {req_ext})
