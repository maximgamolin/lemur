const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: {
        index: './src/index.js',
    },
    resolve: {
        extensions: ['.jsx', '.js'],
        modules: [
            path.resolve(__dirname, "node_modules"),
            'node_modules'
        ],
    },
    module: {
        rules: [{
            test: /\.(jsx|js)$/,
            include: path.resolve(__dirname, 'src'),
            exclude: /node_modules/,
            use: [{
                loader: 'babel-loader',
                options: {
                    presets: [
                        ['@babel/preset-env', {
                            "targets": "defaults"
                        }],
                        '@babel/preset-react'
                    ]
                }
            }]
        }, {
            test: /\.css$/i,
            use: ['style-loader', 'css-loader'],
        }, {
            test: /\.(png|jpe?g|gif|svg|woff|woff2|eot|ttf)$/i,
            use: {
                loader: 'file-loader',
                options: {
                  publicPath: '/static',
                },
            },
        }],
    },
    watch: (process.env.NODE_ENV === 'development'),
    devtool: (process.env.NODE_ENV === 'development') ? 'cheap-inline-module-source-map' : false,
    output: {
        filename: '[name].min.js',
        path: path.resolve('./build/static/')
    }
};
