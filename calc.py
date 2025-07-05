def calculatespan(price, S):

        n= len(price)
        st= []
        st.append(0)
        
        S[0]= 1
        
        for i in range(1, n):
            while(len(st) > 0 and price[st[-1]] <= price[i]):
                st.pop()
            S[i]= i + 1 if len(st) == 0 else (i - st[-1])
            st.append(i)
            
def printarray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")
        
price= [10, 4, 5, 90, 120 ,50]
S= [0 for in range(len(price)+1)]
calculatespan(price, S)
printarray(S, len(price))

