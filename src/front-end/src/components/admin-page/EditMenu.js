import React from "react";

import Divider from '@mui/material/Divider';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

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
                <Box style={{ display: 'flex', flexDirection: 'row', marginBottom: 40 }}>
                    <Box className="user-page-reservation-form-1">
                        <Typography fontSize={14} variant="body1" mb={.5}>Name: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getFoodName(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Category: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getCategory(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Price: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getPrice(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Description: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getDescription(e)} />
                        <Button onClick={() => this.createNewUserAccount()} variant="contained">Submit</Button>

                    </Box>
                    <Box display="flex" flexGrow={1} />
                    <Box className="user-page-reservation-form">
                        this is for editing pre-existing menu items
                    </Box>
                </Box>
            </Box>
        );
    }
};