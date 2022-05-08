import { useState } from 'react';
import axios from "axios";

function Login(props) {

  const [loginForm, setloginForm] = useState({
    name: "",
    email: "",
    password: ""
  })

  function logMeIn(event) {
    axios({
      method: "POST",
      url: "http://127.0.0.1:5000/login",
      data: {
        name: loginForm.name,
        email: loginForm.email,
        password: loginForm.password

      }
    })
      .then((response) => {
        props.setToken(response.data.access_token)
      }).catch((error) => {
        if (error.response) {
          alert(error.response.data)
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
        }
      })

    setloginForm(({
      name: "",
      email: "",
      password: ""
    }))

    event.preventDefault()
  }

  function handleChange(event) {
    const { value, name } = event.target
    setloginForm(prevNote => ({
      ...prevNote, [name]: value
    })
    )
  }

  return (
    <div>
      <h1>Login</h1>
      <form className="login">
        <input onChange={handleChange}
          type="name"
          text={loginForm.name}
          name="name"
          placeholder="name"
          value={loginForm.name} />
        <input onChange={handleChange}
          type="email"
          text={loginForm.email}
          name="email"
          placeholder="Email"
          value={loginForm.email} />
        <input onChange={handleChange}
          type="password"
          text={loginForm.password}
          name="password"
          placeholder="Password"
          value={loginForm.password} />

        <button onClick={logMeIn}>Submit</button>
      </form>
    </div>
  );
}

export default Login;