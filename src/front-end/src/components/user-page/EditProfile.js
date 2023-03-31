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

import './user-styling.scss';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditProfile extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            fullName: '',
            email: '',
            birthDate: null,
            birthday: '',
            currentPassword: '',
            newPassword: '',
            confirmNewPassword: '',
            showPassword: false,

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

    getCurrentPassword(e) {
        this.setState({ currentPassword: e.target.value });
    }

    getNewPassword(e) {
        this.setState({ newPassword: e.target.value });
    }

    getConfirmPassword(e) {
        this.setState({ confirmNewPassword: e.target.value });
    }

    checkBoxClicked(e) {
        this.setState({ showPassword: !this.state.showPassword });
    }

    saveNewChanges() {

    }

    deleteUsersAccount() {

    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Edit Profile</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">To edit profile, simply change your information and click save.</Typography>
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
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getCurrentPassword(e)}
                            type={this.state.showPassword === false ? "password" : "text"} />
                        <Typography fontSize={14} variant="body1" mb={.5}>New Password: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getNewPassword(e)}
                            type={this.state.showPassword === false ? "password" : "text"} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Confirm Password: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getConfirmPassword(e)}
                            type={this.state.showPassword === false ? "password" : "text"} />
                        <FormControlLabel control={<Checkbox onChange={() => this.checkBoxClicked()} />}
                            label="Show Password" />
                    </Box>
                </Box>
                <Box style={{ display: 'flex', flexDirection: 'row', alignItems: 'right', justifyContent: 'right', marginRight: 20 }}>
                    <Button onClick={() => this.deleteUsersAccount()} variant="contained" className="user-page-submit-btn-1">Delete Account</Button>
                    <Button onClick={() => this.saveNewChanges()} variant="contained" className="user-page-submit-btn">Save Changes</Button>
                </Box>
            </Box>
        );
    }
};