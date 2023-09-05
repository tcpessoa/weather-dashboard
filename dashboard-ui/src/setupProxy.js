const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function (app) {
  app.use(
    '/weather', // Replace with your API route path
    createProxyMiddleware({
      target: 'http://127.0.0.1:8000', // The host port of your backend API
      changeOrigin: true,
    })
  );

  // console log each time a proxy request is made
  app.use('/weather', function (req, res, next) {
    console.log('Request Type:', req.method);
    next();
  }
  );
};

