import React from "react";

import Divider from '@mui/material/Divider';
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

import './user-styling.scss';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const NUMBER_OF_PEOPLE = [1, 2, 3, 4, 5, 6, '6+'];

export default class MakeReservation extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            userEmail: props.userEmail,
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

    componentDidMount() {
        backend.load_user_by_email(this.state.userEmail, (data) => {
            let that = this;
            that.setState({ userId: data.id });
        })
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
        this.setState({ open: true, numberOfPeople: e.target.value });
    }

    getFullName(e) {
        this.setState({ fullName: e.target.value });
    }

    submitReservation() {
        let query = {
            'timestamp': this.state.reservationTime, 'customer_name': this.state.fullName, 'seat_count': this.state.numberOfPeople,
            'for_date': this.state.reservation, 'reservation_type': 'Online', 'status': 'Reserved', 'customer_id': this.state.userId
        };
        if (this.state.reservation.length > 0 && this.state.reservationTime.length > 0 && this.state.fullName.length > 0 && this.state.numberOfPeople > 0) {
            backend.add_reservation(query, (data) => {
                let that = this;
                if (data.result) {
                    that.setState({ madeReservation: true, openSnack: true, reservationTime: '', fullName: '', numberOfPeople: 2, reservation: '', reserveDate: null, time: null });
                } else {
                    that.setState({ madeReservation: true, openSnack: true, reservationError: true });
                }
            })
        } else {
            this.setState({ madeReservation: true, openSnack: true, reservationError: true });
        }

    }

    closeAlert() {
        this.setState({ openSnack: false });
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Make Reservation</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">To make a reservation please fill out the form bellow.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                <Box style={{ display: 'flex', flexDirection: 'row', marginBottom: 40 }}>
                    <Box className="user-page-reservation-form-1">
                        <Typography fontSize={14} variant="body1" mb={.5}>Date: </Typography>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <DatePicker className="localization-provider" value={this.state.reserveDate} onChange={(newValue) => this.getReserveDate(newValue)} format="DD-MM-YYYY" views={["year", "month", "day"]} />
                        </LocalizationProvider>

                        <Typography fontSize={14} variant="body1" mb={.5}>Time: </Typography>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <TimePicker
                                className="localization-provider"
                                value={this.state.time}
                                onChange={(newValue) => {
                                    this.setState({ time: newValue }, () => {
                                        this.setReserveTime(newValue)
                                    })
                                }}
                            />
                        </LocalizationProvider>

                        <Typography fontSize={14} variant="body1" mb={.5}>Number of People: </Typography>
                        <FormControl>
                            <Select
                                className="localization-provider"
                                value={this.state.numberOfPeople}
                                onChange={(e) => this.handleOpenMenu(e)}>
                                {NUMBER_OF_PEOPLE.map((e, i) => (
                                    <MenuItem key={i} value={e}>{e}</MenuItem>))}
                            </Select>
                        </FormControl>
                    </Box>
                    <Box display="flex" flexGrow={1} />
                    <Box className="user-page-reservation-form">
                        <Typography fontSize={14} variant="body1" mb={.5}>Full Name: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getFullName(e)} value={this.state.fullName} />
                        <Box style={{ display: 'flex', flexDirection: 'row', alignItems: 'right', justifyContent: 'right', marginTop: 140 }}>
                            < Button onClick={() => this.submitReservation()} variant="contained" className="user-page-submit-bt-4">Submit</Button>
                        </Box>
                    </Box>
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