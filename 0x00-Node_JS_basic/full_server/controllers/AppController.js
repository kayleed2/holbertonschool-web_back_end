// Write the App controller

class AppController {
  static getHomepage(req, resp) {
    return resp.status(200).send('Hello Holberton School!')
  }
}

module.exports = AppController;
