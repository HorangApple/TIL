const React = require('react')
const {
    Router,
    Route,
    IndexRoute,
    browserHistory
} = require('react-router')
const App = require('components/app/app.js')
const Movies = require('components/movies/movies.js')
const Movie = require('components/movie/movie.js')

module.exports = (
    <Router history = {browserHistory}>
        <Route path="/" component={App}>
            // Movie 컴포넌트가 최상위 페이지와 /movies 페이지에서 모두 렌더링 됨
            <IndexRoute component={Movies} />
            <Route path="movies" component={Movies}>
                <Route path=":id" component={Movie}/>
            </Route>
        </Route>
    </Router>
)