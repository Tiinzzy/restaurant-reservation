import React from "react";

import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import FormControl from '@mui/material/FormControl';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';
import { InputLabel } from "@mui/material";

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const NUMBER_OF_PEOPLE = [1, 2, 3, 4, 5, 6, '6+'];

export default class Reservation extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            reserveDate: null,
            reservation: '',
            time: null,
            reservationTime: '',
            fullName: '',
            numberOfPeople: 2,
            open: false,
            madeReservation: false,
            openSnack: false,
            reservationError: false
        }
    }

    getReserveDate(e) {
        let date = e.$y + '/' + (e.$M + 1) + '/' + e.$D;
        this.setState({ reserveDate: e, reservation: date });
    }

    setReserveTime(e) {
        let resTime = e.$H + ':' + e.$m;
        this.setState({ reservationTime: resTime });
    }

    handleOpenMenu(e) {
        this.setState({ open: true, numberOfPeople: e.target.value * 1 });
    }

    getFullName(e) {
        this.setState({ fullName: e.target.value })
    }

    submitReservation() {
        let query = {
            'timestamp': this.state.reservationTime, 'customer_name': this.state.fullName, 'seat_count': this.state.numberOfPeople,
            'for_date': this.state.reservation, 'reservation_type': 'Online', 'status': 'Reserved'
        };
        backend.add_reservation(query, (data) => {
            let that = this;
            if (data.result) {
                that.setState({ madeReservation: true, openSnack: true, reservationTime: '', fullName: '', numberOfPeople: 2, reservation: '', reserveDate: null, time: null });
            } else {
                that.setState({ madeReservation: true, openSnack: true, reservationError: true });
            }
        })
    }

    closeAlert() {
        this.setState({ openSnack: false });
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


                    <FormControl>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <DatePicker value={this.state.reserveDate} label="Date"
                                onChange={(newValue) => this.getReserveDate(newValue)}
                                format="DD-MM-YYYY" views={["year", "month", "day"]} />
                        </LocalizationProvider>
                    </FormControl>

                    <FormControl>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <TimePicker
                                label="Time"
                                className="time-picker-box"
                                value={this.state.time}
                                onChange={(e) =>
                                    this.setState({ time: e }, () => {
                                        this.setReserveTime(e)
                                    })
                                }
                            />
                        </LocalizationProvider>
                    </FormControl>

                    <FormControl>
                        <InputLabel id="no-people-labell">Number of People</InputLabel>
                        <Select
                            label="Number of People"
                            labelId="no-people-label"
                            value={this.state.numberOfPeople}
                            onChange={(e) => this.handleOpenMenu(e)}>
                            {NUMBER_OF_PEOPLE.map((e, i) => (
                                <MenuItem key={i} value={e}>{e}</MenuItem>))}
                        </Select>
                    </FormControl>

                    <TextField value={this.state.fullName} label="Full Name" variant="outlined" style={{ marginTop: 25, width: 300, marginBottom: 25 }}
                        onChange={(e) => this.getFullName(e)} />
                    < Button onClick={() => this.submitReservation()} variant="contained" className="login-box-btn">Submit</Button>
                    <Typography style={{ color: 'rgb(21, 21, 21)' }} variant="body1">
                        Already have an Account? <span className="login-box-span">Login to Make Reservation.</span>
                    </Typography>
                </Box>
                {this.state.madeReservation === true &&
                    <Snackbar open={this.state.openSnack} onClose={() => this.closeAlert()} autoHideDuration={5000} anchorOrigin={{ vertical: "top", horizontal: "center" }}>
                        <Alert severity={this.state.reservationError ? "error" : "success"}>
                            {this.state.reservationError ? "Sorry, Something went wrong!" : "Reservation Made Successfully!"}
                        </Alert>
                    </Snackbar>}
            </Box>
        );
    }
};