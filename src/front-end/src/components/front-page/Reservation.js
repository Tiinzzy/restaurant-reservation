import React from "react";

import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControl from '@mui/material/FormControl';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';

const NUMBER_OF_PEOPLE = ['Number of People', 1, 2, 3, 4, 5, 6, '6+'];

export default class Reservation extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            reserveDate: null,
            reservation: '',
            time: null,
            reservationTime: '',
            fullName: '',
            email: '',
            phoneNumber: '',
            numberOfPeople: 'Number of People',
            open: false
        }
    }

    getReserveDate(e) {
        let date = e.$D + '/' + (e.$M + 1) + '/' + e.$y;
        this.setState({ reserveDate: e, reservation: date });
    }

    setReserveTime(e) {
        let resTime = e.$H + '/' + e.$m;
        this.setState({ reservationTime: resTime });
    }

    handleOpenMenu(e) {
        this.setState({ open: true, numberOfPeople: e.target.value });
    }

    getFullName(e) {
        this.setState({ fullName: e.target.value });
    }

    getEmail(e) {
        this.setState({ email: e.target.value });
    }

    getPhoneNumber(e) {
        this.setState({ phoneNumber: e.target.value })
    }

    submitReservation() {

    }

    render() {
        return (
            <Box className="reservation-main-box">
                <Box className="login-box-form-box">
                    <Box style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: 50 }}>
                        <Typography className="login-form-texts">
                            Reservation
                        </Typography>
                    </Box>
                    <LocalizationProvider dateAdapter={AdapterDayjs}>
                        <DatePicker value={this.state.reserveDate} onChange={(newValue) => this.getReserveDate(newValue)} format="DD-MM-YYYY" views={["year", "month", "day"]} />
                    </LocalizationProvider>

                    <LocalizationProvider dateAdapter={AdapterDayjs}>
                        <TimePicker
                            className="time-picker-box"
                            value={this.state.time}
                            onChange={(newValue) => {
                                this.setState({ time: newValue }, () => {
                                    this.setReserveTime(newValue)
                                })
                            }}
                        />
                    </LocalizationProvider>

                    <FormControl>
                        <Select
                            value={this.state.numberOfPeople}
                            onChange={(e) => this.handleOpenMenu(e)}>
                            {NUMBER_OF_PEOPLE.map((e, i) => (
                                <MenuItem key={i} value={e}>{e}</MenuItem>))}
                        </Select>
                    </FormControl>

                    <TextField label="Full Name" variant="outlined" style={{ marginTop: 25, width: 300 }}
                        onChange={(e) => this.getFullName(e)} />
                    <TextField label="Email" variant="outlined" style={{ marginTop: 25, width: 300 }}
                        onChange={(e) => this.getEmail(e)} />
                    <TextField label="Phone Number" variant="outlined" style={{ marginTop: 25, width: 300, marginBottom: 25 }}
                        onChange={(e) => this.getPhoneNumber(e)} />
                    < Button onClick={() => this.submitReservation()} variant="contained" className="login-box-btn">Submit</Button>
                    <Typography style={{ color: 'rgb(21, 21, 21)' }} variant="body1">
                        Already have an Account? <span className="login-box-span">Login to Make Reservation.</span>
                    </Typography>
                </Box>
            </Box>
        );
    }
};