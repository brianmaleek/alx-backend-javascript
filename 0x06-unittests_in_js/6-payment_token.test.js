/* eslint-disable jest/expect-expect */
/* eslint-disable jest/valid-expect */
// 6-payment_token.test.js

/**
 * Tests the getPaymentTokenFromAPI function
 * It should return a successful response from the API when success is true
 * @return {Promise<void>} A Promise that resolves when the async test is complete
 */
const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token');

/**
 * Test suite for the getPaymentTokenFromAPI function.
 */
describe('getPaymentTokenFromAPI', () => {
  /**
   * Test case to verify that the function returns a promise.
   * @param {Function} done - Callback function to indicate when the test is complete.
   */
  it('should return a promise', () => new Promise((done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        assert.equal(res.data, 'Successful response from the API');
        done();
      })
      .catch((error) => {
        done(error);
      });
  }));
});
