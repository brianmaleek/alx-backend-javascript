import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    const current = this;
    return Object.assign(Object.create(Object.getPrototypeOf(current)), {
      _brand: undefined,
      _motor: undefined,
      _color: undefined,
    });
  }
}
