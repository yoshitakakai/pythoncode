module.exports = {
    mode: 'development',
    entry: './src/main.js',
    output: {
        filename: './out/bundle.js'
    },
    module: {
        rules: [
            {
                test: /.js$/,
                loader: 'babel-loader',
                options: {
                    presets:['@babel/preset-env', '@babel/preset-react']
                }
            }
        ]
    }
};