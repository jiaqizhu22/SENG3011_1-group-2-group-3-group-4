import React from 'react';
import PropTypes from 'prop-types';

const Button = ({ displayText, onClick }) => {
  return (
    <button onClick={onClick}>&displayText;</button>
  );
};

Button.propTypes = {
  onClick: PropTypes.func,
};

export default Button;