import React from "react";

import Box from '@mui/material/Box';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditOrderDialog extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            clickedData: props.clickedData,
            closeDialog: props.closeDialog,
            count: '',
            reservationId: '',
            orderItemId: '',
            menuItemId: ''
        }
    }

    componentDidMount() {
        this.setState({
            reservationId: this.state.clickedData.reservationId, orderItemId: this.state.clickedData.orderItemId,
            count: this.state.clickedData.count, menuItemId: this.state.clickedData.menuItemId, name: this.state.clickedData.food_name
        });
    }

    getNewCount(e) {
        this.setState({ count: (e.target.value * 1) });
    }

    cancelAndClose() {
        this.state.closeDialog();
    }

    saveChanges() {
        if (this.state.count > 0) {
            let query = { 'reservation_id': this.state.reservationId, 'order_item_id': this.state.orderItemId, 'count': this.state.count };
            backend.update_order_items(query, (data) => {
                if (data.result) {
                    this.state.closeDialog({ action: 'changes-made-successfully', reserveId: this.state.reservationId });
                }
            })
        } else if (this.state.count === 0) {
            let query = { 'reservation_id': this.state.reservationId, 'menu_item_id': this.state.menuItemId, 'order_item_id': this.state.orderItemId };
            backend.delete_order_item(query, (data) => {
                if (data.result) {
                    this.state.closeDialog({ action: 'changes-made-successfully', reserveId: this.state.reservationId });
                }
            })
        }
    }

    render() {
        return (
            <Box>
                <DialogTitle id="alert-dialog-title">
                    {"Edit Order"}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        To delete or change the count.
                    </DialogContentText>
                    <Typography style={{ display: 'flex', justifyContent: 'space-between' }}
                        fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Item Name:
                        <span>
                            {this.state.name}
                        </span>
                    </Typography>
                    <TextField type="number" InputLabelProps={{ shrink: true, }} size="small" style={{ width: 300, marginTop: 15 }}
                        value={this.state.count} onChange={(e) => this.getNewCount(e)} label="Count" variant="standard" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => this.cancelAndClose()} variant="contained">Cancel</Button>
                    <Button onClick={() => this.saveChanges()} variant="contained">
                        Save Changes
                    </Button>
                </DialogActions>
            </Box>
        );
    }
};