import React from "react";
import ReactDOM from "react-dom";
import classNames from "classnames/bind";

class Menu extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      menus: []
    };
  }
  componentDidMount() {
    fetch("http://localhost:3000/menus.json")
      .then(response => response.json())
      .then(menus => this.setState( {menus:menus} ));
  }
  render() {
    return (
      <div>
      {console.log(this.state)}
        {this.state.menus.map((v, i) => {
          return (
            <div key={i}>
              <Link label={v} />
            </div>
          );
        })}
      </div>
    );
  }
}

class Link extends React.Component {
  render() {
    const url =
      "/" +
      this.props.label
        .toLowerCase()
        .trim()
        .replace(" ", "-");
    return (
      <div>
        <a href={url}>{this.props.label}</a>
      </div>
    );
  }
}
ReactDOM.render(
  React.createElement(Menu, null),
  document.querySelector("#root")
);
