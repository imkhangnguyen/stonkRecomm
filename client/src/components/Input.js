import React, { useState } from 'react';

const Input = ({ handleAddStock }) => {
  const [input, setInput] = useState('');

  const handleChange = (e) => {
    setInput(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input) return;
    handleAddStock({ id: Math.floor(Math.random() * 100000), symbol: input });
    setInput('');
  };
  return (
    <form className="input-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter a symbol"
        value={input}
        name="text"
        className="stock-input"
        onChange={handleChange}
        autoComplete="off"
      />
      <button className="submit-button">+</button>
    </form>
  );
};

export default Input;
