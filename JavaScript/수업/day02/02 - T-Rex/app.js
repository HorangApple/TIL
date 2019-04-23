const main = document.querySelector("#main");
const pepe = document.querySelector('#pepe')

console.log(main);
// 둘리를 클릭하면, 호이라고 한다.
main.addEventListener(
  "click",
  (() => {
    alert("끼얏호!");
  })()
);

let x = 0
let y = 0

document.addEventListener("keydown", function(event) {
  console.log(event.keyCode);
//   main.innerHTML = `<h1>${event.keyCode}</h1>`;
  if (event.keyCode === 38) {
    console.log("Up");
    y+=300
    pepe.style.marginBottom = `${y}px`
  } else if (event.keyCode === 40){
    y-=300
    pepe.style.marginBottom = `${y}px`
  } else if (event.keyCode === 37){
    x-=300
    pepe.style.marginLeft = `${x}px`
  } else if (event.keyCode === 39){
    x+=300
    pepe.style.marginLeft = `${x}px`
}
});
