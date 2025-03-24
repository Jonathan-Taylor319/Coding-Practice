// declare and name our function
function createCounter() {
    //created a var to hold our number (local scope, stays in function only)
    let counter = 0
    // return a function that has access (within scope)
    return function() {
    //increment our var by 1
      counter ++
    // return our updated var
      return counter
    }
  }

// turned in to a fat arrow function
// top line declares constant var that holds a function
//  = () => {} (this is an arrow fucntion no params will return another function)
const createCounterFat = () => {
  // declare a local var inside 'createCounterFat' (scope) will only persist till closure
  let counter = 0
  // return () => this means create counter returns a new function
  // ++counter -- increments counter before returning it 
  return () => ++ counter
}

  //create new outside scope var that runs function
  const counter1 = createCounter()
  const sample1 = createCounterFat()
  // create another separate var that runs as it own
  const counter2 = createCounter()
  
  //use node.js to run in vs code terminal
  console.log(counter1())
  console.log(counter1())
  console.log(counter2())
  console.log(counter2())
  console.log(counter2())
  console.log(counter1())
  console.log(sample1())
  console.log(sample1())
  console.log(sample1())
  console.log(sample1())
  console.log(sample1())


// ✔ A closure is when a function "remembers" its outer variables even after the outer function has finished running.
// ✔ Returning a function creates a closure, which keeps access to its original variables.
// ✔ Each new instance of createCounter() creates a new, independent closure.
  