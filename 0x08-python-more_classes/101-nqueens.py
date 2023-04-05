
#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

   a = []


   if len(argv) != 2:


       print("Usage: nqueens N")
       exit(1)
   if argv[1].isdigit() is False:
       print("N must be a number")
       exit(1)
   n = int(argv[1])
   if n < 4:
       print("N must be at least 4")
       exit(1)
   # initialize the answer list
   for i in range(n):
       a.append([i, None])
   def already_exists(y):
       """check that a queen does not already exist in that y value"""
       for x in range(n):
           if y == a[x][1]:
               return True
       return False

   def reject(a, b):

       """determines whether or not to reject the solution"""

       if (already_exists(b)):
	       return False

       i = 0
       while(i < a):
           if abs(x[i][1] - b) == abs(i - a):
		return False

           i += 1

       return True
   def clear_x(a):
       for i in range(a, n):
           x[i][1] = None

   def nqueens(a):
       for b in range(n):

           clear_x(a)

           if reject(a, b):

               x[a][1] = b

               if (a == n - 1):  # accepts the solution
                   print(x)

               else:
                   nqueens(a + 1)  # moves on to next a value to continue
   # start the recursive process at a = 0

   nqueens(0)
