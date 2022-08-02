from Libraa import Library
from User1 import Student
from datetime import datetime

class Librarian():
    def datess(self):
        str_d1 = input("Please enter the date you are issuing this book on.")
        str_d2 = input("Please enter the date you are returning this book on.")
        d1 = datetime.strptime(str_d1, "%Y/%m/%d")
        d2 = datetime.strptime(str_d2, "%Y/%m/%d") 
        diff = str(d2 - d1)
        diff = int(diff.split(" ")[0])
        return diff

def main():            
      library=Library(["Ikigai","The Alchmist","Code in Python","Sapiens","Learn C++","The Compound Effect"])
      student=Student()
      librarian=Librarian()
      done=False
      while done==False:
            print(""" Welcome to Webllisto Library
                  1. Look at the list of available books.
                  2. Lend a book.
                  3. Return a book.
                  4. Calculate the charges
                  5. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                library.displayAvailablebooks()
            elif choice==2:
                library.lendBook(student.requestBook())
            elif choice==3:
                library.addBook(student.returnBook())
            elif choice==4:
                library.charge(librarian.datess())    
            elif choice==5:
                print("Thank you. Visit Again")
                exit()
                  
main()