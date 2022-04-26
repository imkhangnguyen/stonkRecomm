import React from 'react';

const Results = ({ results }) => {
  return (
    <div className="top-results">
      <h1>Top 3</h1>
      {results.map((result, key) => {
        return (
          <div className="stock-pick">
            <h1 key={key}>
              {key + 1}. {result}
            </h1>
          </div>
        );
      })}
    </div>
  );
};

export default Results;
