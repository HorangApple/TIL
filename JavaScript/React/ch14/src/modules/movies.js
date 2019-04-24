// 영화 목록 리듀서
const { handleActions } = require("redux-actions");
const FETCH_MOVIES = "movies/FETCH_MOVIES";
const FETCH_MOVIE = "movies/FETCH_MOVIE";

const initialState = {
  movies: [],
  movie: {}
};

// 함수와 액션을 맵핑하는 형식
module.exports = {
  // FETCH_MOVIES 액션 생성자 정의
  fetchMoviesActionCreator: movies => ({
    type: FETCH_MOVIES,
    movies
  }),
  // FETCH_MOVIE 액션 생성자 정의
  fetchMovieActionCreator: index => ({
    type: FETCH_MOVIE,
    index
  }),
  reducer: handleActions(
    {
      [FETCH_MOVIES]: (state, action) => ({
        // 펼침 연산자
        ...state,
        // 스토어의 모든 영화 목록을 저장하거나 변경
        all: action.movies 
      }),
      [FETCH_MOVIE]: (state, action) => ({
        ...state,
        // 스토어의 특정 영화를 저장하거나 변경
        current: state.all[action.index - 1] 
      })
    },
    initialState
  )
};
