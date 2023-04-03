import React from "react";

import Box from '@mui/material/Box';

import BackEndConnection from '../backend-connection/BackEndConnection';

export default class MakeReservation extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="user-home-page-main-box">
               this will be a page for making reservations
            </Box>
        );
    }
};