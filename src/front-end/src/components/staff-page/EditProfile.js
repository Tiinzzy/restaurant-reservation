import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditProfile extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Edit Profile</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">To edit profile, simply change your information and click save.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />

            </Box>
        );
    }
};