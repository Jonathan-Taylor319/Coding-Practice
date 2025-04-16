/* -------------- Retrieving a TOKEN ----------------

API's commonly provide an endpoint (like /api/token or /auth/login) where you send 
credentials. Although some API's might use a GET request, many require a POST request.
(have to send info to cofirm) */

// this is very general and need to adjust according to url and payload-
    async function getToken() {
        try {
            const response = await fetch('https://example.com/api/token', {
                // declare a method
                method: 'POST',
                headers: {
                    'Content-Type': 'applicartioin/json'
                },
                body: JSON.stringigy({
                    username: 'yourUsername',
                    password: 'yourPassword'
                })
            })
            const data = await response.json()
            // assuming returned JSON has token may need do log and see what's returned
            return data.token
        } catch (error) {
            console.error('Error retrieving token:', error)
        }
    }

// if we had simple react form data in our HTML such as 

        import React, { useState } from 'react';

        function LoginForm() {
        const [token, setToken] = useState(null)
        
        async function getToken(username, password) {
            try {
                const response = await fetch('https://example.com/api/token' , {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            })
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }
            const data = await response.json()
            // check for data
            console.log(data)
            return data.toke
            } catch (error) {
                console.error('Error retrieving token:', error)
            }
        }
    
        const handleSubmit = async (e) => {
            // Prevent the default form submission
            e.preventDefault()

            //Use FormData to extrct values from the form
            const formData = new FormData(e.target)
            const username = formData.get('username')
            const password = formData.get('password')

            // Retrieve the token using the credentials
            const retrievedToken - await getToken(username, password)
            setToken(retrievedToken)
            // only for debugging and building
            console.log('Recived token:', retrievedToken)
        }
        
        return (
            <div>
              <form onSubmit={handleSubmit}>
                <input type="text" name="username" placeholder="Username" required />
                <input type="password" name="password" placeholder="Password" required />
                <button type="submit">Login</button>
              </form>
              {token && <p>Token: {token}</p>}
            </div>
          );
        }
        
    export default LoginForm;
