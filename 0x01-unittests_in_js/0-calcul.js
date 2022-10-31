// Create a function named calculateNumber.
const calculateNumber = (a, b) => {
    if (isNaN(a) || isNaN(b)) throw new TypeError('Arguments must be numbers');
    return Math.round(a) + Math.round(b);
  };
  
  module.exports = calculateNumber;
