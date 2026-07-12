const { expect } = require('chai');
const getPaymentTokenFromApi = require("./6-payment_token");

describe("getPaymentTokenFromAPI", () => {
  it("should get promise", async function () {
    const result = await getPaymentTokenFromApi(true);

    expect(result).to.deep.equal({
      data: "Successful response from the API",
    });
  });
});
