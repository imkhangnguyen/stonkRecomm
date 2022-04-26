import './App.css';
import { useState } from 'react';
import Input from './components/Input';
import StockList from './components/StockList';
import axios from 'axios';

function App() {
  const [stocks, setStocks] = useState([]);
  const [results, setResults] = useState([]);
  const [rankDict, setRankDict] = useState({});
  const [priceDict, setPriceDict] = useState({});
  const [loading, setLoading] = useState(false);
  const [ready, setReady] = useState(false);
  const [err, setErr] = useState(false);

  const setStockList = async (stocks) => {
    setStocks(stocks);
    if (stocks.length < 3) {
      setErr(true);
      return;
    } else setErr(false);
    setLoading(true);
    const { data } = await axios.post('http://127.0.0.1:5000', stocks);
    setLoading(false);
    setReady(true);
    setResults(data[0]);
    setRankDict(data[1]);
    console.log(data[2]);
    setPriceDict(data[2]);
    console.log(data);
    console.log(results);
  };

  const getPrice = async (stocks) => {
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
        <h1 style={{ fontSize: '3em' }} className="title">
          StonkRecomm
        </h1>
      </header>

      <Input handleAddStocks={setStockList} />
      {err && <h3 style={{ color: 'red' }}>Error: Enter at least 3 stocks</h3>}
      {loading && <h1>Fetching Results...</h1>}
      {ready && (
        <StockList
          stocks={results}
          dict={rankDict}
          prices={priceDict}
          isTopResults={true}
        />
      )}
      {ready && (
        <StockList
          stocks={stocks}
          dict={rankDict}
          prices={priceDict}
          isTopResults={false}
        />
      )}
    </div>
  );
}

export default App;
