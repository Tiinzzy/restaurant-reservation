import React from "react";

import Box from '@mui/material/Box';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditOrderDialog extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box>
                This will be dialog for editing order item
            </Box>
        );
    }
};