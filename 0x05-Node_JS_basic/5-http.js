const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const { students, csStudents, sweStudents } = await countStudents('database.csv');
      res.write('This is the list of our students:\n');
      res.write(`Number of students: ${students.length}\n`);
      res.write(`Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}\n`);
      res.write(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}\n`);
      res.end();
    } catch (error) {
      res.end('Error: Cannot load the database');
    }
  } else {
    res.end('404 Not Found');
  }
});

app.listen(port);

module.exports = app;
