const path = require('path');

module.exports = {
    "env": {
        "es6": true,
        "node": true
    },
    "settings":{
        "import/resolver":{
            node:{paths:[path.resolve('./src')]}
        }
    },
    "extends": "eslint:recommended",
    "globals": {
        "Atomics": "readonly",
        "SharedArrayBuffer": "readonly"
    },
    "parserOptions": {
        "ecmaVersion": 2018
    },
    "rules": {
        "no-unused-vars": 1,
        "comma-dangle":0,
        "eol-last":0,
        "no-console":0
    }
};