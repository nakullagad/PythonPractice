#Read directory path and list all its content

import os

req_path= input(" Enter Directory path: ")

if os.path.isfile(req_path):
    print("This is a file path.Please enter directory path")

else:
    all_fi_di= os.listdir(req_path)
    print(f"This directory contains: {all_fi_di})

    req_ext= input("Please give required ext from this directory: ")
#joining req-path and all_fi_di---
          
    for each_file in all_fi_di:
        joining_both= os.path.join(req_path,each_file)
        
        if joining_both.isfile:
          print(f"This is a file is with ext : {req_ext}")

        else:
            print("This is a directory")
            
