// 6-payment_token.js

/**
 * Simulates getting a payment token from an API.
 * @param {boolean} success - Indicates whether the API call should succeed.
 * @returns {Promise<Object>} A Promise that resolves with the API response object.
 */
function getPaymentTokenFromAPI(success) {
  return new Promise((resolve) => {
    if (success) {
      // Resolve the promise with the successful response object
      resolve({ data: 'Successful response from the API' });
    }
  });
}

module.exports = getPaymentTokenFromAPI;
