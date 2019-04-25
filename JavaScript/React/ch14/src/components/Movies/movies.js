const React = require("react");
const { connect } = require("react-redux");
const { Link } = require("react-router");
const movies = require("../../movies.json");
const { fetchMoviesActionCreator } = require("modules/movies.js");
const styles = require("./movies.css");

class Movies extends React.Component {
  componentWillMount() {
    this.props.fetchMovies(movies);
  }
  render() {
    const { children, movies = [], params = {} } = this.props;

    return (
      <div className={styles.movies}>
        <div className={params.id ? styles.listHidden : styles.list}>
          {movies.map((movie, index) => (
            <Link key={index} to={`/movies/${index + 1}`}>
              <div
                className={styles.movie}
                style={{ backgroundImage: `url(${movie.cover})` }}
              />
            </Link>
          ))}
        </div>
        {children}
      </div>
    );
  }
}
// 컴포넌트를 스토어에 연결
module.exports = connect(
  ({ movies }) => ({
    movies: movies.all
  }),
  {
    fetchMovies: fetchMoviesActionCreator
  }
)(Movies);