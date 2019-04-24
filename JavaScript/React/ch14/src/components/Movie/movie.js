const React = require("react");
const { Link } = require("react-router");
const { connect } = require("react-redux");
const { fetchMovieActionCreator } = require("modules/movies.js");
const styles = require("./movie.css");

class Movie extends React.Component {
  componentWillMount() {
    this.props.fetchMovie(this.props.params.id);
  }
  componentWillUpdate(next) {
    if (this.props.params.id !== next.params.id) {
      this.props.fetchMovie(next.params.id);
    }
  }

  render() {
    const {
      movie = {
        starring: []
      }
    } = this.props;
    return (
      <div
        className={styles.movie}
        style={{
          backgroundImage: `linear-gradient(90deg,rgba(0,0,0,1) 0%, rgba(0,0,0,0.625) 100%), url(${
            movie.cover
          })`
        }}
      >
        <div
          className={styles.cover}
          style={{ backgroundImage: `url(${movie.cover})` }}
        />
        <div className={styles.description}>
          <div className={styles.title}>{movie.title}</div>
          <div className={styles.year}>{movie.year}</div>
          <div className={styles.starring}>
            {movie.starring.map((actor = {}, index) => (
              <div key={index} className={styles.actor}>
                {actor.name}
              </div>
            ))}
          </div>
        </div>
        <Link className={styles.closeButton} to="/movies">
          ←
        </Link>
      </div>
    );
  }
}
// 컴포넌트를 스토어에 연결
module.exports = connect(
  ({ movies }) => ({
    movie: movies.current
  }),
  {
    fetchMovie: fetchMovieActionCreator
  }
)(Movie);
