process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Create an event listener for stdin data
process.stdin.on('readable', () => {
  const inputData = process.stdin.read();
  if (inputData !== null) {
    // Display the input back to the user
    process.stdout.write(`Your name is: ${inputData.toString().trim()}\n`);
  }
});

// If stdin is not connected to a terminal, handle process exit event
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
