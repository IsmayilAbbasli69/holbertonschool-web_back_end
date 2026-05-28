/* Classroom
    https://stackoverflow.com/questions/4484424/underscore-prefix-for-property-and-method-names-in-javascript
    prefix
*/
export default class ClassRoom {
  constructor(maxStudentsSize = 0) {
    this._maxStudentsSize = maxStudentsSize;
  }
}
