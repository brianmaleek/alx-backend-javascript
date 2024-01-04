/* eslint-disable class-methods-use-this */
export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.validateString(name, 'name');
    this._length = this.validateNumber(length, 'length');
    this._students = this.validateArray(students, 'students');
  }

  // Getters and setters for name
  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this.validateString(value, 'name');
  }

  // Getters and setters for length
  get length() {
    return this._length;
  }

  set length(value) {
    this._length = this.validateNumber(value, 'length');
  }

  // Getters and setters for students
  get students() {
    return this._students;
  }

  set students(value) {
    this._students = this.validateArray(value, 'students');
  }

  // Validate string
  validateString(value, name) {
    if (typeof value !== 'string') {
      throw new TypeError(`${name} must be a string`);
    }
    return value;
  }

  // Validate number
  validateNumber(value, name) {
    if (typeof value !== 'number') {
      throw new TypeError(`${name} must be a number`);
    }
    return value;
  }

  // Validate array
  validateArray(value, name) {
    if (!Array.isArray(value)) {
      throw new TypeError(`${name} must be an Array`);
    }
    return value;
  }
}
