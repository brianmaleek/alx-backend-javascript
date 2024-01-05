/* eslint-disable class-methods-use-this */
import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  // getter and setter for range
  get range() {
    return this._range;
  }

  set range(range) {
    this._range = range;
  }

  cloneCar() {
    return new Car();
  }
}
