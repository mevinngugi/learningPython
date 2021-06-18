""" Task
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 
space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Example:
s = adbecf 

Print: abc def

Constraints

1<= T <= 10
2<= length of S <= 10000

Sample Input

2
Hacker
Rank

Sample Output

Hce akr
Rn ak
 """

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
if 1<= T <= 10:
    countInput = 0
    while countInput != T:
        mystring = str(input())
        if 2 <= len(mystring) <=10000: 
            even = []
            odd = []
            for i, val in enumerate(mystring):
                if i == 0:
                    even.append(val)
                elif i % 2 == 0:            
                    even.append(val)
                else:
                    odd.append(val)
            #evenString = ""
            #oddString = ""
            print(''.join(even), ''.join(odd))
            countInput += 1
        else:
            print("Too short")
else:
    print("Test cases number input should be between 1 and 10") 
