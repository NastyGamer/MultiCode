import sys, List, Create, Delete, Run
from colorama import init, Fore, Style


if(__name__ == "__main__"):
    init()
    if(len(sys.argv) == 1):
        print(Fore.RED + "Invalid argument. Available arguments are:\n-run\n-list\n-create\n-delete" + Style.RESET_ALL)
        exit(0)
    if(sys.argv[1] == "list"):
        List.listInstances()
    elif(sys.argv[1] == "create"):
        Create.createInstance()
    elif(sys.argv[1] == "delete"):
       Delete.deleteInstance()
    elif(sys.argv[1] == "run"):
        Run.runInstance()
        pass
    else:
        print(Fore.RED + "Invalid argument. Available arguments are:\n-run\n-list\n-create\n-delete" + Style.RESET_ALL)
