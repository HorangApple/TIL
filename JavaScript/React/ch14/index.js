const React = require('react')
const {render} = require('react-dom')
const {Provider, createStore} = require('react-redux')
const reducers = require('./modules')
const routes = require('./routes')

module.exports = render((
    <Provider store={createStore(reducers)}>
    {routes}
    </Provider>
), document.getElementById('app'))