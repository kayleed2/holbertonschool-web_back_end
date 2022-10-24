// create a small HTTP server using Express module
const express = require('express');

const app = express();

app.get('/', (req, resp) => resp.send('Hello Holberton School!'))
  .listen(1245);

module.exports = app;
