import React from "react";
import ReactDOM from "react-dom";
import classNames from "classnames/bind";

class ClickCounterButton extends React.Component {
  render() {
    return <button
    onClick={this.props.handler}
    className="btn btn-danger">
    Increase Volume (Current volume is {this.props.counter})
    </button>
  }
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 0
    };
    this.handleClick=this.handleClick.bind(this)
  }
  handleClick(e) {
    console.log(this.state.counter)
    this.setState({ counter: ++this.state.counter });
  }
  render() {
    return (
    <ClickCounterButton handler={this.handleClick} counter={this.state.counter} />
    )
  }
}
ReactDOM.render(<App />, document.querySelector("#root"));
