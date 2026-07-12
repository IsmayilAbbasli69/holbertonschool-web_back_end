const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

// Test cases for different type argument of function
describe('calculateNumber', () => {
    // Test case for SUM type argument of function
    describe('SUM', () => {
        it("should return 6 when adding 1.4 and 4.5", () => {
            expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
        });
    });
    // Test case for SUBTRACT type argument of function
    describe('SUBTRACT', () => {
        it("should return -4 when subtracting 1.4 and 4.5", () => {
            expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
        });
    });

    // Test case for DIVIDE type argument of function
    describe('DIVIDE', () => {
        it("should return 0.2 when dividing 1.4 and 4.5", () => {
            expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
        });

        it("should return 'Error' when dividing 1.4 and 0", () => {
            expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
        });
    });
});
