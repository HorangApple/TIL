import React, { Component } from 'react';
import LoginModalContainer from 'containers/modal/LoginModalContainer';
import * as baseActions from 'store/modules/base';
import {connect} from 'react-redux';
import {bindActionCreators} from 'redux';

class Base extends Component {
  initialize = async () => {

  }
  componentDidMount() {
    this.initialize();
  }
  render() {
    return (
      <div>
        <LoginModalContainer/>
      </div>
    )
  }
}

export default connect(
  null,
  (dispatch) => ({
    BaseActions: bindActionCreators(baseActions, dispatch)
  })
)(Base);