document.addEventListener('DOMContentLoaded', function () {
    const signInForm = document.querySelector('.sign-in form');
    const signUpForm = document.querySelector('.sign-up form');

    const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});
    // Function to get CSRF token from cookie
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) {
            return parts.pop().split(';').shift();
        }
        return null;
    }

    // Get CSRF token
    
    if(!csrf_token){
        const csrf_token = getCookie('csrftoken');
    }
    if (signInForm) {
        signInForm.addEventListener('submit', function (e) {
            // Prevent the default form submission behavior
            e.preventDefault();

            // Get the form data
            const formData = new FormData(this);

            // Send a POST request to the login endpoint
            fetch('/login/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrf_token // Pass CSRF token in headers
                }
            })
            .then(response => {
                // Check if the response is successful
                if (!response.ok) {
                    throw new Error('Unexpected response from the server');
                }
                // Check if the response is JSON
                const contentType = response.headers.get('content-type');
                if (contentType && contentType.includes('application/json')) {
                    // Parse the JSON response
                    return response.json();
                } else {
                    // Return the HTML response
                    return response.text();
                }
            })
            .then(data => {
                // Check if the data is JSON
                if (typeof data === 'object') {
                    // Check if the login was successful
                    if (data.success) {
                        // Redirect the user to the home page
                        window.location.href = '/home/';
                    } else {
                        // Display an error message from JSON response
                        alert(data.error);
                    }
                } else {
                    // Display HTML response
                    // Handle HTML response based on your requirements
                }
            })
            .catch(error => {
                // Log the error to the console
                console.error('Error:', error);
                // Display a generic error message
                alert('An error occurred while logging in. Please try again later.');
            });
        });
    }
    
    if (signUpForm) {
        signUpForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const formData = new FormData(this);
            fetch('/register/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrf_token // Pass CSRF token in headers
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Unexpected response from the server');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    window.location.href = '/login/';
                } else {
                    alert('Registration failed');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
});
