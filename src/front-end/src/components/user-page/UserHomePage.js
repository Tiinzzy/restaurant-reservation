import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

import EditProfile from "./EditProfile";
import MakeReservation from "./MakeReservation";
import ReservationHistory from "./ReservationHistory";
import ViewMenu from "./ViewMenu";

import './user-styling.scss';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const OPTIONS = ['Make Reservation', 'Reservation History', 'View Menu', 'Edit Profile'];

export default class UserHomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            user: props.user,
            openMenu: false,
            anchorEl: null,
            changePage: ''
        }
        this.callBack = this.callBack.bind(this);
    }

    openMenuDetails(e) {
        this.setState({ openMenu: true, anchorEl: e.currentTarget });
    }

    closeMenuDetails(val) {
        this.setState({ openMenu: false, anchorEl: null, val, changePage: '' });
    }

    callBack(data) {
        if (data.action === 'button-clicked-for-reservation') {
            this.setState({ changePage: 'Make Reservation' });
        };
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
                    {(this.state.changePage === '' && this.state.val === 'Edit Profile') && <EditProfile user={this.state.user} />}
                    {(this.state.changePage === 'Make Reservation' || this.state.val === 'Make Reservation') && <MakeReservation />}
                    {(this.state.changePage === '' && this.state.val === 'Reservation History') && <ReservationHistory />}
                    {(this.state.changePage === '' && this.state.val === 'View Menu') && <ViewMenu callBack={this.callBack} />}
                </Box>
            </Box>
        );
    }
};