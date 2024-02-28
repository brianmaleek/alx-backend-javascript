// Import the express module
const express = require('express');

// Create an instance of express
const app = express();

// Define a route for the endpoint '/'
app.get('/', (req, res) => {
  // Send 'Hello Holberton School!' as the response
  res.send('Hello Holberton School!');
});

// Start the server and listen on port 1245
const port = 1245;
app.listen(port, () => {});

// Export the app variable
module.exports = app;
