// HolbertonClass Class

/**
 * Build initial class
 *
 * @class HolbertonClass
 */
export default class HolbertonClass {
  constructor(size = '', location = '') {
    this.size = size;
    this.location = location;
  }

  [Symbol.toPrimitive](dataType) {
    if (dataType === 'string') {
      return (`${this.location}`);
    } if (dataType === 'number') {
      return (`${this.size}`);
    }
    return (`${this.location}`);
  }

  get size() {
    return this._size;
  }

  set size(value) {
    if (typeof value !== 'number') {
      throw new TypeError('size must be a number');
    }
    this._size = value;
  }

  get location() {
    return this._code;
  }

  set location(value) {
    if (typeof value !== 'string') {
      throw new TypeError('size must be a string');
    }
    this._code = value;
  }
}
