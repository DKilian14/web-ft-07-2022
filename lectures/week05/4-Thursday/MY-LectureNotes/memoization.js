
// SMALL EXAMPLE OF MEMOIZATION


// const uniqSort = function(arr){
//     const cache = {};
//     let results = []
//     for(let i = 0;i<arr.length;i++){  
//         if (cache[arr[i]]) {
//         }else{
//             results.push(arr[i]) 
//             cache[arr[i]] = arr[i]
//         }
//     }

    
//     return results.sort((a,b)=>a-b)//this just takes the array of numbers and sorts them smallest to highest
      
// }

// console.log(uniqSort([4,2,2,3,2,2]))



const fib = (n) =>{
    const cache = []
    for(let i=0;i<n;i++){
        if (i==0 || i==1){
            cache[i] = i
        }else{
            cache[i] = cache[i-1] + cache[i-2]
        }

    }
    return cache[cache.length-1]


}


console.log(fib(500))