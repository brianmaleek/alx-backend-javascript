// 0-calcul.js

/**
 * Rounds two numbers and returns their sum.
 * @param {number} a - The first number to be rounded.
 * @param {number} b - The second number to be rounded.
 * @returns {number} The sum of the rounded numbers.
 */

function calculateNumber(a, b) {
  return Math.round(a) + Math.round(b);
}
module.exports = calculateNumber;
