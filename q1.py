def CountSubArray( st , pat ) :

    NumOcc = st.count( pat )                #using the inbuilt function to get the number of occurrences

    return NumOcc

def CountArrayWF( st , pat ) :
    m = len(st)
    
    n = len(pat)

    count = 0

    for i in range(m - n + 1):              # moving the pattern window over the original string

        j = 0

        while j < n :                       #comparing window with original string

            if st[i + j]!= pat[j] : break   #if failed skip the window 

            j += 1

        if(j==n) : count += 1               #check if the window is equal to the pattern length
        
    return count

str = input("Please Enter The String : ")

pattern = input("Please Enter The Pattern : ")

ans = CountSubArray( str , pattern )
ans1 = CountArrayWF( str , pattern )

print(f"The Number Of Times Pattern '{pattern}' was found is : {ans} ")
print(f"The Number Of Times Pattern '{pattern}' was found is : {ans1} ")

