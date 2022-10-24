// create a small HTTP server using the http module
const http = require('http');

const app = http
  .createServer((req, resp) => {
    resp.end('Hello Holberton School!');
  })
  .listen(1245);

module.exports = app;
