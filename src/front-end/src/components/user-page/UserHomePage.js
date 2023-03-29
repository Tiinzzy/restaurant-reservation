import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class UserHomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '',
            showPassword: false,
            user: props.user
        }
    }

    logOutUser() {
        backend.authentication_logout(this.state.user, (data) => {
            if(data.success){
                window.location = '/';
            };
        })
    }


    render() {
        return (
            <Box>
                <Typography>This will be users home page. test</Typography>
                <Button variant="contained" onClick={() => this.logOutUser()}>LogOut</Button>
            </Box>
        );
    }
};