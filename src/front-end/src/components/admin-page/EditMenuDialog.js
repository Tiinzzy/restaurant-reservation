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
        }
    }

    componentDidMount() {
        backend.load_menu_item(this.state.menuItemId, (data) => {
            let that = this;
            this.setState({ data });
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
                    <TextField size="small" variant="outlined" value={this.state.data && this.state.data.name}
                        onChange={(e) => this.getFoodName(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Category: </Typography>
                    <TextField size="small" variant="outlined" value={this.state.data && this.state.data.category}
                        onChange={(e) => this.getCategory(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Price: </Typography>
                    <TextField size="small" variant="outlined" value={this.state.data && this.state.data.price}
                        onChange={(e) => this.getPrice(e)} className="menu-item-detail-text" />
                    <Typography fontWeight='bold' fontSize={14} variant="body1" mb={.5} mt={1.5}>Description: </Typography>
                    <TextField size="small" variant="outlined" value={this.state.data && this.state.data.description}
                        onChange={(e) => this.getDescription(e)} className="menu-item-detail-text" />
                </DialogContent>
                <DialogActions>
                    <Button >Cancel</Button>
                    <Button autoFocus>
                        Save Changes
                    </Button>
                </DialogActions>

            </Box>
        );
    }
};