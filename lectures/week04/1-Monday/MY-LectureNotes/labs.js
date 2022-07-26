// let firstName = "Dan"
// let lastName = "Kilian"
// console.log(firstName, lastName)

// greeting = `My name is ${firstName} ${lastName}`
// console.log(greeting)


// let a = 14
// let b = 5

// let sum = a + b

// let answer = `the sum of ${a} and ${b} is ${sum}`
// console.log(answer)

// console.log(greeting.indexOf())
// console.log()
// console.log(4 == '4')



// let num1=3
// let num2=5

// if (num1 > num2){
//     console.log(`${num1} is greater than ${num2}`)
// }else if (num1 < num2){
//     console.log(`${num1} is less than ${num2}`)
// }else{
//     console.log(`${num1} and ${num2} are equal`)
// }

// let fruit ='papayas'

// switch(fruit){
//     case 'oranges':
//         console.log('oranges are .50 cents per pound')
//         break
//     case 'papayas':
//         console.log('papayas are .50 cents per pound')
//         break
// }
// let month = 9
// if (
//     month === 1 ||
//     month === 3 ||
//     month === 5 ||
//     month === 7 ||
//     month === 8 ||
//     month === 10 ||
//     month === 12
//   ) {
//     alert("This month has 31 days");
//   } else if (month === 4 || month === 6 || month === 9 || month === 11) {
//     alert("This month has 30 days");
//   } else if (month === 2) {
//     alert("This month has 28 days");
//   } else {
//     alert("Unknown month!");
//   }


// let month = 3


// switch(month){
//     case 2:
//         console.log("This month has  28 days")
//         break
//     case 1:
//     case 3:
//     case 5:
//     case 7:
//     case 8:
//     case 10:
//     case 12:
//         console.log("This month has 30 days")
//         break
//     case 4:
//     case 6:
//     case 9:
//     case 11:
//         console.log("this month has 31 days")
//         break
//     default:
//         console.log("you think THAT is a month? Peh!")
// }

// count = 0
// while (count < 20){
//     if (count%2==0){
//         console.log(count)
//     }
//     count++
// }


// for (let index = 0; index <21;index++){
//     if (index%2 == 0){
//         console.log(index)
//     }
// }


// for (let count = 1; count<=30; count++){
//     console.log(count)
//     if(count%3==0){
//         console.log('fizz')
//     }
//     if(count%5==0){
//         console.log('buzz')
//     }
// }

// let arr = [32, 4, 22, 41, 7]

// arr[1] = 6

// // arr = [32, 4, 22, 41, 7]

// arr.push(5)//Adds and element to the end of the array

// // arr = [ 32, 6, 22, 41, 7, 5 ]

// arr.pop() //Removes element from the end of the array
// // arr = [ 32, 6, 22, 41, 7 ]

// arr.shift() //Removes element from beginning of the array
// // arr = [ 6, 22, 41, 7 ]

// arr.unshift(2) //Adds an element to the beginning of the array
// // arr = [ 2, 6, 22, 41, 7 ]


// //splice(index to begin with, number of indexes)
// arr.splice(1,2) //removed '6' and '22', which is 1 index to begin with and 2 indexes. If only one parameter is given, it will just remove all indexes before the given parameter. 
// // arr=[ 2, 41, 7 ]
// console.log(arr)

// arr.splice(2)

// console.log(arr.slice(1))//removes the indexes within the range. if there is one paramater, it will start with that index and copy the rest. This will not affect the 'arr' variable. Rather, this is like creating a state. 
// console.log(arr)

// name = "Daniel"

// let newName = name.split('')
// console.log(newName)
// let newestName = newName.join('')
// console.log(newestName)


// var lottoNums = [23, 11, 43, 19, 37, 16];
// var arrayOfSplicedValues = 
// lottoNums.splice(2);
// console.log(arrayOfSplicedValues);

// Given a string change the every second letter to an uppercase ‘Z’.
// Assume there are no spaces.

let str1 = "javascript";

// Example output:
// jZvZsZrZpZ OR each letter on a new line
// HINT: You can use  if((i+1) % 2 == 0) to check for even indexes



for (let i=0;i<str1.length; i+=1){
    
    if((i) % 2 == 0){
        console.log(str1[i])
    }else{
        console.log('Z')
    }
}