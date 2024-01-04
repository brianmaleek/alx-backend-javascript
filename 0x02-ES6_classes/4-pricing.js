/* eslint-disable class-methods-use-this */
import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = this.validateNumber(amount, 'amount');
    this._currency = this.validateCurrency(currency, 'currency');
  }

  // Getters and setters for amount
  get amount() {
    return this._amount;
  }

  set amount(value) {
    this._amount = this.validateNumber(value, 'amount');
  }

  // Getters and setters for currency
  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = this.validateCurrency(value, 'currency');
  }

  // Method to display full price
  displayFullPrice() {
    return `${this.amount} ${this.currency.displayFullCurrency()}`;
  }

  // Static method to convert price to another currency
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }

  // Validate currency
  validateCurrency(value, name) {
    if (!(value instanceof Currency)) {
      throw new TypeError(`${name} must be a Currency`);
    }
    return value;
  }

  // Validate number
  validateNumber(value, name) {
    if (typeof value !== 'number' || Number.isNaN(value)) {
      throw new TypeError(`${name} must be a number`);
    }
    return value;
  }
}
