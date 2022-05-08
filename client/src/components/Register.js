import { useState } from 'react';

import axios from "axios";


function Register(props) {

    const [registerForm, setregisterForm] = useState({
        name: "",
        email: "",
        password: ""
    })

    function logMeIn(event) {
        axios({
            method: "POST",
            url: "http://127.0.0.1:5000/register",
            data: {
                name: registerForm.name,
                email: registerForm.email,
                password: registerForm.password

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

        setregisterForm(({
            name: "",
            email: "",
            password: ""
        }))

        event.preventDefault()
    }

    function handleChange(event) {
        const { value, name } = event.target
        setregisterForm(prevNote => ({
            ...prevNote, [name]: value
        })
        )
    }

    return (
        <div>
            <h1 q>Register</h1>
            <form className="register">
                <input onChange={handleChange}
                    type="name"
                    text={registerForm.name}
                    name="name"
                    placeholder="name"
                    value={registerForm.name} />
                <input onChange={handleChange}
                    type="email"
                    text={registerForm.email}
                    name="email"
                    placeholder="Email"
                    value={registerForm.email} />
                <input onChange={handleChange}
                    type="password"
                    text={registerForm.password}
                    name="password"
                    placeholder="Password"
                    value={registerForm.password} />

                <button onClick={logMeIn}>Submit</button>
            </form>
        </div>
    );
}

export default Register;
