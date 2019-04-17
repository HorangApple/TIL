import React, { Component } from "react";
import { render } from "react-dom";

// 상태 비저장 컴포넌트1
const DigitalDisplay = function(props){
  return <div>{props.time}</div>
}

// 상태 비저장 컴포넌트2
const AnalogDisplay = function AnalogDisplay(props){
  let date = new Date(props.time)
  let dialStyle = {
    position: 'relative',
    top: 0,
    left: 0,
    width: 200,
    height: 200,
    borderRadius: 20000,
    borderStyle: 'solid',
    borderColor: 'black'
  }
  let secondHandStyle = {
    position: 'relative',
    top: 100,
    left: 100,
    border: '1px solid red',
    width: '40%',
    height: 1,
    transform: 'rotate(' + ((date.getSeconds() / 60) *360 -90).toString() + 'deg)',
    transformOrigin: '0% 0%',
    backgroundColor:'red'
  }
  let minuteHandStyle = {
    position: 'relative',
    top: 100,
    left: 100,
    border: '1px solid grey',
    width: '40%',
    height: 3,
    transform: 'rotate(' + ((date.getMinutes() / 60) *360 -90).toString() + 'deg)',
    transformOrigin: '0% 0%',
    backgroundColor:'grey'
  }
  let hourHandStyle = {
    position: 'relative',
    top: 92,
    left: 106,
    border: '1px solid grey',
    width: '20%',
    height: 7,
    transform: 'rotate(' + ((date.getHours() / 12) *360 -90).toString() + 'deg)',
    transformOrigin: '0% 0%',
    backgroundColor:'grey'
  }
  return (
    <div style={dialStyle}>
      <div style={secondHandStyle}/>
      <div style={minuteHandStyle}/>
      <div style={hourHandStyle}/>
    </div>
  )
}

// 상태 저장 컴포넌트
class Time extends Component {
  constructor (props) {
    console.log('constructor time...')
    super(props)
    // callback 함수 호출로 데이터 변경 -> React 변경 감지 -> 렌더링
    this.launchClock()
    this.state = {currentTime: new Date().toLocaleString('en')}
  }
  launchClock() {
    // 1초마다 시간 갱신
    setInterval(()=>{
      console.log('Updating time...')
      this.setState({
        currentTime: new Date().toLocaleString('en')
      })
    },1000)
  }
  render() {
    console.log('Rendering...')
    return (
      <div>
        <AnalogDisplay time={this.state.currentTime}/>
        <DigitalDisplay time={this.state.currentTime}/>
      </div>
    )
  }
}

render(
<Time />, document.getElementById("root"));
