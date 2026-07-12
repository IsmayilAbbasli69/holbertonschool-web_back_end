const sinon = require("sinon");
const { expect } = require("chai");

const sendPaymentRequestToApi = require("./5-payment");

describe("sendPaymentRequestToApi", () => {
  let spy;

  // Creating Spy before each test
  beforeEach(() => {
    spy = sinon.spy(console, "log");
  });

  // Wrapping function after each test
  afterEach(() => {
    sinon.restore();
  });

  // First Test
  it("should test sending payment", () => {
    // Calling function with 100 and 20 arguments
    sendPaymentRequestToApi(100, 20);

    // Verifiying the function called once and log correct message
    expect(spy.calledOnce).to.equal(true);
    expect(spy.calledWith("The total is: 120")).to.equal(true);
  });

  // Second Test
  it("should test sending payment", () => {
    // Calling function with 10 and 10 arguments
    sendPaymentRequestToApi(10, 10);

    // Verifiying the function called once and log correct message
    expect(spy.calledOnce).to.equal(true);
    expect(spy.calledWith("The total is: 20")).to.equal(true);
  });
});
