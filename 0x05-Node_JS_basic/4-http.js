const http = require('http');

// Create HTTP server
const app = http.createServer((_, res) => {
  // Set the response HTTP header with HTTP status and Content type
  res.statusCode = 200;
  // Send response headers
  res.setHeader('Content-Type', 'text/plain');
  // Send response body
  res.end('Hello Holberton School!\n');
});

// Listen on port 1245
const port = 1245;
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

// Export the app
module.exports = app;
