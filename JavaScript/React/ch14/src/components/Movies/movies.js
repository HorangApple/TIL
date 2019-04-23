const React = require('react')
const {connect} = require('react-redux')
const {Link} = require('react-router')
const movies = require('../../movies.json')
const {fetchMoviesActionCreator} = require('module/movies.js')
const styles = require('./movies.css')

class Movies extends React.Component {
  componentWillMount(){
    this.props.fetchMovies(movies)
  }
  render() {
    const { 
      children,
      movies = [],
      params={}
    } = this.props;

    return (
      <div className={styles.movies}>
        {movies.map((movie, index) => (
          <div key={index}>{movie.title}</div>
        ))}
      </div>
    );
  }
}
module.exports=connect(({movies})=>({
  movies:movies.all
}), {
  fetchMoviesActionCreator
})(Movies)