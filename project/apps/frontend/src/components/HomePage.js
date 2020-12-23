import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import Room from "./Room";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route path="/room/join" component={RoomJoinPage} />
          <Route path="/room/create" component={CreateRoomPage} />
          <Route path="/room/:roomCode" component={Room} />
          <Route exact path="/room"><p>Test Home Page JS</p></Route>
          {/* <Route path="/"><p>Test Home Page (Without exact)</p></Route> */}
        </Switch>
      </Router>
    );
  }
}