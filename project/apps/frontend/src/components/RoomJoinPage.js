import React, { Component } from "react";
import { TextField, Button, Grid, Typography } from "@material-ui/core";
import { Link } from "react-router-dom";

export default class RoomJoinPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            roomCode: "",
            error: ""
        }
        this.handelTextFieldChange = this.handelTextFieldChange.bind(this);
        this.roomButtonPressed = this.roomButtonPressed.bind(this);
    }

    render() {
        return (
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography variant="h4" component="h4">
                        Join A Room
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <TextField 
                        error="error"
                        label="Code"
                        placehold="Enter a Room Code"
                        value={this.state.roomCode}
                        helperText={this.state.error}
                        variant="outlined"
                        onChange={this.handelTextFieldChange}
                    ></TextField>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="primary" onClick={this.roomButtonPressed}>
                        Enter Room
                    </Button>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button variant="contained" color="secondary" to="/room" component={Link}>
                        Back
                    </Button>
                </Grid>
            </Grid>
        );
    }

     handelTextFieldChange(e) {
        this.setState({
            roomCode: e.target.value
        });
    }

    roomButtonPressed() {
        console.log(this.state.roomCode)
    }
}