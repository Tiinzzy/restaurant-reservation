import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';

import BackEndConnection from '../backend-connection/BackEndConnection';

export default class MakeReservation extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Make Reservation</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">To make a reservation please fill out the form bellow.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />

            </Box>
        );
    }
};