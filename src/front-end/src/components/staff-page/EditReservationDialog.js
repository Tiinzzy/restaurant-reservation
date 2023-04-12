import React from "react";

import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditMenuDialog extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            closeDialog: props.closeDialog,
            reservationId: props.reservationId,
            updateError: false,
            customerName: '',
            customerId: '',
            date: '',
            duration: '',
            comment: '',
            reservationType: '',
            numberOfPeople: '',
            status: '',
            tableId: '',
            waiterId: '',
            tip: '',
            total: '',
            time: ''
        }
    }

    componentDidMount() {
        backend.load_reservation(this.state.reservationId, (data) => {
            let that = this;
            that.setState({
                customerName: data.cutomer_name, customerId: data.customer_id, date: data.for_date, duration: data.for_how_long, comment: data.latest_comment,
                reservationType: data.reservation_type, numberOfPeople: data.seat_count, status: data.status, tableId: data.table_id, waiterId: data.waiter_id,
                tip: data.tip_percent, total: data.total_price, time: data.timestamp
            });
        })
    }

    getCustomerName(e) {
        this.setState({ customerName: e.target.value, updateError: false });
    }

    getCustomerId(e) {
        this.setState({ customerId: e.target.value, updateError: false });
    }

    getDate(e) {
        this.setState({ date: e.target.value, updateError: false });
    }

    getTime(e) {
        this.setState({ time: e.target.value, updateError: false });
    }

    getDuration(e) {
        this.setState({ duration: e.target.value, updateError: false });
    }

    getComments(e) {
        this.setState({ comment: e.target.value, updateError: false });
    }

    getReservationType(e) {
        this.setState({ reservationType: e.target.value, updateError: false });
    }

    getSeatCount(e) {
        this.setState({ numberOfPeople: e.target.value, updateError: false });
    }

    getTableId(e) {
        this.setState({ tableId: e.target.value, updateError: false });
    }

    getStatus(e) {
        this.setState({ status: e.target.value, updateError: false });
    }

    getWaiterId(e) {
        this.setState({ waiterId: e.target.value, updateError: false });
    }

    getTipPercent(e) {
        this.setState({ tip: e.target.value, updateError: false });
    }

    getTotalPrice(e) {
        this.setState({ total: e.target.value, updateError: false });
    }

    cancelAndClose() {
        this.state.closeDialog();
    }

    saveChanges() {
        let query = {
            'id': this.state.reservationId, 'for_how_long': this.state.duration, 'customer_name': this.state.customerName, 'customer_id': this.state.customerId, 'seat_count': this.state.numberOfPeople,
            'table_id': this.state.tableId, 'for_date': this.state.date, 'timestamp': this.state.time, 'status': this.state.status, 'latest_comment': this.state.comment, 'waiter_id': this.state.waiterId,
            'reservation_type': this.state.reservationType, 'total_price': this.state.total, 'tip_percent': this.state.tip
        }
        backend.update_reservation(query, (data) => {
            let that = this;
            if (data.result) {
                that.state.closeDialog({ action: 'changes-made-successfully' });
            } else {
                that.setState({ updateError: true });
            }
        })
    }

    render() {
        return (
            <Box>
                <DialogTitle id="alert-dialog-title">
                    {"Edit Reservation #" + this.state.reservationId}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        The following are current data, type in textfield to change.
                    </DialogContentText>
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Customer Name: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.customerName && this.state.customerName}
                        onChange={(e) => this.getCustomerName(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Customer ID: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.customerId && this.state.customerId}
                        onChange={(e) => this.getCustomerId(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Date: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.date && this.state.date}
                        onChange={(e) => this.getDate(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Time: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.time && this.state.time}
                        onChange={(e) => this.getTime(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Duration: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.duration && this.state.duration}
                        onChange={(e) => this.getDuration(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Comments: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.comment && this.state.comment}
                        onChange={(e) => this.getComments(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Reservation Type: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.reservationType && this.state.reservationType}
                        onChange={(e) => this.getReservationType(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Number of People: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.numberOfPeople && this.state.numberOfPeople}
                        onChange={(e) => this.getSeatCount(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Table ID: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.tableId && this.state.tableId}
                        onChange={(e) => this.getTableId(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Status: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.status && this.state.status}
                        onChange={(e) => this.getStatus(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Waiter ID: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.waiterId && this.state.waiterId}
                        onChange={(e) => this.getWaiterId(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Tip Percent: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.tip && this.state.tip}
                        onChange={(e) => this.getTipPercent(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Total: </Typography>
                    <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.total && this.state.total}
                        onChange={(e) => this.getTotalPrice(e)} className="menu-item-detail-text" />
                </DialogContent >
                <DialogActions>
                    <Button onClick={() => this.cancelAndClose()} variant="contained">Cancel</Button>
                    <Button onClick={() => this.saveChanges()} variant="contained">
                        Save Changes
                    </Button>
                </DialogActions>
            </Box >
        );
    }
};