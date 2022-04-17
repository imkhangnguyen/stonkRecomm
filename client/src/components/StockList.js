import React, { useState } from 'react';
import Input from './Input';

const StockList = ({ stocks }) => {
  return (
    <div>
      {stocks.map((stock) => {
        return <div className="stock">{stock.symbol}</div>;
      })}
    </div>
  );
};

export default StockList;
