import React from "react";

import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

import BackEndConnection from '../components/backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class HeaderLogin extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            user: props.user
        }
    }

    openUserHomePage() {
    }

    logUserOut() {
        backend.authentication_logout(this.state.user, (data) => {
            if (data.success) {
                window.location = '/';
            };
        })
    }


    render() {
        return (
            <Box className="header-box">
                <Box className="header-box-left">
                    <Typography id="links-typograpphy" onClick={() => this.openUserHomePage()}> Home </Typography>
                </Box>
                <Box className="header-box-logo">
                    <Typography fontSize="25px" id="links-typograpphy"> Restaurant Reservation </Typography>
                </Box>
                <Box className="header-box-right">
                    <Typography id="links-typograpphy" onClick={() => this.logUserOut()}> Log Out </Typography>
                </Box>
            </Box>
        );
    }
};