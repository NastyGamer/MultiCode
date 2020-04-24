import sys, List, Create, Delete, Run


if(__name__ == "__main__"):
    if(len(sys.argv) == 1):
        print("Invalid argument. Available arguments are:\n-run\n-list\n-create\n-delete")
        exit(0)
    if(sys.argv[1] == "list"):
        List.listInstances()
    elif(sys.argv[1] == "create"):
        Create.createInstance()
    elif(sys.argv[1] == "delete"):
       Delete.deleteInstance()
    elif(sys.argv[1] == "run"):
        #Open JSON
        #Get appropriate folder
        #Start Code
        pass
    else:
        print("Invalid argument. Available arguments are:\n-run\n-list\n-create\n-delete")
