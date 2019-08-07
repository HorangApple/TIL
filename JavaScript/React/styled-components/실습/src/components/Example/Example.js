import React from "react";
import styled, {keyframes} from "styled-components";

// Create the keyframes
const rotate = keyframes`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`;

const Rotate = styled.div`
  display: inline-block;
  animation: ${rotate} 2s linear infinite;
  padding: 2rem 1rem;
  font-size: 1.2rem;
`;

const Example = () => (
  <Rotate>&lt; 💅 &gt;</Rotate> // &lt;, &gt;는 간접 표현식
);

export default Example;
