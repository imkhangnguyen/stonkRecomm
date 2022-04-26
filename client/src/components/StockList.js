import React, { useState } from 'react';
import Input from './Input';

const StockList = ({ stocks, dict }) => {
  return (
    <div>
      <h1>Stocks Entered</h1>
      {stocks.map((stock, key) => {
        return (
          <div key={key} className="stock">
            <div>{stock}</div>
            <div style={{ color: 'gray' }}>Score: {dict[stock]}</div>
          </div>
        );
      })}
    </div>
  );
};

export default StockList;
