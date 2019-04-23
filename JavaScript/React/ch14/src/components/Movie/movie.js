const {connect} = require('react-redux')
class Movie extends React.Component{
    componentWillMount(){
        this.props.dispatch({
            type:FETCH_MOVIE,
            movie:{}
        })
    }

    render() {
        const {
            movie={
                starring:[]
            }
        }=this.props
    }
}

module.exports = connect(({movies}) => ({
    movie: movies.current
}), {
    fetchMovieActionCreator
}) (Movie)