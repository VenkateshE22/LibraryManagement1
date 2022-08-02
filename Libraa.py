from datetime import datetime
class Library:
      def __init__(self,list1):
            self.availablebooks=list1

      def displayAvailablebooks(self):
            print("The list of books that are currently available - ")
            for book in self.availablebooks:
                  print(book)
      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you wanted has been issued to you.")
                  self.availablebooks.remove(requestedBook)
                  print("Please enter the date you are issuing this book on.")
                  issue_date = input()
                  return issue_date
            else:
                  print("Sorry. The book you requested is currently unavailable.")
                  
      def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thank you for returning the book.")
            print("Please enter the date you are returning this book on.")
            return_date = input()
            return return_date
      def charge(self,diff):
            if (diff > 5):
                  charge = 50*(diff-5)
                  print(f"Please pay Rs.{charge}")


      
      

            
