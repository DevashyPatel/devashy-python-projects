#Author : Devashy Patel
#Date : 6/7/2025

class Library:
    def __init__(self,*booknames):
        self.N = len(booknames)
        self.Books = list(booknames)


    def show(self):
         print("The number of books:", self.N)
         print("The names of books:", self.Books)
    def add(self, book):
        self.Books.append(book)
        self.N +=1
        self.show()
    def remove(self,book):
        self.Books.remove(book)
        self.N -=1
        self.show()

#Testing
# lib = Library("Cake","bake")
# lib.show()
# lib.remove("Cake")
# lib.add("pirates of the crribian")
