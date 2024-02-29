/* eslint-disable no-unused-expressions */
/* eslint-disable jest/valid-expect */
// 3-payment.test.js

const { expect } = require('chai');
const sinon = require('sinon');

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  /**
   * Test case for sendPaymentRequestToApi function.
   * It should call Utils.calculateNumber with correct arguments.
   * Expected: true because Utils.calculateNumber is called once with 'SUM', 100, and 20.
   * The result of the arithmetic operation or 'Error' if division by zero occurs.
   * sinon.spy(object, 'method') creates a spy for the object's method.
   * The spy records calls to the method in its call history.
   */
  it('should call Utils.calculateNumber with correct arguments', () => {
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);

    expect(calculateNumberSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

    calculateNumberSpy.restore();
  });
});
