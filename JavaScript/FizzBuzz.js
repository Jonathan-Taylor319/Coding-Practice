/* 
The FizzBuzz Problem
Problem Statement:
Write a program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, for multiples of 5, print "Buzz",
 and for numbers which are multiples of both 3 and 5, print "FizzBuzz".

Steps to consider:

Looping:
Use a loop to iterate through numbers 1 to 100.

Conditionals:
For each number:

Check if it’s divisible by both 3 and 5.

Else, check if it’s divisible by 3.

Else, check if it’s divisible by 5.

Otherwise, print the number.

Output:
Ensure each output is printed on a new line (or with a clear separation). */


/*    function FizzBuzz() {
        for (let i = 0; i <= 100; i++)
            if (i % 15 == 0) {
                console.log("FizzBuzz")
            } else if (i % 5 == 0) {
                console.log("Buzz")
            } else if (i % 3 == 0) {
                console.log("Fizz")
            } else {
                console.log(i) 
            }
    }
*/

// ---------------Trying to Refractor------------------

    function getFizzBuzz(i) {
        if (i % 15 === 0) {
            return "FizzBuzz";
        } else if (i % 5 === 0) {
            return "Buzz";
        } else if (i % 3 === 0) {
            return "Fizz";
        } else {
            return i.toString();
        }
    }
    
    function FizzBuzz() {
        for (let i = 0; i <= 100; i++)
            console.log(getFizzBuzz(i))
    }
FizzBuzz()

