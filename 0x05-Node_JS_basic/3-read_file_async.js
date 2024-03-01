const fs = require('fs');

/**
 * Asynchronously counts the number of students in each field from a CSV file.
 * @param {string} path - The path to the CSV file.
 * @returns {Promise<void>} - A promise that resolves if the operation is successful and rejects
 *                            with an error if the database cannot be loaded.
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    // Read the CSV file asynchronously
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        // If there's an error reading the file, reject the promise with an error message
        reject(Error('Cannot load the database'));
      } else {
        // Split the file data into lines
        const lines = data.split('\n');
        let length = 0;
        const students = {}; // Object to store students by field
        const fields = {}; // Object to store count of students in each field

        // Iterate through each line of the CSV file
        for (const line of lines) {
          if (line) { // Ignore empty lines
            const student = line.split(',');
            length += 1; // Increment total student count

            // Update count of students in each field
            if (!fields[student[3]]) {
              fields[student[3]] = 1;
            } else {
              fields[student[3]] += 1;
            }

            // Store student names by field
            if (!students[student[3]]) {
              students[student[3]] = [student[0]];
            } else {
              students[student[3]].push(student[0]);
            }
          }
        }
        length -= 1; // Adjust total count for header row

        // Log the total number of students
        console.log(`Number of students: ${length}`);

        // Log the count of students and their names by field
        for (const field in fields) {
          if (Object.prototype.hasOwnProperty.call(fields, field)) {
            if (field !== 'field') { // Skip the header row
              console.log(`Number of students in ${field}: ${fields[field]}. List: ${students[field].join(', ')}`);
            }
          }
        }
        resolve(); // Resolve the promise after processing
      }
    });
  });
}

module.exports = countStudents;
