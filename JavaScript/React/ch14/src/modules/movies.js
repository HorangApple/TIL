const {handleActions} = require('redux-actions')
const FETCH_MOVIES = 'movies/FETCH_MOVIES'
const FETCH_MOVIE = 'movies/FETCH_MOVIE'

const initialState = {
    movies:[],
    movie:{}
}

// 함수와 액션을 맵핑하는 형식
module.exports = {
    // FETCH_MOVIES 액션 생성자 정의
    fetchMoviesActionCreator:(movies)=>({
        type: FETCH_MOVIES,
        movies
    }),
    // FETCH_MOVIE 액션 생성자 정의
    fetchMovieActionCreator: (index) =>({
        type: FETCH_MOVIE,
        index
    }),
    reducer: handleActions({
        [FETCH_MOVIES]: (state, action) => ({
            ...state,
            all: action.movies
        }),
        [FETCH_MOVIE]: (state,action)=>({
            ...state,
            current: state.all[action.index-1]
        })
    }, initialState)
}