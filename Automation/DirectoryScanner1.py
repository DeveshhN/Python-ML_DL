import sys
import os

def DirectoryScanner(DirectoryPath):
    
    print("Files from Directory are : ")

    for FolderName , SubFolder , FileName in os.walk(DirectoryPath):
        for fname in FileName:
            print(fname)


def main():
    Border = "-"*51
    print(Border)
    print("Marvellous Automation Scrip")
    print(Border)

    if(len(sys.argv) ==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is used to travel the directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("Directory name should be Absolute Path")

        else:
            DirectoryScanner(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Please us --h or --u for more information")
    
    print(Border)
    print("Thank You for using Marvellous Automation Scrip")
    print(Border)
    

if __name__ == "__main__":
    main()