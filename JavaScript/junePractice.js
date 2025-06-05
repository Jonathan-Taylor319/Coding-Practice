// // use Map() to double each number in an array

// // Input
// const nums = [1, 2, 3, 4];

// // Expected output: [2, 4, 6, 8]
// function doubleNumbers(arr) {
//     const result = []

//     for (let i=0; i < arr.length; i++) {
//         result.push(arr[i] * 2);
//     }

//     return result
// }

// console.log(doubleNumbers(nums))

// reverse a string in JS

let word = "hello"
let word2 = 'goodbye'

// // declare a function
// function wordReverser(str) {
//     // create an empty variable to hold the reversed string
//     let wordReversed = ''
//     //for loop / go backwords the length of the str; till i greater than or equal to 0; count down
//     for (let i = str.length - 1; i >= 0; i--) {
//         // add current letter during loop to our holder var
//         wordReversed += str[i] 
//     }
//     // return our var 
//     return wordReversed
// }

// refractored 

// function wordReverser(str) {
//     // return split the string up . reverse everything . join together
//     return str.split('').reverse().join('')
// }

// str.split(''): turns the string into an array of characters
// e.g. "hello" → ['h', 'e', 'l', 'l', 'o']

// .reverse(): reverses that array
// → ['o', 'l', 'l', 'e', 'h']

// .join(''): joins the array back into a string
// → "olleh"

// console.log(wordReverser(word))
// console.log(wordReverser(word2))

// JS usses arrays / python uses lists
// numSet1 = [1, 2, 3]
// numSet2 = [4, 5, 6]

// function numDoubler(number) {
//     // create a holder array
//     let doubledNums = []
//     //for loop (i = 0; as long as i is less than the legnth; increment up)
//     for (let i = 0; i < number.length; i++) {
//         // push = put the number at the end (current number * 2)
//         doubledNums.push(number[i] * 2)
//     }
//     // return the new array
//     return doubledNums
// }

// 🔍 What is .map()?
// .map() is a built-in JavaScript array method that:

// Creates a new array by applying a function to each element of the original array.

// const nums = [1, 2, 3];

// const doubled = nums.map(num => num * 2);

// console.log(doubled); // [2, 4, 6]
// declare a function


// function numDoubler(number) {
//     // return 
//     return number.map(num => num * 2)
// }


// console.log(numDoubler(numSet1))
// console.log(numDoubler(numSet2))

// numSet1 = [1, 2, 3]
// numSet2 = [4, 5, 6]

// // new var doubled = take array.map(each number = number * 2)
// const doubled = numSet1.map(num => num * 2)
// const doubled2 = numSet2.map(num => num * 2)

// console.log(doubled)
// console.log(doubled2)

// const scores = [70, 85, 90]

// let updatedScores = scores.map(score => score + 10)

// console.log(updatedScores)

// 🟦 Challenge: addToEach Function
// Goal:
// Write a function addToEach that takes two arguments:

// an array of numbers

// a number to add to each item

// Then return a new array using .map().

// function addToEach(arr, numToAdd) {
//     return arr.map(num => num + numToAdd)
// }

// console.log(addToEach([1, 2, 3], 5)); 
// // Expected Output: [6, 7, 8]


