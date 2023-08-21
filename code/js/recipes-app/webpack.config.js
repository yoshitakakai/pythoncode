var path = require("path");

module.exports = {
    devtool: "source-map",
    entry: "./src/index.js",
    output: {
        path: path.join(__dirname, "dist", "assets"),
        filename: "bundle.js"
    },
    module: {
        rules: [{ test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" }]
    }
};