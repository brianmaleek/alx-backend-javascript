export default function createInt8TypedArray(length, position, value) {
  // Check if length, position, and value are all numbers
  if (typeof length !== 'number' || typeof position !== 'number' || typeof value !== 'number') {
    throw new Error('Length, position and value must be numbers');
  }

  // Check if specified position is within valid range
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Create new ArrayBuffer with the specified length, then create a DataView to access it
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);

  // Setting the Int8 value at the specified position
  view.setInt8(position, value);

  // Return the dataview
  return view;
}
