const http = require('http');
const students = require('./3-read_file_async'); // Import the function to read student data asynchronously

const hostname = '127.0.0.1';
const port = 1245;

/**
 * Create an HTTP server to handle requests.
 */
const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  // Handle root path
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  // Handle /students path
  if (req.url === '/students') {
    // Write response header
    res.write('This is the list of our students\n');
    // Read student data asynchronously
    students(process.argv[2]).then((data) => {
      // Write the number of students and their names in CS field
      res.write(`Number of students: ${data.students.length}\n`);
      res.write(`Number of students in CS: ${data.csStudents.length}. List: ${data.csStudents.join(', ')}\n`);
      // Write the number of students and their names in SWE field
      res.write(`Number of students in SWE: ${data.sweStudents.length}. List: ${data.sweStudents.join(', ')}`);
      res.end(); // End response
    }).catch((err) => res.end(err.message)); // Handle errors
  }
});

// Start the server to listen on the specified hostname and port
app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}`);
});

module.exports = app; // Export the app for testing or use in other modules
