import React from "react";

import Box from '@mui/material/Box';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';
import Button from '@mui/material/Button';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditOrderDialog extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            clickedData: props.clickedData
        }
    }

    componentDidMount() {
        this.setState({ reservationId: this.state.clickedData.reservationId, orderItemId: this.state.clickedData.orderItemId, count: this.state.clickedData.count });
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
                        fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Order Item Id:
                        <span>
                            {this.state.orderItemId}
                        </span>
                    </Typography>
                    <Typography style={{ display: 'flex', justifyContent: 'space-between' }}
                        fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Count:
                        <span>
                            <IconButton style={{ marginRight: 10 }} onClick={() => this.reduceTheCount()}>
                                <RemoveCircleOutlineIcon />
                            </IconButton>
                            {this.state.count}
                            <IconButton style={{ marginLeft: 10 }} onClick={() => this.increaseTheCount()}>
                                <AddCircleOutlineIcon />
                            </IconButton>
                        </span>
                    </Typography>
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