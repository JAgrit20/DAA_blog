def edit(s1, s2, m, n):
    #two base base case 

    #if s1 is empty
    #then total operation will be n to make s1->s2
        
    if(m == 0): 
        return n

    #if s2 is empty
    #then total operation will be m to make s1->s2
    elif(n == 0):
        return m 
        
    #if character at mth position of s1 is equal to the nth position of s2
    #then no operation is required, so answer will be minimum operation
    #required to make s1 with m-1 character = s2 with n-1 characters

    elif(m-1>=0 and n-1 >=0 and s1[m-1] == s2[n-1] ):
        return edit(s1, s2, m-1, n-1)
        
    #if character at mth position of s1 is not equal to the nth position of s2
    #then we can have three cases

    #case 1: insert the element which is at the nth position of s2 to mth position of s1
    #this means total cost =  1(insertion) + minimum operation required to make 
    #s1 with m characters = s2 with n-1 characters

    #case 2: replace element at mth position of s1 by element at nth position of s2
    #this means total cost =  1(replace) + minimum operation required to make 
    #s1 with m-1 character = s2 with n-1 characters

    #case 3: delete element at the mth position of s1
    #this means total cost =  1(deletion) + minimum operation required to make 
    #s1 with m-1 character = s2 with n characters
    
    elif(m-1>=0 and n-1 >=0 and s1[m-1] != s2[n-1]):
        return 1 + min(edit(s1, s2, m, n-1), edit(s1, s2, m-1, n-1), edit(s1, s2, m, n-1))
    
print(edit("geek", "gesek", 4, 5))