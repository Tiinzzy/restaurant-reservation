import React from "react";

import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class Login extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '',
            showPassword: false,
            callBack: props.callBack
        }
    }

    getEmail(e) {
        this.setState({ email: e.target.value });
    }

    getPassword(e) {
        this.setState({ password: e.target.value });
    }

    checkBoxClicked() {
        this.setState({ showPassword: !this.state.showPassword });
    }

    loginTheUser() {

        backend.authentication_login(this.state.email, this.state.password, (data) => {
            if (data.success === true) {
                this.state.callBack({ 'user': this.state.email, 'login': data.success });
            } else {
                console.log('something went wrong');
            }
        });
    }

    render() {
        return (
            <Box className="login-main-box">
                <Box className="login-box-form-box">
                    <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                        <Typography className="login-form-texts">
                            Login
                        </Typography>
                    </Box>
                    <TextField label="Email" variant="outlined" style={{ marginTop: 50, width: 300 }}
                        onChange={(e) => this.getEmail(e)} />
                    <TextField label="Password" variant="outlined" style={{ marginTop: 25, width: 300 }}
                        onChange={(e) => this.getPassword(e)}
                        type={this.state.showPassword === false ? "password" : "text"} />
                    <FormControlLabel control={<Checkbox onChange={() => this.checkBoxClicked()} />}
                        style={{ marginTop: 15, marginBottom: 50 }}
                        label="Show Password" />
                    <Button onClick={() => this.loginTheUser()} variant="contained" className="login-box-btn">Login</Button>
                    <Typography style={{ color: 'rgb(21, 21, 21)' }} variant="body1">
                        Don't have an Account? <span className="login-box-span">Sign Up</span>
                    </Typography>
                </Box>
            </Box>
        );
    }
};