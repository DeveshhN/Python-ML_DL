import os

def main():
    ret = os.path.exists("Demo.txt")

    if (ret == True):
        print("File is present in current directory")
    else:
        print("Doesnot exist in directory")

if __name__ == "__main__":
    main()