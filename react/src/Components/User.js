import axios from 'axios'
import React from 'react'

function UserItem(props) {
    const deleteUserHandler = (name) => {
    axios.delete(`http://localhost:8000/delete/user/${name}`)
        .then(res => console.log(res.data)) }
  
    return (
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline' }}>{props.user.name} : </span> {props.user.location} 
                <button onClick={() => deleteUserHandler(props.user.name)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default UserItem;