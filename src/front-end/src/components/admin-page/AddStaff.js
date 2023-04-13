import React from "react";

import Divider from '@mui/material/Divider';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
import OutlinedInput from '@mui/material/OutlinedInput';
import MenuItem from '@mui/material/MenuItem';
import ListItemText from '@mui/material/ListItemText';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const STAFF_ROLE = ['Admin', 'Customer', 'Waiter', 'Cashier'];

const ITEM_HEIGHT = 48;

const ITEM_PADDING_TOP = 8;

const MenuProps = {
    PaperProps: {
        style: {
            maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
            width: 250,
        },
    },
};

export default class AddStaff extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            fullName: '',
            email: '',
            birthDate: null,
            birthday: '',
            password: '',
            showPassword: false,
            open: false,
            userRole: [],
            buttonOff: true,
            addUser: false,
            openSnack: false,
            userError: false
        }
    }

    componentDidMount(email) {
        if (email) {
            backend.load_user_by_email(email, (data) => {
                let userId = data.id;
                this.setState({ userId });
                let query = { 'user_id': userId, 'role_name': this.state.userRole };

                backend.add_user_role(query, (data) => {
                    let that = this;
                    if (data.result[0] === true) {
                        that.setState({ fullName: '', email: '', birthDate: null, birthday: '', password: '', birthDate: null, userRole: [] });
                    }
                })
            })
        }
    }

    getFullName(e) {
        this.setState({ fullName: e.target.value });
    }

    getEmail(e) {
        this.setState({ email: e.target.value });
    }

    getBirthDate(e) {
        let date = e.$y + '/' + (e.$M + 1) + '/' + e.$D;
        this.setState({ birthDate: e, birthday: date, generalError: false });
    }

    handleMenuChange(e) {
        let value = e.target.value;
        let userRole = (typeof value === 'string' ? value.split(',') : value);
        this.setState({ userRole, buttonOff: false });
    }

    checkBoxClicked(e) {
        this.setState({ showPassword: !this.state.showPassword });
    }

    generateTempPassword() {
        let random = (Math.random() + 1).toString(36).substring(6);
        let temporaryPassword = this.state.fullName.replace(' ', '') + '-' + random;
        this.setState({ password: temporaryPassword });
    }

    createNewUserAccount() {
        backend.add_user(this.state.fullName, this.state.email, this.state.password, this.state.birthday, (data) => {
            let that = this;
            if (data.result === true) {
                that.setState({ openSnack: true, addUser: true }, () => {
                    this.componentDidMount(this.state.email);
                })
            } else {
                that.setState({ userError: true, openSnack: true, addUser: true });
            }
        });
    }

    closeAlert() {
        this.setState({ openSnack: false });
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Add Staff</Typography>
                    <Box display="flex" flexGrow={1} />
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                <Box style={{ display: 'flex', flexDirection: 'row', marginBottom: 40, justifyContent: 'space-between' }}>
                    <Box className="user-page-reservation-form-1">
                        <Typography fontSize={14} variant="body1" mb={.5}>Full Name: </Typography>
                        <TextField value={this.state.fullName} variant="outlined" className="localization-provider"
                            onChange={(e) => this.getFullName(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Email: </Typography>
                        <TextField value={this.state.email} variant="outlined" className="localization-provider"
                            onChange={(e) => this.getEmail(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Birth Date: </Typography>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <DatePicker
                                value={this.state.birthDate} onChange={(newValue) => this.getBirthDate(newValue)} format="DD-MM-YYYY" views={["year", "month", "day"]} />
                        </LocalizationProvider>
                        <Typography id="user-role-id" fontSize={14} variant="body1" mb={.5} mt={2}>User Role: </Typography>
                        <FormControl>
                            <Select
                                labelId="user-role-id"
                                multiple
                                className="localization-provider"
                                value={this.state.userRole}
                                renderValue={(selected) => selected.join(', ')}
                                onChange={(e) => this.handleMenuChange(e)}
                            >
                                {STAFF_ROLE.map((e, i) => (
                                    <MenuItem key={i} value={e}>
                                        <Checkbox
                                            checked={this.state.userRole.includes(e)} />
                                        <ListItemText primary={e} />
                                    </MenuItem>))}
                            </Select>
                        </FormControl>
                    </Box>
                    <Box className="user-page-reservation-form">
                        <Typography fontSize={14} variant="body1" mb={.5}>Create Password: </Typography>
                        <TextField
                            value={this.state.password}
                            variant="outlined" className="localization-provider"
                            type={this.state.showPassword === false ? "password" : "text"} />
                        <Box style={{ display: 'flex', flexDirection: 'row' }}>
                            <FormControlLabel control={<Checkbox onChange={() => this.checkBoxClicked()} />}
                                label="Show Password" />
                            <Box display="flex" flexGrow={1} />
                            <Button variant="contained" onClick={() => this.generateTempPassword()} disabled={this.state.buttonOff}>
                                Generate Password</Button>
                        </Box>
                        <Box style={{ display: 'flex', flexDirection: 'row', alignItems: 'right', justifyContent: 'right' }}>
                            <Button onClick={() => this.createNewUserAccount()} variant="contained" className="user-page-submit-bt-2">Create User Account</Button>
                        </Box>
                    </Box>
                </Box>
                {this.state.addUser === true &&
                    <Snackbar open={this.state.openSnack} onClose={() => this.closeAlert()} autoHideDuration={5000} anchorOrigin={{ vertical: "top", horizontal: "center" }}>
                        <Alert severity={this.state.userError === true ? "error" : "success"}>
                            {this.state.userError === true ? "Sorry, Something went wrong!" : "Account Created Successfully!"}
                        </Alert>
                    </Snackbar>}
            </Box>
        );
    }
};