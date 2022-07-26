// Selection sort moves the smallest value to the front of the Array. 

// const arr = [34,22,10,19,17]



// for (let current_index = 0 ; current_index < arr.length ; current_index+=1){
//     let min = current_index
//     for (let index_to_check = current_index ; index_to_check < arr.length ; index_to_check+=1){
//         console.log(`I am on index ${current_index}, currently checking to see if ${arr[current_index]} is greater than ${arr[index_to_check]}`)
//         if (arr[min] > arr[index_to_check]){
//             console.log(`${arr[current_index]} is greater than ${arr[index_to_check]}`)
            
//             min = index_to_check
//             console.log(`Smallest number is now ${arr[min]} at index ${min}`)
//         }
//     }
//     console.log(`after looking at all the remaining unsorted list, ${arr[min]} is the smallest number`)  
//     smallest = arr[min] 
//     current = arr[current_index]
//     arr[current_index] = smallest
//     arr[min] = current
// }
// console.log(arr)


arr = [34,22,10,19,17]






function selectionSort(list){
    for (let i = 0; i< list.length;i+=1){
        let index_of_smallest = i
        for(let j = i+1; j< list.length; j+=1){
            if (list[index_of_smallest]> list[j]){
                index_of_smallest = j
            }
        }
        smallestValue = list[index_of_smallest]
        list[index_of_smallest] = list[i]
        list[i]= smallestValue 
    }
    return list
}

console.log(selectionSort(arr))