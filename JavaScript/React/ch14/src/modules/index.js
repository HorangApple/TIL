// 리듀서 결합
const { combineReducers } = require("redux");
const { reducer: movies } = require("./movies");

module.exports = combineReducers({
  movies
});
