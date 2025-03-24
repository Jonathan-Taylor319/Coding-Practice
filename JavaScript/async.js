/*
 javascript is single - threaded...meaning it can only execute one operation at a time
 ap calls take awhile to complete --- instead of waiting will handle them asynchronously

     callbacks - the original method - using functions to passed into async operations
     promises - objects representing a future value that help manage async flows
     async/await a syntax build on promises hatmakes code easier to read/maintain

 2 --- what are promises ?
     a promise presents the eventual completion (or failure) of an asynchronous operation.
    instead of nesting callbacks, you chain actions with .then() and handle erros with .catch()

  ------Below is valid but messy with multiple async functions -----------

    fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));



 3 Async / Await for cleaner code
 -- the async function always returns a promise. The "await" keyword pauses the execution untill
 the promise is resolved, making your code appear synchronous.

 -- key points --
    - async function - declared with the "async" keyword
    - await - can only be used inside an async function  and waits for a promise to resolve


4. -------- Writing an Async API call --------

async function fetchData() {
    try {
    // wait for the fetch call to complete 
    const response = await fetch('https://api.example.com/data')
    
    //then check if response was succeddful if not catch the error
    if (!resonse.ok) {
        throw new Error(`http error! status: ${response.status}`)
        }
        // parse the JSON from the response
        const data = await response.json()
        //(log data or change to use as needed / set state etc)
        console.log(data)
        } catch (error) {
         // handl errors (network errors, JSON parsing errors, etc.)
         console.error('Error fetching data:', error)
        }
    }

    //call the async function
    fetchData()

breakdown of the code above-----
async function fetchData(): declares a asynchronous function(named fetchData)
await fetch(url): sens the api request and waits for the response
if (!response.ok) checks for HTTP errors (like 404 or 500)
await response.json(): converts the response to JSON
try/catch Block: Catches and handles any errors during the process

5. Practice Exercises
To build confidence, try the following exercises:

Multiple API Calls: Write a function that makes two or more API calls sequentially or concurrently (using Promise.all) and processes their results.

Error Simulation: Intentionally use an incorrect URL to see how your error handling works.

Dynamic API Endpoints: Create a function that takes an API endpoint as a parameter and fetches data accordingly.

UI Integration: If you're working on a web project, integrate your async API calls with UI updates, such as displaying a loading spinner while data is being fetched.

*/

/* ----------------------------------------------------------------

 a simple fetch request 

 fetch("https://jsonplaceholder.typicode.com/posts") -- initiates a GET request to the API
 await response.json() -- Parses the response body as JSON
 Error Handling: the try/catch block catches any errors during the fetch or JSON conversion */

        // async function fetchPosts() {
        //     try {
        //         const response = await fetch("https://jsonplaceholder.typicode.com/posts")

        //         if (!response.ok) {
        //             throw new Error(`HTTP error! status: ${response.status}`)
        //         }

        //         const posts = await response.json()
                
        //         console.log(posts)
            
        //     } catch (error) {
        //         console.error("Error fetching posts:", error)
        //         }
        //     }

        //    fetchPosts()

// Next pracitce is to only pull one post and log the title and body

        // async function fetchOnePost() {
        //     try {
        //         const response = await fetch("http://jsonplaceholder.typicode.com/posts/1")

        //         if (!response.ok) {
        //             throw new Error(`HTTP errror! status: ${responst.status}`)
        //         }
        //         const post1 = await response.json()
        //         console.log("this is the title:", post1.title)
        //         console.log("this is the body:", post1.body)
        //     } catch (error) {
        //         console.error("Error fetching posts:", error)
        //     }
        // }

        // fetchOnePost()


// ----------------------- working on POST / PATCH / DELETE ================================

