from Libraa import Library
class Student:
      def requestBook(self):
        print("Enter the title of the book you want to get issued.")
        self.book=input()
        return self.book

      def returnBook(self):
        print("Enter the title of the book you would like to return.")
        self.book=input()
        return self.book

