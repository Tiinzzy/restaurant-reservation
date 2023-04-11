import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

import EditProfile from "./EditProfile";
import MakeReservation from "./MakeReservation";
import AllReservations from "./AllReservations";
import MakeOrder from "./MakeOrder";

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const OPTIONS = ['All Reservations', 'Make Reservation', 'Make an Order', 'Edit Profile'];

export default class WaiterHomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            user: props.user,
            openMenu: false,
            anchorEl: null,
            selectedMenuItem: ''
        }
    }

    componentDidMount() {
        backend.load_user_by_email(this.state.user.username, (data) => {
            let that = this;
            that.setState({ usersName: data.name })
        })
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
                        <Typography>Hi {this.state.usersName}, Welcome Back!</Typography>
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
                    {this.state.selectedMenuItem === 'All Reservations' && <AllReservations />}
                    {this.state.selectedMenuItem === 'Make Reservation' && <MakeReservation />}
                    {this.state.selectedMenuItem === 'Make an Order' && <MakeOrder />}
                    {this.state.selectedMenuItem === 'Edit Profile' && <EditProfile user={this.state.user} />}
                </Box>
            </Box>
        );
    }
};