import React, { Component } from "react";
import { render } from "react-dom";

 
let si = <h1>HelloWorld</h1>
class HelloWorld extends Component {
  render() {
    return (
      <div>
        {si}
        <h1>2. HelloWorld!</h1>
      </div>
    )
  }
}

render(
<HelloWorld />, document.getElementById("root"));
