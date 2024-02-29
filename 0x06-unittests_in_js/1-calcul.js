// 1-calcul.js

/**
 * Perform arithmetic operations based on the specified type.
 * @param {string} type - The type of operation: 'SUM', 'SUBTRACT', or 'DIVIDE'.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 * @returns {number|string} - The result of the arithmetic operation or 'Error' if
 *                              division by zero occurs.
 */
function calculateNumber(type, a, b) {
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);

  if (type === 'SUM') {
    return roundedA + roundedB;
  }
  if (type === 'SUBTRACT') {
    return roundedA - roundedB;
  }
  if (type === 'DIVIDE') {
    if (roundedB === 0) {
      return 'Error';
    }
    return roundedA / roundedB;
  }

  // Default return statement
  return 'Invalid operation type';
}

module.exports = calculateNumber;
