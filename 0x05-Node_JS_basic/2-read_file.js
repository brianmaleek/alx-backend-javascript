const fs = require('fs');

function countStudents(fileName) {
  // Initialize objects to store students and fields counts
  const students = {};
  const fields = {};
  let length = 0; // Variable to count the total number of students

  try {
    // Read the content of the file synchronously
    const fileContent = fs.readFileSync(fileName, 'utf-8');

    // Split the content into lines
    const lines = fileContent.toString().split('\n');

    // Iterate over each line
    for (let i = 0; i < lines.length; i += 1) {
      // Check if the line is not empty
      if (lines[i]) {
        // Increment the total number of students
        length += 1;

        // Split the line into fields
        const field = lines[i].toString().split(',');

        // Update the students object with the current field
        if (Object.prototype.hasOwnProperty.call(students, field[3])) {
          students[field[3]].push(field[0]);
        } else {
          students[field[3]] = [field[0]];
        }

        // Update the fields object with the current field
        if (Object.prototype.hasOwnProperty.call(fields, field[3])) {
          fields[field[3]] += 1;
        } else {
          fields[field[3]] = 1;
        }
      }
    }

    // Calculate the total number of students (excluding the header)
    const l = length - 1;

    // Log the total number of students
    console.log(`Number of students: ${l}`);

    // Log the number of students in each field along with their lists of first names
    for (const [key, value] of Object.entries(fields)) {
      // Check if the key is not 'field'
      if (key !== 'field') {
        console.log(`Number of students in ${key}: ${value}. List: ${students[key].join(', ')}`);
      }
    }
  } catch (error) {
    // If an error occurs during file reading, throw an error
    throw Error('Cannot load the database');
  }
}

// Export the countStudents function to be used in other modules
module.exports = countStudents;
