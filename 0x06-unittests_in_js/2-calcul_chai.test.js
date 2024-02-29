/* eslint-disable jest/expect-expect */
/* eslint-disable jest/prefer-expect-assertions */
// 2-calcul_chai.test.js

const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('#calculateNumber() with type SUM', () => {
  /**
   * Test case for calculateNumber function.
   * It should return the sum of rounded numbers.
   * Expected: 4 because 1.4 is rounded to 1 and 2.6 is rounded to 3.
   */
  it('should return the sum of rounded numbers', () => {
    chai.expect(calculateNumber('SUM', 1.4, 2.6)).to.equal(4);
  });

  /**
   * Test case for calculateNumber function.
   * It should handle negative numbers correctly.
   * Expected: -4 because -1.4 is rounded to -1 and -2.6 is rounded to -3.
   */
  it('should handle negative numbers correctly', () => {
    chai.expect(calculateNumber('SUM', -1.4, -2.6)).to.equal(-4);
  });

  /**
   * Test case for calculateNumber function.
   * It should handle zero correctly.
   * Expected: 0 because both arguments are 0.
   */
  it('should handle zero correctly', () => {
    chai.expect(calculateNumber('SUM', 0, 0)).to.equal(0);
  });
});

describe('#calculateNumber() with type SUBTRACT', () => {
  /**
   * Test case for calculateNumber function.
   * It should handle decimal numbers correctly.
   * Expected: -2 because 1.2 is rounded to 1 and 2.8 is rounded to 3.
   */
  it('should handle decimal numbers correctly for a', () => {
    chai.expect(calculateNumber('SUBTRACT', 1.2, 2.8)).to.equal(-2);
  });

  /**
   * Test case for calculateNumber function.
   * It should handle decimal numbers correctly.
   * Expected: 4 because 1 is rounded to 1 and 2.8 is rounded to 3.
   */
  it('should handle decimal numbers correctly for b', () => {
    chai.expect(calculateNumber('SUBTRACT', 1, 2.8)).to.equal(-2);
  });

  /**
   * Test case for calculateNumber function.
   * It should handle subtraction.
   * Expected: -4 because 1.4 is rounded to 1 and 2.6 is rounded to 3.
   */
  it('should handle subtraction', () => {
    chai.expect(calculateNumber('SUBTRACT', 1.4, 2.6)).to.equal(-2);
  });

  /**
     * Test case for calculateNumber function.
     * It should handle negative numbers correctly.
     * Expected: 2 because -1.4 is rounded to -1 and -2.6 is rounded to -3.
     */
  it('should handle negative numbers correctly', () => {
    chai.expect(calculateNumber('SUBTRACT', -1.4, -2.6)).to.equal(2);
  });
});

describe('#calculateNumber() with type DIVIDE', () => {
  /**
   * Test case for calculateNumber function.
   * It should handle division by zero.
   * Expected: 'Error' because division by zero occurs.
   */
  it('should handle division by zero', () => {
    chai.expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });

  /**
   * Test case for calculateNumber function.
   * It should handle division.
   * Expected: 3.0 because 2.6 is rounded to 3 and 1.4 is rounded to 1.
   */
  it('should handle division', () => {
    chai.expect(calculateNumber('DIVIDE', 2.6, 1.4)).to.equal(3.0);
  });

  /**
   * Test case for calculateNumber function.
   * It should handle division.
   * It should return 0.25 when dividing 1 and 3.7.
   */
  it('should return 0.25 when dividing 1 and 3.7', () => {
    chai.expect(calculateNumber('DIVIDE', 1, 3.7)).to.equal(0.25);
  });

  /**
   * Test case for calculateNumber function.
   * It should handle division.
   * It should return -1 when dividing -0.7 and 0.7.
   */
  it('should return -1 when dividing -0.7 and 0.7', () => {
    chai.expect(calculateNumber('DIVIDE', -0.7, 0.7)).to.equal(-1);
  });

  /**
   * Test case for calculateNumber function.
   * It should handle division.
   * It should return 1 when dividing -0.8 and -0.7.
   */
  it('should return 1 when dividing -0.8 and -0.7', () => {
    chai.expect(calculateNumber('DIVIDE', -0.8, -0.7)).to.equal(1);
  });

  /**
   * Test case for calculateNumber function.
   * It should handle division.
   * It should return 'Error' when dividing 1.3 and 0.3.
   */
  it("should return 'Error' when dividing 1.3 and 0.3", () => {
    chai.expect(calculateNumber('DIVIDE', 1.3, 0.3)).to.equal('Error');
  });
});

describe('#calculateNumber() with invalid operation type', () => {
  /**
   * Test case for calculateNumber function.
   * It should handle invalid operation type.
   * Expected: 'Invalid operation type' because the operation type is invalid.
   */
  it('should handle invalid operation type', () => {
    chai.expect(calculateNumber('INVALID', 1.4, 2.6)).to.equal('Invalid operation type');
  });
});
