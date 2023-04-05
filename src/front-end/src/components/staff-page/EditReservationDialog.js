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
            reservationId: props.reservationId
        }
    }

    componentDidMount() {
        backend.load_reservation(this.state.reservationId, (data) => {
            let that = this;
            that.setState({ data });
        })
    }

    cancelAndClose() {
        this.state.closeDialog();
    }

    saveChanges() {
        this.state.closeDialog();
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
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Name: </Typography>
                    {this.state.data && this.state.data.map((e, i) => (
                        <Box key={i} >
                        {e.id}
                        </Box>))}
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => this.cancelAndClose()}>Cancel</Button>
                    <Button onClick={() => this.saveChanges()} autoFocus>
                        Save Changes
                    </Button>
                </DialogActions>
            </Box>
        );
    }
};