let arr1 = [[3,2],[1,1,4,6],[3,4,2]]
let arr2 = [[3,2,3,3,3,3,3,3,],[1,1,4,6],[3,400,2]]
let arr3 = [[],2,[]]
let arr4 = [[1],[2],[3],[4],[5],[6]]
let arr5 = [[6],[5],[4],[3],[2],[1]]
let arr6= [[0,0,0,0],[0],[0,0],[00],[0,0],[0]] //Interesting behavior

function sortLittleArrays(arr){
    for (let i = 0; i< arr.length; i++){
        let current_little_array = arr[i]
        let min_sum_index = i
        let min_sum = 0
    
        for(let k=0;k<arr[i].length; k++){
            min_sum +=arr[i][k]
        }
    
    
        let min_sum_arr = []
        for (let j = i; j<arr.length; j++){
            let sum = 0
    
            for (let q=0;q<arr[j].length;q++){
                sum+=arr[j][q]
            }
            // the < || sum == !true > assumes that an empty nested array is equal to zero.
            if (sum < min_sum || sum == !true){
                min_sum_arr = arr[j]
                min_sum_index = j
            }  
        }
        arr[i] = min_sum_arr
        arr[min_sum_index] = current_little_array
    }
    console.log(arr)
}


sortLittleArrays(arr1)
sortLittleArrays(arr2)
sortLittleArrays(arr3)
sortLittleArrays(arr4)
sortLittleArrays(arr5)
sortLittleArrays(arr6)