/* eslint-disable jest/no-hooks */
/* eslint-disable no-unused-expressions */
/* eslint-disable jest/valid-expect */
// 5-payment.test.js

const sinon = require('sinon');
const { expect } = require('chai');

const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let consoleLogSpy;

  beforeEach(() => {
    // Create a spy on console.log to track its calls
    consoleLogSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the spy after each test
    consoleLogSpy.restore();
  });

  it('should log correct total when totalAmount = 100 and totalShipping = 20', () => {
    // Call the function under test
    sendPaymentRequestToApi(100, 20);

    // Assertions
    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledWithExactly('The total is: 120')).to.be.true;
  });

  it('should log correct total when totalAmount = 10 and totalShipping = 10', () => {
    // Call the function under test
    sendPaymentRequestToApi(10, 10);

    // Assertions
    expect(consoleLogSpy.calledOnce).to.be.true;
    expect(consoleLogSpy.calledWithExactly('The total is: 20')).to.be.true;
  });
});
