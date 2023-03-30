import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import Divider from '@mui/material/Divider';

import './user-styling.scss';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const OPTIONS = ['Make Reservation', 'Change Password', 'Edit Profile', 'Reservation History'];

export default class UserHomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            user: props.user,
            openMenu: false,
            anchorEl: null
        }
    }

    logOutUser() {
        backend.authentication_logout(this.state.user, (data) => {
            if (data.success) {
                window.location = '/';
            };
        })
    }

    openMenuDetails(e) {
        this.setState({ openMenu: true, anchorEl: e.currentTarget });
    }

    closeMenuDetails() {
        this.setState({ openMenu: false, anchorEl: null });
    }

    render() {
        return (
            <Box className="user-home-page-main-box">
                <Box className="user-home-page-data-box">
                    <Box className="user-home-page-users-name">
                        <Typography>Hi {this.state.user}, Welcome Back!</Typography>
                        <Box display="flex" flexGrow={1} />
                        <IconButton color="primary" aria-label="menu">
                            <MenuIcon fontSize="large" onClick={(e) => this.openMenuDetails(e)} />
                        </IconButton>

                        <Menu
                            anchorEl={this.state.anchorEl}
                            anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
                            transformOrigin={{ vertical: 'top', horizontal: 'right' }}
                            open={this.state.openMenu}
                            onClose={() => this.closeMenuDetails()}
                            PaperProps={{
                                style: {
                                    maxHeight: 100 * 4.5,
                                    width: '20ch',
                                },
                            }}>
                            {OPTIONS.map((e, i) => (
                                <MenuItem key={i} onClick={() => this.closeMenuDetails()}>
                                    {e}
                                    <Divider />
                                </MenuItem>
                            ))}
                        </Menu>

                    </Box>

                </Box>
            </Box>
        );
    }
};