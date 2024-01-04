/* eslint-disable class-methods-use-this */
export default class Currency {
  constructor(code, name) {
    this._code = this.validateString(code, 'code');
    this._name = this.validateString(name, 'name');
  }

  // Getters and setters for code
  get code() {
    return this._code;
  }

  set code(value) {
    this._code = this.validateString(value, 'code');
  }

  // Getters and setters for name
  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this.validateString(value, 'name');
  }

  // Method to display full currency
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }

  // Validate string
  validateString(value, name) {
    if (typeof value !== 'string') {
      throw new TypeError(`${name} must be a string`);
    }
    return value;
  }
}
