export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Getters and setters for size
  get size() {
    return this._size;
  }

  set size(value) {
    this._size = value;
  }

  // Getters and setters for location
  get location() {
    return this._location;
  }

  set location(value) {
    this._location = value;
  }

  // Casting to number
  valueOf() {
    return this.size;
  }

  // Casting to string
  toString() {
    return this.location;
  }
}
