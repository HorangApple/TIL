import React from "react";
import styled from "styled-components";

const Link = ({className, children}) => (
  <a className={className}>
    {children}
  </a>
);

const StyledLink = styled(Link)`
  color: palevioletred;
  font-weight: bold;
`;

const Box = () => (
  <div>
    <Link>Unstyled Link</Link>
    <br />
    <StyledLink>Styled Link</StyledLink>
  </div>
)
export default Box;
