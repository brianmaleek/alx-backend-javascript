/* eslint-disable consistent-return */
// 6-payment_token.js
/**
 * @module 6-payment_token
 * @description This module exports a function that returns a promise.
 */
function getPaymentTokenFromAPI(success) {
  if (success === true) return Promise.resolve({ data: 'Successful response from the API' });
}

module.exports = getPaymentTokenFromAPI;
