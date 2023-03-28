import React from "react";

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

export default class Signup extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            fullName: '',
            email: '',
            password: '',
            confirmPassword: '',
            birthDate: null,
            birthday: '',
            showPassword: false,
        }
    }

    getFullName(e) {
        this.setState({ fullName: e.target.value });
    }

    getEmail(e) {
        this.setState({ email: e.target.value });
    }

    getPassword(e) {
        this.setState({ password: e.target.value });
    }

    getConfirmPassword(e) {
        this.setState({ confirmPassword: e.target.value });
    }

    getBirthDate(e) {
        let date = e.$D + '/' + (e.$M + 1) + '/' + e.$y;
        this.setState({ birthDate: e, birthday: date });
    }

    checkBoxClicked() {
        this.setState({ showPassword: !this.state.showPassword });
    }

    createAccount() {
        backend.add_user((data) => {
            console.log(data);
        })
    }

    render() {
        return (
            <Box className="signup-main-box">
                <Box className="signup-box-form-box">
                    <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                        <Typography className="login-form-texts">
                            Sign Up
                        </Typography>
                    </Box>
                    <TextField label="Full Name" variant="outlined" style={{ marginTop: 50, width: 300 }}
                        onChange={(e) => this.getFullName(e)} />
                    <TextField label="Email" variant="outlined" style={{ marginTop: 25, width: 300 }}
                        onChange={(e) => this.getEmail(e)} />
                    <TextField label="Password" variant="outlined" style={{ marginTop: 25, width: 300 }}
                        onChange={(e) => this.getPassword(e)}
                        type={this.state.showPassword === false ? "password" : "text"} />
                    <TextField label="Confirm Password" variant="outlined" style={{ marginTop: 25, width: 300, marginBottom: 25 }}
                        onChange={(e) => this.getConfirmPassword(e)}
                        type={this.state.showPassword === false ? "password" : "text"} />

                    <LocalizationProvider dateAdapter={AdapterDayjs}>
                        <DatePicker value={this.state.birthDate} onChange={(newValue) => this.getBirthDate(newValue)} format="DD-MM-YYYY" views={["year", "month", "day"]} />
                    </LocalizationProvider>

                    <FormControlLabel control={<Checkbox onChange={() => this.checkBoxClicked()} />}
                        style={{ marginTop: 15, marginBottom: 50 }}
                        label="Show Password" />
                    <Button onClick={() => this.createAccount()} variant="contained" className="signup-box-btn">
                        Create Account
                    </Button>
                    <Typography style={{ color: 'rgb(21, 21, 21)' }} variant="body1">
                        Already have an Account? <span className="signup-box-span">Login</span>
                    </Typography>
                </Box>
            </Box>
        );
    }
};