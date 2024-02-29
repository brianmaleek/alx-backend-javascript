/* eslint-disable jest/expect-expect */
/* eslint-disable jest/prefer-expect-assertions */
// 0-calcul.test.js

const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  /**
   * Test case for calculateNumber function.
   * It should return the sum of rounded numbers.
   * Expected: 4 because 1.4 is rounded to 1 and 2.6 is rounded to 3.
   */
  it('should return the sum of rounded numbers', () => {
    assert.strictEqual(calculateNumber(1.4, 2.6), 4);
  });

  /**
     * Test case for calculateNumber function.
     * It should handle negative numbers correctly.
     * Expected: -4 because -1.4 is rounded to -1 and -2.6 is rounded to -3.
     */
  it('should handle negative numbers correctly', () => {
    assert.strictEqual(calculateNumber(-1.4, -2.6), -4);
  });

  /**
     * Test case for calculateNumber function.
     * It should handle decimal numbers correctly.
     * Expected: 4 because 1.2 is rounded to 1 and 2.8 is rounded to 3.
     */
  it('should handle decimal numbers correctly for a', () => {
    assert.strictEqual(calculateNumber(1.2, 2.8), 4);
  });

  /**
     * Test case for calculateNumber function.
     * It should handle decimal numbers correctly.
     * Expected: 4 because 1 is rounded to 1 and 2.8 is rounded to 3.
     */
  it('should handle decimal numbers correctly for b', () => {
    assert.strictEqual(calculateNumber(1, 2.8), 4);
  });

  /**
     * Test case for calculateNumber function.
     * It should handle zero correctly.
     * Expected: 0 because both arguments are 0.
     */
  it('should handle zero correctly', () => {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  /**
     * Test case for calculateNumber function.
     * It should round a and b and return the sum of it.
     * Expected: NaN because no arguments provided.
     */
  it('should handle NaN correctly', () => {
    assert.strictEqual(calculateNumber(), NaN);
  });

  /**
     * Test case for calculateNumber function.
     * It should round a and b and return the sum of it.
     * Expected: 4 because '4' is converted to a number (4) and rounded, then added to 4.
     */
  it('should round a and b and return the sum of it', () => {
    assert.strictEqual(calculateNumber('', 4), 4);
  });

  /**
     * Test case for calculateNumber function.
     * It should round a and b and return the sum of it.
     * Expected: 8 because '4' is converted to a number (4) and rounded, then added to 4 (rounded).
     */
  it('should round str a and b and return the sum of it', () => {
    assert.strictEqual(calculateNumber('4', 4), 8);
  });
});
