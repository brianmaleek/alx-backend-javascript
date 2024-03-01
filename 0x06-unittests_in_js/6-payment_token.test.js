/* eslint-disable jest/valid-expect */
// 6-payment_token.test.js

/**
 * @module 6-payment_token.test
 * @description This file contains unit tests for the `getPaymentTokenFromAPI` function.
 */

const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  describe('arg = true?', () => {
    it('resolved to true.', () => new Promise((done) => {
      getPaymentTokenFromAPI(true)
        .then((res) => {
          expect(res).to.include({ data: 'Successful response from the API' });
          done();
        })
        .catch((err) => done(err));
    }));
  });
});
