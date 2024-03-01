/* eslint-disable jest/valid-expect */
// 6-payment_token.test.js

/**
 * Tests the getPaymentTokenFromAPI function
 * It should return a successful response from the API when success is true
 * @return {Promise<void>} A Promise that resolves when the async test is complete
 */
const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('should return successful response from the API when success is true', () => new Promise((done) => {
    // Call the function under test with success set to true
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // Assert that the response is as expected
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done(); // Call done to indicate that the async test is complete
      })
      .catch((err) => done(err)); // Call done with an error if the promise is rejected
  }));
});
