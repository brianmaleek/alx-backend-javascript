/* eslint-disable jest/no-test-callback */
/* eslint-disable jest/valid-expect */
// 6-payment_token.test.js

/**
 * @module 6-payment_token.test
 * @description This file contains unit tests for the `getPaymentTokenFromAPI` function.
 */

const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('async tests with done', () => {
  it('should resolve a promise if success === true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.include({ data: 'Successful response from the API' });
        done();
      })
      .catch((error) => {
        done(error);
      });
  });
});
