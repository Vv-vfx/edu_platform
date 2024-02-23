const path = require('path');

module.exports = {
  mode: 'development',
  entry: {
    requests_by_token: "./src/requests_by_token.js",
    update_token: "./src/update_token.js"
  },
  output: {
    path: path.resolve(__dirname, "../static/frontend/"),
    filename: '[name].js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};