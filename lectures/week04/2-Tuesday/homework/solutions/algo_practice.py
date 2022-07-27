arr = [[3,2],[1,1,4,6],[3,4,2]]
new_arr = []
count=0

# FOR EACH LITTLE ARRAY
for i in arr:
    
    # SAVE THE LITTLE ARRAY VALUE, ASSUME IT IS THE SMALLEST
    min = i
    print(f'lets see if the little array, {i}')
    # FIND THE SUM OF THE LITTLE ARRAY
    min_sum=0
    for j in i:
        min_sum+=j
    
    
    
    # CHECK TO SEE IF IT IS THE SMALLEST OF THE OTHER LITTLE ARRAYS
    
    # get the sum of all the little arrays
    for k in range(len(arr)):
        sum=0
        for q in arr[k]:
            sum+=q
        print(f'sum of {arr[k]} is {sum}')
        # If the sum of i is larger, swap. 
        
        if min_sum > sum:
            print(f'min_sum = {min_sum}')
            i = arr[k]
            print(f'min_sum = {min_sum}')
            arr[k] = min 
            print(f'{min_sum} is more than {sum}')
            
    
        print(f'i = {i}, arr[k] = {arr[k]},')
        print(f'min={min}, min_sum={min_sum}')
        
    
    count= count+1
    print("---------------------------------------------")
    
print(arr)