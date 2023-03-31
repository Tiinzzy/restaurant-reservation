import React from "react";

import Divider from '@mui/material/Divider';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditMenu extends React.Component {

    constructor(props) {
        super(props);
        this.state = {

        }
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Edit Menu</Typography>
                    <Box display="flex" flexGrow={1} />
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
            </Box>
        );
    }
};