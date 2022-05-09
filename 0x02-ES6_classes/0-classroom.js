/*
eslint no-underscore-dangle: ["error", { "allowAfterThis": true }]
*/
export default class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }
}
