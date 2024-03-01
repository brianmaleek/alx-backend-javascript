const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
      } else {
        const lines = data.trim().split('\n');
        let length = 0;
        const students = {};
        const fields = {};

        for (const line of lines) {
          const student = line.split(',');
          if (student.length === 4) { // Ensure the line has all fields
            length += 1;
            const field = student[3];
            if (!fields[field]) {
              fields[field] = 1;
            } else {
              fields[field] += 1;
            }
            if (!students[field]) {
              students[field] = [student[0]];
            } else {
              students[field].push(student[0]);
            }
          }
        }

        console.log(`Number of students: ${length}`);

        for (const field in fields) {
          if (Object.prototype.hasOwnProperty.call(fields, field)) {
            console.log(`Number of students in ${field}: ${fields[field]}. List: ${students[field].join(', ')}`);
          }
        }

        resolve();
      }
    });
  });
}

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!\n');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    countStudents('database.csv')
      .then(() => {
        console.log('Students count successfully displayed.');
        res.end(); // Ending the response here as we've already logged the students' count
      })
      .catch((error) => {
        console.error(error.message);
        res.end('Error: Cannot load the database');
      });
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found\n');
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
