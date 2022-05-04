import React from 'react';
import { Navbar, Container, Nav } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';
const navbarStyle = {
  backgroundColor: '#333126',
};

const Header = ({ title }) => {
  return (
    <Navbar style={navbarStyle} variant="dark">
      <Container>
        <Logo alt={title} style={{ maxWidth: '16rem', maxHeight: '2rem' }} />
      </Container>
    </Navbar>
  );
};

export default Header;
