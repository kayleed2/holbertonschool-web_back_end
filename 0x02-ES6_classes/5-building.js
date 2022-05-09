/*
eslint no-underscore-dangle: ["error", { "allowAfterThis": true }]
*/
export default class Building {
  constructor(sqft) {
    if (Building.this.evacuationWarningMessage === undefined) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    return `Evacuate ${this._sqft}`;
  }
}
