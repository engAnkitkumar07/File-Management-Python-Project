import os
from fileinput import filename
from os import write
from random import choice


def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"filename{filename}:created succesfully")
    except FileExistsError:
        print(f"This File {filename} Already Exists")
    except Exception as E:
        print("An Error Occured")

#For Viewing All Files ->>>>>>>>>>>>

def view_all_files():
    file=os.listdir()
    if not file:
        print("No Any File Exists")
    else:
        print("File In Directry")
        for files in file:
            print(file)
#For Deleting all Files from the Directry-->>>>>>>
def delete_file(filename):
    try:
        os.remove(filename) #function for removing passed file as a parameter
        print(f"file has been deleted")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error Occurred ! ")

def read_file(filename):
    try:
        with open("raja.text",'r') as f:
            contect=f.read()
            print(f"content of file {filename} \n  {contect}")
    except FileNotFoundError:
        print(f"File {filename} Is Not Exists")
    except Exception as e:
        print("AN error Ocurred")

def edit_file(filename):
      try:
          with open(filename,'a') as f:
              content=input("Enter A Data for add")
              f.write(content+"\n")
              print(f"Data is add in {content} Succesfully")
      except FileNotFoundError:
          print("File is not exists")
      except Exception as e:
          print("An Error Occured ! ")
def main():
    while True:
        print("FILE MGMT APP->>>")
        print("1--> Create A file Press-1")
        print("1--> View all data A file Press-2")
        print("1--> delete A file Press-3")
        print("1--> Read A file Press-4")
        print("1--> Edit A file content Press-5")
        print("1--> Exit from file to Press-6")

        c=input("Enter A you choice between 1-6")
        if c=="1":
            filename=input("Enter Your Name ")
            create_file(filename)
        elif c=="2":
            view_all_files()
        elif c=="3":
            filename=input("enter your file name")
            delete_file(filename)
        elif c=="4":
            filename = input("enter your file name")
            read_file(filename)
        elif c=="5":
            filename = input("enter your file name")
            edit_file(filename)
        elif c=="6":
            print("closing the connection")
        else:
            print("Enter The right numbers 1-6")

        break




if __name__=="__main__":
    main()
