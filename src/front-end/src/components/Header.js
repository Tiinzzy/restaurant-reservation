import React from "react";

import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

export default class Header extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    openMenuPage() {
        window.location = '/menu';
    }

    openReservationPage() {
        window.location = '/reservation';
    }

    openHomepage() {
        window.location = '/';
    }

    openLoginPage() {
        window.location = '/login';
    }

    openSignupPage() {
        window.location = '/signup';
    }

    render() {
        return (
            <Box className="header-box">
                <Box className="header-box-left">
                    <Typography id="links-typograpphy" onClick={() => this.openMenuPage()}> Menu </Typography>
                    <Typography ml={3} id="links-typograpphy" onClick={() => this.openReservationPage()}> Reservations </Typography>
                </Box>
                <Box className="header-box-logo">
                    <Typography fontSize="25px" id="links-typograpphy" onClick={() => this.openHomepage()}> Restaurant Reservation </Typography>
                </Box>
                <Box className="header-box-right">
                    <Typography mr={3} id="links-typograpphy" onClick={() => this.openLoginPage()}> Login </Typography>
                    <Typography id="links-typograpphy" onClick={() => this.openSignupPage()}> Sign Up </Typography>
                </Box>
            </Box>
        );
    }
};