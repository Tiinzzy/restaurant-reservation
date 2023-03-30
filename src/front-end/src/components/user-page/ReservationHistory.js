import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';


import './user-styling.scss';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();


export default class ReservationHistory extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Typography fontSize={20} fontWeight="bold" mb={2}>Reservation History</Typography>
                <Divider style={{marging:10}}/>
                <Typography fontSize={16} variant="body1" mt={2}>Lisr of old, new and current reservation histories.</Typography>
            </Box>
        );
    }
};