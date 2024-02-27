process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Create an event listener for stdin data
process.stdin.on('data', (data) => {
  const inputData = data.toString().trim();

  // Display the input back to the user
  process.stdout.write(`Your name is: ${inputData}\n`);

  // If stdin is connected to a terminal, exit after processing input
  if (process.stdin.isTTY) {
    process.exit();
  }
});

// If stdin is not connected to a terminal, handle process exit event
if (!process.stdin.isTTY) {
  process.on('exit', () => {
    process.stdout.write('This important software is now closing\n');
  });
}
