import React from "react";

import Box from '@mui/material/Box';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class MakeOrder extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="user-home-page-main-box">
              this will be a page for making orders
            </Box>
        );
    }
};