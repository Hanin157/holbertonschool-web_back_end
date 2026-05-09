export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const Species = Symbol.species;
    const ClonedClass = this.constructor[Species] || this.constructor;

    return new ClonedClass();
  }

  static get [Symbol.species]() {
    return this;
  }
}
