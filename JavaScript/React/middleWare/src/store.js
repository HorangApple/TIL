import { createStore, applyMiddleware } from "redux";
import modules from "./modules";
// import loggerMiddleware from './lib/loggerMiddleware';
import { createLogger } from "redux-logger";
// import ReduxThunk from 'redux-thunk';

// import {createPromise } from 'redux-promise-middleware'

import penderMiddleware from "redux-pender";

const logger = createLogger();
// const pm = createPromise ({
//   promiseTypeSuffixes:['PENDING','SUCCESS','FAILURE']
// })

const store = createStore(
  modules,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__(),
  applyMiddleware(logger, penderMiddleware())
);

export default store;
