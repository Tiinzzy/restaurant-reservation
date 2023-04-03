import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import TextField from '@mui/material/TextField';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class MakeOrder extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            reservationId: '',
            count: ''
        }
    }

    componentDidMount() {
        backend.all_menu_items((data) => {
            let that = this;
            that.setState({ data });
        })
    }

    getReservationId(e) {
        this.setState({ reservationId: e.target.value });
    }

    getMenuItemCount(e) {
        this.setState({ count: e.target.value });
    }

    addToReservationOrder(menuItemId) {
        console.log(this.state.count, 'count');
        console.log(this.state.reservationId, 'reservation id');
        console.log(menuItemId);
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Make an Order</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">To make an order, just click on the + to add.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                <Box style={{ display: 'flex', flexDirection: 'row' }}>
                    <Box className="user-page-reservation-form-4">
                        <Typography fontSize={14} variant="body1" mb={.5}>Enter Reservation ID: </Typography>
                        <TextField size="small" variant="outlined"
                            onChange={(e) => this.getReservationId(e)} />
                    </Box>
                    <Box className="user-page-reservation-form-4">
                        {this.state.data && this.state.data.map((e, i) => (
                            <Box key={i}>
                                <Box style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-betwee', alignItems: 'center' }}>
                                    <Typography fontFamily="serif" fontWeight="bold" fontSize="1em" color="rgb(37, 37, 37)">{e.name}</Typography>
                                    <Box display="flex" flexGrow={1} />
                                    <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                                        <span fontFamily="serif" color="rgb(37, 37, 37)">${e.price}</span>
                                        <IconButton onClick={() => this.addToReservationOrder(e.id)}>
                                            <AddCircleOutlineIcon />
                                        </IconButton>
                                        <TextField variant="outlined" style={{ width: '50px' }} onChange={(e) => this.getMenuItemCount(e)} />
                                    </span>
                                </Box>
                                <Typography fontFamily="serif" fontSize=".8em" color="rgb(94, 94, 94)">{e.description}</Typography>
                                <Divider />
                            </Box>))}
                    </Box>
                </Box>
            </Box>
        );
    }
};