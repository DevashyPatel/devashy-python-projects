def fibonnaci(n):
    if n < 2:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)
n= int(input("Enter the number of terms to calculate Fibonnaci series term: "))
print(fibonnaci(n))