import React,  { Component } from "react";
import { render } from "react-dom";
import HomePage from './HomePage';
// import CreateRoomPage from './CreateRoomPage';
// import RoomJoinPage from './RoomJoinPage';

export default class App extends Component {
    constructor(props) {
        super(props);
        // this.state = {

        // }
    }

    render() {
        // return <h1>{this.props.name}</h1>;
        // return <HomePage />
        return (<div>
            <HomePage />
            {/* <CreateRoomPage></CreateRoomPage> */}
            {/* <RoomJoinPage></RoomJoinPage> */}
        </div>

        )
    }
}

const appDiv = document.getElementById("app");
render(<App name="Nouvellie React ready."/>, appDiv)