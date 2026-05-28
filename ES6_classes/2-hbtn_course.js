// Holberton Course
export default class HolbertonCourse {
  constructor(name = '', length = 0, students = []) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw TypeError('Length must be a number');
    }
    this._length = value;
  }

  get students() {
    return this._students;
  }

  set students(currStudents) {
    if (typeof currStudents === 'object') {
      for (const student in currStudents) {
        if (typeof student !== 'string') {
          throw new TypeError('Students must be an array of strings');
        }
      }
    } else {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = currStudents;
  }
}
