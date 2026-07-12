const request = require('request');
const { expect } = require('chai');

describe('API integration tests', () => {
  const URL = 'http://localhost:7865'; 

  it('Correct status code?', (done) => {
    request(URL, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result?', (done) => {
    request(URL, (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('Correct status code for /cart/:id with valid id?', (done) => {
    request(`${URL}/cart/123`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result for /cart/:id with valid id?', (done) => {
    request(`${URL}/cart/123`, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 123');
      done();
    });
  });
  
  it('Correct status code for /cart/:id with invalid id?', (done) => {
    request(`${URL}/cart/abc`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('Correct status code for :login with valid userName?', (done) => {
    const options = {
      url: `${URL}/login`,
      method: 'POST',
      json: { userName: 'John' },
    };

    request(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result for :login with valid userName?', (done) => {
    const options = {
      url: `${URL}/login`,
      method: 'POST',
      json: { userName: 'John' },
    };

    request(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome John');
      done();
    });
  }); 

  it('Correct status code for /available_payments?', (done) => {
    request(`${URL}/available_payments`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct result for /available_payments?', (done) => {
    request(`${URL}/available_payments`, (error, response, body) => {
      const expectedResponse = {
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      };
      expect(JSON.parse(body)).to.deep.equal(expectedResponse);
      done();
    });
  });
});