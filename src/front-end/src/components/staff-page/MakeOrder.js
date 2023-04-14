import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import TextField from '@mui/material/TextField';
import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
import Dialog from '@mui/material/Dialog';

import EditOrderDialog from "./EditOrderDialog";

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class MakeOrder extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            reservationId: '',
            count: '',
            changesMade: false,
            openSnack: false,
            changeError: false,
            openDialog: false,
            buttonOff: true
        }
        this.handleCloseDialog = this.handleCloseDialog.bind(this);
    }

    componentDidMount(reserveId) {
        backend.all_menu_items((data) => {
            let that = this;
            that.setState({ data });
        });

        backend.all_order_items(reserveId, (data) => {
            let that = this;
            that.setState({ allOrderItems: data });
        })
    }

    getReservationId(e) {
        this.setState({ reservationId: e.target.value || e }, () => {
            backend.all_order_items(this.state.reservationId, (data) => {
                let that = this;
                that.setState({ allOrderItems: data, buttonOff: false });
            })
        });
    }

    getMenuItemCount(e) {
        this.setState({ count: (e.target.value * 1) });
    }

    addToReservationOrder(menuItemId) {
        let query = { 'reservation_id': this.state.reservationId, 'menu_item_id': menuItemId, 'count': this.state.count };
        if (this.state.count === 0 || this.state.count === null || this.state.count.length === 0 || this.state.count === '') {
            this.setState({ changesMade: true, openSnack: true, changeError: true, count: '' });
        } else {
            backend.add_order_item(query, (data) => {
                let that = this;
                if (data.result) {
                    that.setState({ changesMade: true, openSnack: true, count: '' }, () => {
                        this.componentDidMount(this.state.reservationId);
                    });
                } else {
                    that.setState({ changesMade: true, openSnack: true, changeError: true, count: '' });
                }
            })
        }
    }

    closeAlert() {
        this.setState({ openSnack: false, changeError: false });
    }

    handleOpenDialog(data) {
        this.setState({ openDialog: true, clickedData: data });
    }

    handleCloseDialog(data) {
        if (data && data.action === 'changes-made-successfully') {
            this.setState({ openDialog: false, changesMade: true, openSnack: true });
            this.componentDidMount(data.reserveId);
        }
        this.setState({ openDialog: false });
    }

    render() {
        return (
            <Box className="satff-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Make an Order</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">To make an order, just click on the + to add.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                <Box style={{ display: 'flex', flexDirection: 'row' }}>
                    <Box className="staff-page-make-order-menu-box-left">
                        <Typography fontSize={14} variant="body1" mb={.5}>Enter Reservation ID: </Typography>
                        <TextField size="small" variant="outlined"
                            onChange={(e) => this.getReservationId(e)} />
                        <table width="100%">
                            <tbody>
                                <tr>
                                    <th>Reservation ID</th>
                                    <th>Item Name</th>
                                    <th>Count</th>
                                </tr>
                                {this.state.allOrderItems && this.state.allOrderItems.map((e, i) => (
                                    <tr id="td-menu-item-id"
                                        key={i} onClick={() => this.handleOpenDialog({ 'reservationId': e.reservation_id, 'orderItemId': e.order_item_id, 'count': e.count, 'menuItemId': e.menu_item_id, 'food_name': e.name })}>
                                        <td>
                                            {e.reservation_id}
                                        </td>
                                        <td>
                                            {e.name}
                                        </td>
                                        <td>
                                            {e.count}
                                        </td>
                                    </tr>))}
                            </tbody>
                        </table>
                    </Box>
                    <Box className="staff-page-make-order-menu-box-right">
                        {this.state.data && this.state.data.map((e, i) => (
                            <Box key={i}>
                                <Box style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-betwee', alignItems: 'center' }}>
                                    <Typography fontFamily="serif" fontWeight="bold" fontSize="1em" color="rgb(37, 37, 37)"> <span style={{ marginRight: 5 }}>{e.id}</span>{e.name}</Typography>
                                    <Box display="flex" flexGrow={1} />
                                    <span style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                                        <span fontFamily="serif" color="rgb(37, 37, 37)">${e.price}</span>
                                        <TextField variant="outlined" style={{ width: '50px', marginLeft: 10, marginTop: 10 }} onChange={(e) => this.getMenuItemCount(e)} />
                                        <IconButton onClick={() => this.addToReservationOrder(e.id)} disabled={this.state.buttonOff}>
                                            <AddCircleOutlineIcon />
                                        </IconButton>
                                    </span>
                                </Box>
                                <Typography fontFamily="serif" fontSize=".8em" color="rgb(94, 94, 94)">{e.description}</Typography>
                                <Divider />
                            </Box>))}
                    </Box>
                </Box>
                {this.state.changesMade === true &&
                    <Snackbar open={this.state.openSnack} onClose={() => this.closeAlert()} autoHideDuration={5000} anchorOrigin={{ vertical: "top", horizontal: "center" }}>
                        <Alert severity={this.state.changeError === true ? "error" : "success"}>
                            {this.state.changeError === true ? 'Sorry, Something Went Wrong!' : 'Changes Made Successfully!'}
                        </Alert>
                    </Snackbar>}

                <Dialog open={this.state.openDialog} onClose={() => this.handleCloseDialog()} size="md">
                    <EditOrderDialog clickedData={this.state.clickedData} closeDialog={this.handleCloseDialog} />
                </Dialog>
            </Box>
        );
    }
};