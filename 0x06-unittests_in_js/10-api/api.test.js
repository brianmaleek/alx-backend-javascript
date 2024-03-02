/* eslint-disable jest/lowercase-name */
/* eslint-disable jest/no-test-callback */
/* eslint-disable jest/valid-expect */
// Import the 'request' module for making HTTP requests and
// the 'expect' function from Chai for assertions
const request = require('request');
const { expect } = require('chai');

const url = 'http://localhost:7865';

// eslint-disable-next-line jest/lowercase-name
describe('Index Page', () => {
  // Test for correct status code
  it('should return a status code of 200', (done) => {
    request.get(url, (_error, response) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  // Test for correct result
  it('should return the welcome string', (done) => {
    request.get(url, (_error, _response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('Cart Page', () => {
  // Test for correct status code when :id is a number
  it('should return a status code of 200 when :id is a number', (done) => {
    const cartId = 123; // Example numeric cart ID
    request.get(`${url}/cart/${cartId}`, (_error, response) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  // Test for correct status code when :id is NOT a number (404)
  it('should return a status code of 404 when :id is NOT a number', (done) => {
    const cartId = 'abc'; // Example non-numeric cart ID
    request.get(`${url}/cart/${cartId}`, (_error, response) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Login Endpoint', () => {
  it('should return a status code of 200 and welcome message', (done) => {
    const userName = 'John';
    request.post({
      url: `${url}/login`,
      body: JSON.stringify({ userName }),
      headers: { 'Content-Type': 'application/json' },
    }, (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome John');
      done();
    });
  });
});

describe('Available Payments Endpoint', () => {
  it('should return a status code of 200 and payment methods object', (done) => {
    request.get(`${url}/available_payments`, (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      const responseBody = JSON.parse(body);
      expect(responseBody).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});
