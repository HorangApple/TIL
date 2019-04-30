// import axios from 'axios' // node가 es6를 지원을 못함, babel로 해결
// const axios = require('axios') // 브라우저 상에서 지원이 안됨
// React 같은 경우 React가 알아서 작동해주었기 때문에 돌아갔던 것
// 원래 npm으로 설치한 모듈은 브라우저에서 읽히지 않는다.

// fetch
// XMLHttpRequest
// Axios

const URL = 'https://dog.ceo/api/breeds/image/random'

// then 사용
axios.get(URL) //AJAX CALL
    .then(response=>{
      const imageUrl = response.data.message
      const imageBox = document.querySelector('#img-div')
      const image = document.createElement('img')
      image.src = imageUrl
      imageBox.appendChild(image)
    })


// async/await 사용
const getImage = async() => {
  // 비동기 함수 promise에 await를 붙인다
  // 응답을 통해서 URL을 받아오길 기대함
  const response = await axios.get(URL) 
  const imageUrl = response.data.message
  const imageBox = document.querySelector('#img-div')
  const image = document.createElement('img')
  image.src = imageUrl
  imageBox.appendChild(image)
}
getImage()