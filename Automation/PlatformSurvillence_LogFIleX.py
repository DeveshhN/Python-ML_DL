import psutil
import sys
import os
import time

def PlatformSurvillence(FolderName):
    Border = "-"*51
    
    Ret = False
    
    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existing")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for the log file gets created sucessfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    
    fobj = open(FileName , "w")

    print(f"Log file gets sucessfully created with name {FileName}")

def main():
    Border = "-"*51
    print(Border)
    print("-----Marvellous platform survillence system--------")
    print(Border)

#--h and --u Handling
    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h" or sys.argv[1]=="--H"):
            print("This automation script is used to perform ")
            print("1 : It fetch the information of running processess")
            print("2 : It fetch the information about primary storage as the RAM")
            print("3 : It fetch the information about secondary storage as HDD")
            print("4 : It fetch the information about the microprocessor")
            print("5 : It gets autoscheduled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1]=="--U"):
            print("Use the automation script as:")
            print(f"python {sys.argve[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Nmae : ")

        else:
            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for getting more details")

#Actual Project code
    elif(len(sys.argv)==3):
        PlatformSurvillence(sys.argv[2])

    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")


    print(Border)
    print("-----Thank You for using our Automation system-----")
    print(Border)

if __name__ == "__main__":
    main()