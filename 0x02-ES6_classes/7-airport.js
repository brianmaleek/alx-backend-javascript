export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Getters and setters for name
  get name() {
    return this._name;
  }

  set name(value) {
    this._name = value;
  }

  // Getters and setters for code
  get code() {
    return this._code;
  }

  set code(value) {
    this._code = value;
  }

  // Default string representation of an object is [object object_type]
  get [Symbol.toStringTag]() {
    return this.code;
  }
}
