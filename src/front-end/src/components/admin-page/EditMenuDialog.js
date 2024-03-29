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
            menuItemId: props.menuItemId,
            handleCloseDialog: props.handleCloseDialog,
            id: '',
            name: '',
            category: '',
            price: '',
            description: ''
        }
        this.cancelAndClose = this.cancelAndClose.bind(this);
    }

    componentDidMount() {
        backend.load_menu_item(this.state.menuItemId, (data) => {
            let that = this;
            that.setState({ id: data.id, name: data.name, category: data.category, price: data.price, description: data.description });
        })
    }

    getFoodName(e) {
        this.setState({ name: e.target.value });
    }

    getCategory(e) {
        this.setState({ category: e.target.value });
    }

    getPrice(e) {
        this.setState({ price: e.target.value });
    }

    getDescription(e) {
        this.setState({ description: e.target.value });
    }

    cancelAndClose() {
        this.state.handleCloseDialog();
    }

    deleteAndClose() {
        backend.delete_menu_item(this.state.id, (data) => {
            if (data.result === true) {
                this.state.handleCloseDialog({ action: 'changes-has-been-made' });
            }
        })
    }

    saveChanges() {
        backend.update_menu_item(this.state.id, this.state.name, this.state.category, this.state.price * 1, this.state.description, (data) => {
            if (data.result === true) {
                this.state.handleCloseDialog({ action: 'changes-has-been-made' });
            }
        })
    }


    render() {
        return (
            <Box>
                <DialogTitle id="alert-dialog-title">
                    {"Edit Menu Item"}
                </DialogTitle>
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        The following are current values, type in textfield to change.
                    </DialogContentText>
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Name: </Typography>
                    <TextField size="small" variant="outlined" value={this.state.name && this.state.name}
                        onChange={(e) => this.getFoodName(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Category: </Typography>
                    <TextField size="small" variant="outlined" value={this.state.category && this.state.category}
                        onChange={(e) => this.getCategory(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Price: </Typography>
                    <TextField size="small" variant="outlined" value={this.state.price && this.state.price}
                        onChange={(e) => this.getPrice(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Description: </Typography>
                    <TextField size="small" variant="outlined" value={this.state.description && this.state.description}
                        onChange={(e) => this.getDescription(e)} className="menu-item-detail-text" />
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => this.cancelAndClose()} variant="contained" size="small">Cancel</Button>
                    <Button onClick={() => this.deleteAndClose()} variant="contained" size="small">Delete</Button>
                    <Button onClick={() => this.saveChanges()} variant="contained" size="small">
                        Save Changes
                    </Button>
                </DialogActions>
            </Box>
        );
    }
};