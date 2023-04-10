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
            passwordNotMatch: false,
            generalError: false
        }
    }

    componentDidMount(email) {
        backend.load_user_by_email(email, (data) => {
            let userId = data.id;
            let roleName = 'Customer';
            this.setState({ userId })
            let query = { 'user_id': userId, 'role_name': roleName };
            backend.add_user_role(query, (data) => {
                if (data.result[0] === true) {
                    backend.authentication_login(this.state.email, this.state.password, this.state.userId, (data) => {
                        if (data.success === true) {
                            window.location = '/';
                        }
                    });
                }
            })
        })
    }

    getFullName(e) {
        this.setState({ fullName: e.target.value, generalError: false });
    }

    getEmail(e) {
        this.setState({ email: e.target.value, generalError: false });
    }

    getPassword(e) {
        this.setState({ password: e.target.value, passwordNotMatch: false, generalError: false });
    }

    getConfirmPassword(e) {
        this.setState({ confirmPassword: e.target.value, passwordNotMatch: false, generalError: false });
    }

    getBirthDate(e) {
        let date = e.$y + '/' + (e.$M + 1) + '/' + e.$D;
        this.setState({ birthDate: e, birthday: date, generalError: false });
    }

    checkBoxClicked() {
        this.setState({ showPassword: !this.state.showPassword });
    }

    createAccount() {
        if (this.state.password !== this.state.confirmPassword) {
            this.setState({ passwordNotMatch: true });
        } else if (this.state.fullName.length === 0 || this.state.password.length === 0 || this.state.confirmPassword.length === 0 || this.state.email.length === 0 || this.state.birthday === 0) {
            this.setState({ generalError: true })
        } else {
            backend.add_user(this.state.fullName, this.state.email, this.state.confirmPassword, this.state.birthday, (data) => {
                if (data.result === true) {
                    console.log('yes')
                    this.componentDidMount(this.state.email);
                };
            });
        }
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
                        error={this.state.generalError === true}
                        onChange={(e) => this.getFullName(e)} />
                    <TextField label="Email" variant="outlined" style={{ marginTop: 25, width: 300 }}
                        error={this.state.generalError === true}
                        onChange={(e) => this.getEmail(e)} />
                    <TextField label="Password" variant="outlined" style={{ marginTop: 25, width: 300 }}
                        onChange={(e) => this.getPassword(e)}
                        error={this.state.passwordNotMatch === true || this.state.generalError == true}
                        helperText={this.state.passwordNotMatch && "Passwords Not Matching"}
                        type={this.state.showPassword === false ? "password" : "text"} />
                    <TextField label="Confirm Password" variant="outlined" style={{ marginTop: 25, width: 300, marginBottom: 25 }}
                        onChange={(e) => this.getConfirmPassword(e)}
                        error={this.state.passwordNotMatch === true || this.state.generalError == true}
                        helperText={this.state.passwordNotMatch && "Passwords Not Matching"}
                        type={this.state.showPassword === false ? "password" : "text"} />

                    <LocalizationProvider dateAdapter={AdapterDayjs}>
                        <DatePicker error={this.state.generalError === true}
                            value={this.state.birthDate} onChange={(newValue) => this.getBirthDate(newValue)} format="DD-MM-YYYY" views={["year", "month", "day"]} />
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