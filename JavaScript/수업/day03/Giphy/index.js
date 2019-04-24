// 1. input 태그안의 값을 잡는다.
const button = document.querySelector("#js-go");
const input = document.querySelector("#js-userinput");
const resultArea = document.querySelector("#result-area");

button.addEventListener("click", e => {
  const value = input.value;
  searchAndPush(value)
});

input.addEventListener("keypress", e => {
  const value = input.value;
  if (e.charCode === 13) {
    searchAndPush(value)
  }
});

// 2. Giphy api를 통해 data를 받아서 가공한다.
const searchAndPush = (keyword) => {
  // 이전 검색 초기화
  resultArea.innerHTML=null
  const myInit = { api_key: "keyValue", lang: "ko" };
  const GiphyXHR = new XMLHttpRequest();
  const GiphyURL = `https://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${myInit.api_key}&lang=${myInit.lang}`
  GiphyXHR.open("GET", GiphyURL);
  GiphyXHR.send();
  // 콜백 함수 안에 있는 변수는 밖으로 빼낼 수 없다.
  GiphyXHR.addEventListener('load',(event)=>{
    const rawData=event.target.response;
    const parsedData = JSON.parse(rawData)
    for (data of parsedData.data){
      pushToDom(data.images.fixed_height.url)
    }
  })
}

// 3. gif 파일들을 index.html(DOM)에 밀어 넣어서 보여준다.
const pushToDom = data => {
  // innerHTML은 비효율적으로 동작한다. : 기존 것을 지우고 전체+추가요소를 다시 넣는 방식
  // resultArea.innerHTML += `<img src="${data}">`;
  const img = document.createElement('img')
  img.setAttribute('src',data) // img.src=data과 같다.
  img.className = 'container-image'
  
  resultArea.appendChild(img)
};


