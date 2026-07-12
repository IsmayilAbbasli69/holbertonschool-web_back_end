const sinon = require("sinon");
const { expect } = require("chai");

const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment");

describe("sendPaymentRequestToApi", () => {
  afterEach(() => {
    sinon.restore();
  });

  it("should log the correct message", () => {
    const calculateStub = sinon.stub(Utils, "calculateNumber").returns(10);

    const logSpy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    expect(calculateStub.calledOnce).to.equal(true);
    expect(calculateStub.calledWith("SUM", 100, 20)).to.equal(true);

    expect(logSpy.calledOnce).to.equal(true);
    expect(logSpy.calledWith("The total is: 10")).to.equal(true);
  });
});
