import React from "react";

import Divider from '@mui/material/Divider';
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

import './user-styling.scss';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const NUMBER_OF_PEOPLE = [1, 2, 3, 4, 5, 6, '6+'];

export default class MakeReservation extends React.Component {

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
            numberOfPeople: 1,
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
                    <Box className="user-page-reservation-form">
                        <Typography fontSize={14} variant="body1" mb={.5}>Full Name: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getFullName(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Email: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getEmail(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Phone Number: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getPhoneNumber(e)} />
                    </Box>
                </Box>
                <Box style={{ display: 'flex', flexDirection: 'row', alignItems: 'right', justifyContent: 'right', marginRight:20 }}>
                    < Button onClick={() => this.submitReservation()} variant="contained" className="user-page-submit-btn">Submit</Button>
                </Box>
            </Box>
        );
    }
};