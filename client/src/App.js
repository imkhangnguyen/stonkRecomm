import './App.css';
import { useState } from 'react';
import Input from './components/Input';
import StockList from './components/StockList';
import axios from 'axios';

function App() {
  const [stocks, setStocks] = useState([]);

  const addStock = (stock) => {
    const newStocks = [stock, ...stocks];
    setStocks(newStocks);
    console.log(stock);
  };

  const getRecomm = async () => {
    const res = await axios.get(
      'https://api.polygon.io/v3/reference/tickers?active=true&sort=ticker&order=asc&limit=10&apiKey=cnoCmpcsXDv6vDdj17wIcrYrd3PJGFUI'
    );
    const arr = res.data.results;
    const newStocks = [];
    arr.forEach((item) => {
      newStocks.push(item.ticker);
    });
    console.log(newStocks);
    setStocks(newStocks);
  };
  return (
    <div className="App">
      <header className="App-header">
        <h1>StonkRecomm</h1>
      </header>
      <Input handleAddStock={addStock} />
      <button onClick={getRecomm}>Recommend</button>
      <StockList stocks={stocks} />
    </div>
  );
}

export default App;
