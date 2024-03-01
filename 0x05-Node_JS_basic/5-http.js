const http = require('http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = 1245;

function countStudents(fileName) {
  return new Promise((resolve, reject) => {
    fs.readFile(fileName, (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const students = {};
        const fields = {};
        let length = 0;
        const lines = data.toString().trim().split('\n');

        lines.forEach((line) => {
          const [firstname, , , field] = line.split(',');
          if (firstname && field) {
            length += 1;
            students[field] = students[field] || [];
            students[field].push(firstname);
            fields[field] = (fields[field] || 0) + 1;
          }
        });

        const output = Object.entries(fields)
          .filter(([key]) => key !== 'field')
          .map(([key, value]) => `Number of students in ${key}: ${value}. List: ${students[key].join(', ')}`)
          .join('\n');

        resolve(`Number of students: ${length}\n${output}`);
      }
    });
  });
}

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.end('Hello Holberton School!\n');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(process.argv[2].toString())
      .then((output) => res.end(output))
      .catch(() => {
        res.statusCode = 404;
        res.end('Cannot load the database\n');
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found\n');
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
