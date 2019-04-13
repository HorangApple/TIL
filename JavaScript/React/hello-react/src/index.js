import React, { Component } from "react";
import { render } from "react-dom";
import PropTypes from "prop-types";

const UserProfile = props => {
  return <img src={`https://source.unsplash.com/user/${props.username}`} />;
};
UserProfile.protoType = {
  pagename: PropTypes.string
};

const UserProfileLink = props => {
  return <a href={`https://ifelse.io/${props.username}`}>{props.username}</a>;
};

const UserCard = props => {
  return (
    <div>
      <UserProfile username={props.username} />
      <UserProfileLink username={props.username} />
    </div>
  );
};

render(<UserCard username="erondu" />, document.getElementById("root"));
