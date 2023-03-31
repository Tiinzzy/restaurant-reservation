import React from "react";

import Divider from '@mui/material/Divider';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class AddStaff extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            fullName: '',
            email: '',
            birthDate: null,
            birthday: '',
            password: '',
            showPassword: false
        }
    }

    getFullName(e) {
        this.setState({ fullName: e.target.value });
    }

    getEmail(e) {
        this.setState({ email: e.target.value });
    }

    getBirthDate(e) {
        let date = e.$D + '/' + (e.$M + 1) + '/' + e.$y;
        this.setState({ birthDate: e, birthday: date, generalError: false });
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
            console.log(data);
        });
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Add Staff</Typography>
                    <Box display="flex" flexGrow={1} />
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                <Box style={{ display: 'flex', flexDirection: 'row', marginBottom: 40 }}>
                    <Box className="user-page-reservation-form-1">
                        <Typography fontSize={14} variant="body1" mb={.5}>Full Name: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getFullName(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Email: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getEmail(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Birth Date: </Typography>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <DatePicker
                                value={this.state.birthDate} onChange={(newValue) => this.getBirthDate(newValue)} format="DD-MM-YYYY" views={["year", "month", "day"]} />
                        </LocalizationProvider>
                    </Box>
                    <Box display="flex" flexGrow={1} />
                    <Box className="user-page-reservation-form">
                        <Typography fontSize={14} variant="body1" mb={.5}>Current Password: </Typography>
                        <TextField
                            value={this.state.password}
                            variant="outlined" className="localization-provider"
                            type={this.state.showPassword === false ? "password" : "text"} />
                        <Box style={{ display: 'flex', flexDirection: 'row' }}>
                            <FormControlLabel control={<Checkbox onChange={() => this.checkBoxClicked()} />}
                                label="Show Password" />
                            <Box display="flex" flexGrow={1} />
                            <Button variant="contained" onClick={() => this.generateTempPassword()}>Generate Password</Button>
                        </Box>
                        <Box style={{ display: 'flex', flexDirection: 'row', alignItems: 'right', justifyContent: 'right' }}>
                            <Button onClick={() => this.createNewUserAccount()} variant="contained" className="user-page-submit-bt-2">Create User Account</Button>
                        </Box>
                    </Box>
                </Box>
            </Box>
        );
    }
};