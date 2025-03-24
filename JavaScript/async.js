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

// POST - used to create new data on the server 
// PATCH - request partial updates on the server
// DELETE - removes data from the server

// need to add in method and headers to our request -- continue using json -- moodify as needed

// ---------------- POST -------------------------------
   
//   async function createPost() {
    //     try {
    //       const respsonse = await fetch("https://jsonplaceholder.typicode.com/posts" , {
    //         // declare what kind of request
    //         method: "POST" ,
    //         headers: {
    //           // tell the server we're sending JSON
    //           "Content-Type": "application/json"
    //         },
    //         // convert the JavaScript object to JSON string
    //         body: JSON.stringify({
    //           title: "foo",
    //           body: "bar",
    //           userID: 1
    //         }) 
    //       })

    //     if (!respsonse.ok) {
    //       throw new Error(`HTTP error! status: ${Response.status}`)
    //     }

    //     const newPost = await respsonse.json()
    //     console.log("Post created:", newPost)
    //     } catch (error) {
    //       console.error("Error creating post:", error)
    //     }
    //   }

    // createPost()

// ------------------- PATCH ----------------------

    //   async function updatePost() {
    //     // Data for the update (only including the field(s) you want to change)
    //     const patchData = {
    //       title: 'Foo to the BAR'
    //     }

    //     try {
    //       const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
    //         // Tell server we are PATCHing
    //         method: 'PATCH',
    //         headers: {
    //           'Content-type': 'application/json'
    //         },
    //         //convert JavaScript object to JSON string
    //         body: JSON.stringify(patchData)
    //       })
    //       // parse the JSON response 
    //       const updatedPost = await response.json()
    //       console.log('Post Updated:', updatedPost)
    //     } catch (error) {
    //       console.error('Error updating post:', error)
    //     }
    //   }

    // updatePost()


//------------------DELETE---------------------

    // async function deletePost() {
    //   try {
    //     const response = await fetch('https://jsonplaceholder.typicode.com/posts/1', {
    //       // Tell server to DELETE
    //       method: 'DELETE'
    //     }) 

    //   if (response.ok) {
    //     console.log('Post deleted successfully.')
    //   } else {
    //     console.error('Failed to delete post. Status:' , response.status)
    //   }
    //   } catch (error) {
    //     console.error('Error deleting post:', error)
    //   }
    // }

    // deletePost()

    /*------------------OTHER HEADERS AND BODY CONSIDERATIONS---------------------
    Common Headers:
    Content-Type: Indicates the format of the request body. For JSON data, use 'application/json'.
    
    Accept: Specifies the type of responses your client can handle (e.g., 'application/json').
    
    Authorization: Carries the token for secured endpoints.
    
    Custom Headers: Some APIs might require additional headers such as X-API-Key, X-CSRF-Token, or other custom fields.
    
    Request Body:
    JSON Data: When sending data (e.g., in POST or PATCH requests), you usually format it as a JSON string.
    
    Form Data: For some endpoints, you might need to use form data instead of JSON.
    
    Additional Fields: Depending on the API, your body may need extra metadata or parameters. Always refer to the API’s documentation for the exact requirements. */