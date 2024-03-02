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
