// Airport Class

/**
 * Build initial class
 *
 * @class Airport
 */
export default class Airport {
  constructor(name = '', code = '') {
    this.name = name;
    this.code = code;
  }

  get [Symbol.toStringTag]() {
    return `${this.code}`;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = value;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw new TypeError('code must be a string');
    }
    this._code = value;
  }
}
