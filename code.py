def editDistance( s1, s2):# this function will return the final answer
		# Code here
		m = len(s1)# length of s1
		n = len(s2)# length of s2
		global t #global variable t

    # creating a 2D matrix for storing
    # subproblems answer
		t = [[-1 for i in range(n+1)] for j in range(m+1)]
    # calling the main function which will calculate the total min cost
		return edit( s1, s2, m, n)

def edit( s1, s2, m, n):

    # two loops to iterate in the matrix
    for i in range(m+1):
        for j in range(n+1):

            if(i == 0): #if s1 is empty
                t[i][j] = j#then total operation will be j to make s1->s2

            elif(j == 0):#if s2 is empty
                t[i][j] = i #then total operation will be i to make s1->s2

            #if character at ith position of s1 is equal to the jth position of s2
            #then no operation is required so answer will be t[i-1][j-1]
            #that is minimum operation required to make s1 with i-1 character = s2 with j-1 characters
            elif(s1[i - 1] == s2[j-1] ):
                t[i][j] = t[i-1][j-1]

            #if character at ith position of s1 is not equal to the jth position of s2
            #then we can have three cases

            #case 1: insert the element which is at the jth position of s2 to ith position of s1
            #this means total cost =  1(insertion) + minimum operation required to make
            #s1 with i character = s2 with j-1 characters

            #case 2: replace element at ith position of s1 by element at jth position of s2
            #this means total cost =  1(replace) + minimum operation required to make
            #s1 with i-1 character = s2 with j-1 characters

            #case 3: delete element at the ith position of s1
            #this means total cost =  1(deletion) + minimum operation required to make
            #s1 with i-1 character = s2 with j characters

            elif(s1[i-1] != s2[j-1]):
                t[i][j] = min(1+t[i-1][j-1], 1+t[i-1][j], 1+t[i][j-1])

    return t[m][n]# last element of matrix will keep the minimum value to make s1 to s2.


editDistance("geek", "gesek")
