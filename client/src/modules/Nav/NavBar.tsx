import React from 'react';
import { Menu } from 'semantic-ui-react'
import { NavLink } from 'react-router-dom';

const NavBar = () => (
  <Menu>
    <Menu.Item>CFB Simulations Website</Menu.Item>
    <Menu.Item as={NavLink} to="/home" style={{ marginLeft: '20px' }}>Home</Menu.Item>
    <Menu.Item as={NavLink} to="/team-ratings">Team Ratings</Menu.Item>
    <Menu.Item as={NavLink} to="/simulate">Simulation Table</Menu.Item>
    <Menu.Item>FAQ</Menu.Item>
  </Menu>
);

export default NavBar;
