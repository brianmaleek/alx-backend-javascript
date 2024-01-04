export default class Building {
  constructor(sqft) {
    this._sqft = this.validateNumber(sqft, 'sqft');
    this.evacuationWarningMessage();
  }

  // Getters and setters for sqft
  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = this.validateNumber(value, 'sqft');
  }

  // Abstract method - must be implemented by subclasses
  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    if (this.constructor !== Building) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // Validate number
  // eslint-disable-next-line class-methods-use-this
  validateNumber(value, name) {
    if (typeof value !== 'number' || Number.isNaN(value)) {
      throw new TypeError(`${name} must be a number`);
    }
    return value;
  }
}
