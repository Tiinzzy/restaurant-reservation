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


const INPUIT_FIELDS = ['id', 'waiter_id', 'reservation_type', 'status', 'for_date', 'timestamp', 'customer_id', 'cutomer_name', 'for_how_long', 'latest_comment', 'seat_count', 'table_id', 'tip_percent', 'total_price'];

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

            Object.keys(data).forEach(k => data[k] = data[k] || '');

            that.setState({ rsvData: data });
            console.log(data)
        })
    }

    cancelAndClose() {
        this.state.closeDialog();
    }

    saveChanges() {
        backend.update_reservation(this.state.rsvData, (data) => {
            let that = this;
            if (data.result) {
                that.state.closeDialog({ action: 'changes-made-successfully' });
            } else {
                that.setState({ updateError: true });
            }
        })
    }

    smartChange(e, key) {
        let data = { ...this.state.rsvData };
        data[key] = e.target.value;
        this.setState({ rsvData: data });
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
                    {this.state.rsvData && INPUIT_FIELDS.map((k, i) => (
                        <Box key={i} p={1}>
                            <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>{k.replaceAll('_', ' ')}: </Typography>
                            <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.rsvData[k]}
                                onChange={(e) => this.smartChange(e, k)} className="menu-item-detail-text" />
                        </Box>
                    ))}

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