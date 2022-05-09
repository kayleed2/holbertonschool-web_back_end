/*
eslint no-underscore-dangle: ["error", { "allowAfterThis": true }]
*/
export default class Vroom {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    return new this.constructor();
  }
}
