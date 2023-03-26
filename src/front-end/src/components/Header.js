import React from "react";

import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

export default class Header extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="header-box">
                <Box className="header-box-left">
                    <Typography id="links-typograpphy"> Menu </Typography>
                    <Typography ml={3} id="links-typograpphy"> Reservations </Typography>
                </Box>
                <Box className="header-box-logo">
                    <Typography fontSize="25px" id="links-typograpphy"> Restaurant Reservation </Typography>
                </Box>
                <Box className="header-box-right">
                    <Typography mr={3} id="links-typograpphy"> Login </Typography>
                    <Typography id="links-typograpphy"> Sign Up </Typography>
                </Box>
            </Box>
        );
    }
};