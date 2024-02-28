process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Create an event listener for stdin data
process.stdin.on('readable', () => {
  const inputData = process.stdin.read();

  // Display the input back to the user
  if (inputData !== null) {
    process.stdout.write(`Your name is: ${inputData}\n`);
  }
});

// Create an event listener for the end
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
