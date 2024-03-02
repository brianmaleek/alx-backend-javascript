// api.js
// Create a simple express server
const express = require('express');

// Create the express app
const app = express();
// Define the port
const port = 7865;

// Define the / route
app.get('/', (req, res) => {
  // Send the response
  res.end('Welcome to the payment system');
});

// Start the server, listening on defined port
app.listen(port, () => {
  // Log the server is running and listening to the port
  console.log(`API available on localhost port ${port}`);
});
