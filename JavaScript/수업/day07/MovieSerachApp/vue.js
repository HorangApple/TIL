const API_KEY = "187f30a9782a19dee9f5bb4aea47b45e"
const URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}`
const IMG_URL = 'https://image.tmdb.org/t/p/w500'
/*
1. 빈 movies를 가지고 있는 vue 인스턴스 생성
2. created 함수가 실행되면서 api를 통해 movies를 가져옴
3. vue의 movies 안에 가져온 movies 데이터를 할당
4. vue의 데이터에 변화가 생기면서 새롭게 렌더링
*/
const app = new Vue({
  el: '#main',
  data: {
    query: '',
    movies: []
  },
  // 함수를 정의하는 곳, caching이 됨(함수의 반환값을 vue가 알고 있음)
  computed: {
    filteredMovies: function () {
      // query 로 filtering 한 movie 만 반환
      // callback 함수에서 반환되는 값이 true인 아이템 만으로 새로운 배열 생성
      return this.movies.filter(movie => {
        // indexOf 대신에 includes로 사용해도 됨
        return movie.title.toLowerCase().replace(/\s/g,'').indexOf(this.query.toLowerCase().replace(/\s/g,'').trim()) > -1
      })
    }
  },
  // Vue 인스턴스가 생성되고 난 후 실행하는 함수, api를 받아온다.
  async created() {
    const response = await axios.get(URL)
    const movies = response.data.results
    // callback 함수에서 return 되는 아이템으로 새롭게 배열을 만듬
    this.movies = movies.map(movie => {
      return { title: movie.title, image: IMG_URL + movie.poster_path }
    })
  }
})