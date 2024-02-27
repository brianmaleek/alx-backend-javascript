const http = require('http');

// Define the hostname and port
const hostname = '127.0.0.1';
const port = 1245;

// Create HTTP server
const app = http.createServer((req, res) => {
  // Set the response HTTP header with HTTP status and Content type
  res.statusCode = 200;
  // Send response headers
  res.setHeader('Content-Type', 'text/plain');
  // Send response body
  res.end('Hello Holberton School!\n');
});

// Make the server listen on port 1245
app.listen(port, hostname, () => {});

// Export the app
module.exports = app;
