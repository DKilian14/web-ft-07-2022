// if the number is 5:
// fibbonacci index 5 is fibbonacci index 4 and fibonnaci index 3
// if the number is 4:
// fibbonacci index 4 is fibbonacci index 3 and fibonnaci index 2
// if the number is 3:
// fibbonacci index 3 is fibbonacci index 2 and fibonnaci index 1
// if the number is 2:
// fibbonacci index 2 is fibbonacci index 1 and fibonnaci index 0 
// if the number is 1:
// fibbonacci index 1 is fibbonacci index 0 and fibonnaci index ...nonexistant.
//fibbonacci index 1 is 1
//fibbonacci index 0 is 0


// const findFib = (n) => {
//     if (n<2){
//         // the index of the fib sequence is the same as the fib number
//         return n
//     }else{
//         return findFib(n-1)+ findFib(n-2)
//     }
// }


// console.log(findFib(10))


// your solution should look like: {sitting:3, standing: 2}

var desks = [ { type: 'sitting' }, { type: 'standing' }, { type: 'sitting' }, { type: 'sitting' }, { type: 'standing' } ];

var deskTypes = desks.reduce(function(prev,desk) {
    desk.type == 'sitting'? prev.sitting +=1 : prev.standing +=1;
    return prev
    
}, { sitting: 0, standing: 0 });

console.log(deskTypes)