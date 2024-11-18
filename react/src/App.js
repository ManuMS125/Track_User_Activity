import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import UserView from './Components/UserListView';
 

function App() {

  const [userList, setUserList] = useState([{}])
  const [name, setName] = useState('')
  const [loc, setLoc] = useState('')
  const [hobby, setHobby] = useState('')

  //Read all users
  useEffect(()=>{
    axios.get('http://localhost:8000/get/user')
    .then(res =>{
      setUserList(res.data)
    })
  });

  //post a user
  const addUserHandler = () => {
    axios.post('http://localhost:8000/create/user', {'name': name, 'location': loc, 'hobby': hobby})
    .then(res => console.log(res))
  };



  return (
    
    <div className='App list-group-item justify-content-center
    align-items-center mx-auto' style={{'width':'400px',
      'backgroundColor':'white','marginTop':'15px'}}>
    <h1 className='card text-white bg-primary mb-1'
    styleName='max-width: 20rem;'>Track User Activity</h1>
    <h6 className='card text-white bg-primary mb-3'>
    FastAPI - React - MongoDB</h6>
    <div className='card-body'>
    <h5 className='card text-white bg-dark mb-3'>Add user details</h5>
      <span className='card-text'>
        <input className='mb-2 form-control nameIn' onChange={event => setName(event.target.value)}placeholder='Name'/>
        <input className='mb-2 form-control locIn' onChange={event => setLoc(event.target.value)} placeholder='Location'/>
        <input className='mb-2 form-control hobbyIn' onChange={event => setHobby(event.target.value)}placeholder='Hobby'/>
        <button className='btn btn-outline-primary mx-2 mb-3' style={
          {'borderRadius':'50px','font-weight':'bold'}} onClick={
            addUserHandler}>Add User </button>
        
        
      </span>
    
    <h5 className='card text-white bg-dark mb-3'>Users</h5>
    <div>
    <UserView userList={userList} />
    </div>
    

    
    </div>

    <h6 className='card text-dark bg-warning py-1 mb-0'>Copyright
      2024, All rights reserved &copy;</h6>
    </div>
    
  
  );
}

export default App;
