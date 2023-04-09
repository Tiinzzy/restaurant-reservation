import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

import AddStaff from "./AddStaff";
import EditMenu from "./EditMenu";

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const OPTIONS = ['Add Staff', 'Edit Menu'];

export default class AdminHomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            user: props.user,
            openMenu: false,
            anchorEl: null,
            selectedMenuItem: ''
        }
    }

    openMenuDetails(e) {
        this.setState({ openMenu: true, anchorEl: e.currentTarget });
    }

    closeMenuDetails(val) {
        this.setState({ openMenu: false, anchorEl: null, selectedMenuItem: val });
    }

    render() {
        return (
            <Box className="user-home-page-main-box">
                <Box className="user-home-page-data-box">
                    <Box className="user-home-page-users-name">
                        <Typography>Hi {this.state.user.username}, Welcome Back!</Typography>
                        <Box display="flex" flexGrow={1} />
                        <IconButton color="primary" aria-label="menu" onClick={(e) => this.openMenuDetails(e)} >
                            <MenuIcon fontSize="large" />
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
                                    width: '22ch',
                                },
                            }}>
                            {OPTIONS.map((val) => (
                                <MenuItem key={val} onClick={() => this.closeMenuDetails(val)}>
                                    {val}
                                </MenuItem>
                            ))}
                        </Menu>
                    </Box>
                    {this.state.selectedMenuItem === 'Add Staff' && <AddStaff />}
                    {this.state.selectedMenuItem === 'Edit Menu' && <EditMenu />}

                </Box>
            </Box>
        );
    }
};