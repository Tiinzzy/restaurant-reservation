import React from "react";

import Divider from '@mui/material/Divider';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
import Dialog from '@mui/material/Dialog';

import EditMenuDialog from "./EditMenuDialog";

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditMenu extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            foodName: '',
            category: '',
            price: '',
            description: '',
            addItem: false,
            openSnack: false,
            menuError: false,
            openDialog: false
        }
    }

    componentDidMount() {
        backend.all_menu_items((data) => {
            let that = this;
            that.setState({ menuItems: data })
        })
    }

    getFoodName(e) {
        this.setState({ foodName: e.target.value });
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

    submitAddingMenuItem() {
        backend.add_menu_item(this.state.foodName, this.state.category, this.state.price, this.state.description, (data) => {
            let that = this;
            if (data.result === true) {
                that.setState({ addItem: true, openSnack: true }, () => {
                    that.componentDidMount();
                });
            } else {
                that.setState({ menuError: true });
            }
        })
    }

    closeAlert() {
        this.setState({ openSnack: false });
    }

    handleOpenDialog(e) {
        this.setState({ openDialog: true, menuItemId: e.target.innerHTML });
    }

    handleCloseDialog() {
        this.setState({ openDialog: false });
    }

    render() {
        return (
            <>
                <Box className="delete-account-main-box">
                    <Box className="top-header-reservation">
                        <Typography fontSize={20} fontWeight="bold">Edit Menu</Typography>
                        <Box display="flex" flexGrow={1} />
                    </Box>
                    <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                    <Box style={{ display: 'flex', flexDirection: 'row', marginBottom: 40 }}>
                        <Box className="user-page-reservation-form-1">
                            <Typography fontSize={14} variant="body1" mb={.5}>Name: </Typography>
                            <TextField variant="outlined" className="localization-provider"
                                onChange={(e) => this.getFoodName(e)} />
                            <Typography fontSize={14} variant="body1" mb={.5}>Category: </Typography>
                            <TextField variant="outlined" className="localization-provider"
                                onChange={(e) => this.getCategory(e)} />
                            <Typography fontSize={14} variant="body1" mb={.5}>Price: </Typography>
                            <TextField variant="outlined" className="localization-provider"
                                onChange={(e) => this.getPrice(e)} />
                            <Typography fontSize={14} variant="body1" mb={.5}>Description: </Typography>
                            <TextField variant="outlined" className="localization-provider"
                                onChange={(e) => this.getDescription(e)} />
                            <Button onClick={() => this.submitAddingMenuItem()} variant="contained">Submit</Button>

                        </Box>
                        <Box display="flex" flexGrow={1} />
                        <Box className="user-page-reservation-form-3">
                            <Box className="table-data-display-box">
                                <table width="100%">
                                    <tbody>
                                        <tr>
                                            <th>id</th>
                                            <th>Name</th>
                                            <th>Category</th>
                                            <th>Price</th>
                                            <th>Description</th>
                                        </tr>
                                        {this.state.menuItems && this.state.menuItems.map((e, i) => (
                                            <tr key={i}>
                                                <td id="td-menu-item-id" onClick={(e) => this.handleOpenDialog(e)}>
                                                    {e.id}
                                                </td>
                                                <td>
                                                    {e.name}
                                                </td>
                                                <td>
                                                    {e.category}
                                                </td>
                                                <td>
                                                    ${e.price}
                                                </td>
                                                <td>
                                                    {e.description}
                                                </td>
                                            </tr>))}
                                    </tbody>
                                </table>
                            </Box>
                        </Box>
                    </Box>
                </Box>
                {this.state.addItem === true &&
                    <Snackbar open={this.state.openSnack} onClose={() => this.closeAlert()} autoHideDuration={5000} anchorOrigin={{ vertical: "top", horizontal: "center" }}>
                        <Alert severity={this.state.menuError === true ? "error" : "success"}>
                            {this.state.menuError === true ? "Sorry, Something went wrong!" : "Menu Item Added Successfully!"}
                        </Alert>
                    </Snackbar>}

                <Dialog open={this.state.openDialog} onClose={() => this.handleCloseDialog()}>
                    <EditMenuDialog menuItemId={this.state.menuItemId} />
                </Dialog>
            </>
        );
    }
};