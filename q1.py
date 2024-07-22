def CountSubArray( st , pat ) :

    NumOcc = st.count( pat )

    return NumOcc

def CountArrayWF( st , pat ) :
    m = len(st)
    
    n = len(pat)

    count = 0

    for i in range(m - n + 1):

        j = 0

        while j < n :

            if st[i + j]!= pat[j] : break

            j += 1

        if(j==n) : count += 1
        
    return count

str = input("Please Enter The String : ")

pattern = input("Please Enter The Pattern : ")

ans = CountSubArray( str , pattern )
ans1 = CountArrayWF( str , pattern )

print(f"The Number Of Times Pattern '{pattern}' was found is : {ans} ")
print(f"The Number Of Times Pattern '{pattern}' was found is : {ans1} ")

