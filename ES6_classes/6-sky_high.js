// Extend Buildinf
import Building from './5-building';

/**
 * Define Class
 *
 * @class SkyHighBuilding
 */
class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get floors() {
    return (this._floors);
  }

  evacuationWarningMessage() {
    return (`Evacuate slowly the ${this.floors} floors`);
  }
}

export default SkyHighBuilding;
