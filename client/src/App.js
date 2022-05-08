import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './components/Login'
import Header from './components/Header'
import useToken from './components/useToken'
import Stockget from './components/Stockget'
import Register from './components/Register'
import './App.css'

function App() {
  const { token, removeToken, setToken } = useToken();

  return (
    <BrowserRouter>
      <div className="App">
        {!token && token!=="" &&token!== undefined?  
        <>
          <Login setToken={setToken} />
          <Register setToken={setToken} />
        </>

        :(
          <>
            <Header token={removeToken}/>
            <Stockget token={token} setToken={setToken}/>
        </>
         )}
      </div>
    </BrowserRouter>
  );
}

export default App;