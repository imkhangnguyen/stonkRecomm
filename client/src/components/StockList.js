import React, { useState } from 'react';
import {
  CircularProgressbarWithChildren,
  buildStyles,
} from 'react-circular-progressbar';
import Input from './Input';

const StockList = ({ stocks, dict, isTopResults }) => {
  return (
    <div>
      {isTopResults ? <h1>Top 3</h1> : <h1>Stocks Entered</h1>}
      {stocks.map((stock, key) => {
        return (
          <div key={key} className={isTopResults ? 'stock-pick' : 'stock'}>
            <div>{stock}</div>
            <div className="info">
              <h3>Score:</h3>
              <div style={{ width: 100, height: 100 }}>
                <CircularProgressbarWithChildren
                  className="circle"
                  styles={buildStyles({
                    // Whether to use rounded or flat corners on the ends - can use 'butt' or 'round'
                    strokeLinecap: 'round',

                    // Text size
                    textSize: '20px',

                    // Colors
                    pathColor: `rgba(10, 232, 255, ${dict[stock] / 100})`,
                    textColor: '#0a1f21',
                    trailColor: '#f0f0f0',
                    backgroundColor: '#3e98c7',
                  })}
                  value={dict[stock]}
                  text={`${dict[stock]}%`}
                />
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default StockList;
