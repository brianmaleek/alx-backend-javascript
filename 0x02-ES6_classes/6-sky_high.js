import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = this.validateNumber(floors, 'floors');
  }

  // Getters and setters for floors
  get floors() {
    return this._floors;
  }

  set floors(value) {
    this._floors = this.validateNumber(value, 'floors');
  }

  // Overrides evacuationWarningMessage method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
