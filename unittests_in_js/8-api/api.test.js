const app = require("./api");
const { expect } = require("chai");
const request = require("request");

describe("Route test for index page", () => {
  it("returns correct status code", (done) => {
    request("http://localhost:7865", (err, res, body) => {
      expect(res.statusCode).to.equal(200);

      done();
    });
  });

  it("returns correct response body", (done) => {
    request("http://localhost:7865", (err, res, body) => {
      expect(body).to.equal("Welcome to the payment system");

      done();
    });
  });
});
