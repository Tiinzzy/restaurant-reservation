import React from "react";

import Box from '@mui/material/Box';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditMenuDialog extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            closeDialog: props.closeDialog,
            reservationId: props.reservationId
        }
        console.log(this.state.reservationId);
    }

    render() {
        return (
            <Box>
                this is to display data for one reservation
            </Box>
        );
    }
};