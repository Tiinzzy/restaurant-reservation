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

import './staff-styling.scss';

const backend = BackEndConnection.INSTANCE();

const INPUIT_FIELDS = ['id', 'timestamp', 'customer_name', 'customer_id', 'seat_count', 'table_id', 'for_date', 'for_how_long', 'status', 'latest_comment', 'waiter_id', 'reservation_type', 'total_price', 'tip_percent'];

function capitalizeFirst(mySentence) {
    const words = mySentence.split('_');
    for (var w in words) {
        words[w] = words[w][0].toUpperCase() + words[w].substring(1);
    }
    return words.join(' ');
}

export default class EditMenuDialog extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            closeDialog: props.closeDialog,
            reservationId: props.reservationId,
            updateError: false
        }
    }

    componentDidMount() {
        backend.load_reservation(this.state.reservationId, (data) => {
            let that = this;

            Object.keys(data).forEach(k => data[k] = data[k] || '');

            that.setState({ rsvData: data });
        })
    }

    cancelAndClose() {
        this.state.closeDialog();
    }

    saveChanges() {
        let availableChanges = {};
        for (let i in this.state.rsvData) {
            if (this.state.rsvData[i].length > 0 || this.state.rsvData[i] !== '') {
                availableChanges[i] = this.state.rsvData[i];
            }
        }

        backend.update_reservation(availableChanges, (data) => {
            let that = this;
            if (data.result) {
                that.state.closeDialog({ action: 'changes-made-successfully' }, () => {
                    that.componentDidMount();
                });
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
                    <DialogContentText id="alert-dialog-description">
                        The following are current data, type in textfield to change.
                    </DialogContentText>
                </DialogTitle>
                <DialogContent>
                    <Box className="staff-edit-reservation-dialog-box">
                        {this.state.rsvData && INPUIT_FIELDS.map((k, i) => (
                            <Box key={i} p={1}>
                                <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>{capitalizeFirst(k).replaceAll('_', ' ')}: </Typography>
                                <TextField error={this.state.updateError} size="small" variant="outlined" value={this.state.rsvData[k]}
                                    onChange={(e) => this.smartChange(e, k)} className="staff-edit-reservation-textfield" />
                            </Box>
                        ))}
                    </Box>
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
