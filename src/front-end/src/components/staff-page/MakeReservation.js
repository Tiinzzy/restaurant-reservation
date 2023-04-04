import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import FormControl from '@mui/material/FormControl';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

const NUMBER_OF_PEOPLE = [1, 2, 3, 4, 5, 6, '6+'];
const RESERVATION_TYPE = ['Phone', 'Online', 'In person'];
const STATUS_TYPE = ['Just walked in', 'Here sitting', 'Left', 'Completed', 'Reserved', 'Cancelled']

export default class MakeReservation extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            reserveDate: null,
            reservation: '',
            time: null,
            reservationTime: '',
            customerFullName: '',
            customerId: '',
            status: '',
            tableId: '',
            numberOfPeople: 1,
            latestComment: '',
            duration: '',
            open: false,
            tipPercent: '',
            totalPrice: '',
            waiterId: '',
            statusType: 'Just walked in',
            reservationType: 'Phone'
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
        this.setState({ open: true, numberOfPeople: e.target.value * 1 });
    }

    getTableId(e) {
        this.setState({ tableId: e.target.value * 1 });
    }

    getCustomerFullName(e) {
        this.setState({ customerFullName: e.target.value });
    }

    getCustomerId(e) {
        this.setState({ customerId: e.target.value * 1 });
    }

    getStatus(e) {
        this.setState({ status: e.target.value })
    }

    getLatestComment(e) {
        this.setState({ latestComment: e.target.value });
    }

    getDurationOfStay(e) {
        this.setState({ duration: e.target.value });
    }

    handleOpenReservationType(e) {
        this.setState({ reservationType: e.target.value, open: true });
    }

    handleOpenStatusType(e) {
        this.setState({ statusType: e.target.value, open: true });
    }

    getTipPercent(e) {
        this.setState({ tipPercent: e.target.value * 1 })
    }

    getTotalPrice(e) {
        this.setState({ totalPrice: e.target.value * 1 });
    }

    getWaiterId(e) {
        this.setState({ waiterId: e.target.value * 1 });
    }

    submitReservation() {
        let query = {
            'timestamp': this.state.reservationTime, 'customer_name': this.state.customerFullName, 'customer_id': this.state.customerId, 'seat_count': this.state.numberOfPeople, 'table_id': this.state.tableId, 'for_date': this.state.reservation,
            'for_how_long': this.state.duration, 'status': this.state.status, 'latest_comment': this.state.latestComment, 'waiter_id': this.state.waiterId, 'reservation_type': this.state.reservationType, 'total_price': this.state.totalPrice,
            'tip_percent': this.state.tipPercent
        };

        backend.add_reservation(query, (data) => {
            console.log(data);
        })
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
                <Box style={{ display: 'flex', flexDirection: 'row', marginBottom: 40, overflowY: 'scroll' }}>
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
                        <Typography fontSize={14} variant="body1" mb={.5}>Duration: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getDurationOfStay(e)} />
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
                        <Typography fontSize={14} variant="body1" mb={.5}>Table ID: </Typography>
                        <TextField type="text" inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }} variant="outlined" className="localization-provider"
                            onChange={(e) => this.getTableId(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Waiter ID: </Typography>
                        <TextField type="text" inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }} variant="outlined" className="localization-provider"
                            onChange={(e) => this.getWaiterId(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Total Price: </Typography>
                        <TextField type="text" inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }} variant="outlined" className="localization-provider"
                            onChange={(e) => this.getTotalPrice(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Tip Percent: </Typography>
                        <TextField type="text" inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }} variant="outlined" className="localization-provider"
                            onChange={(e) => this.getTipPercent(e)} />
                    </Box>
                    <Box display="flex" flexGrow={1} />
                    <Box className="user-page-reservation-form">
                        <Typography fontSize={14} variant="body1" mb={.5}>Customer Full Name: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getCustomerFullName(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Customer ID: </Typography>
                        <TextField type="text" inputProps={{ inputMode: 'numeric', pattern: '[0-9]*' }} variant="outlined" className="localization-provider"
                            onChange={(e) => this.getCustomerId(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Status: </Typography>
                        <FormControl>
                            <Select
                                className="localization-provider"
                                value={this.state.statusType}
                                onChange={(e) => this.handleOpenStatusType(e)}>
                                {STATUS_TYPE.map((e, i) => (
                                    <MenuItem key={i} value={e}>{e}</MenuItem>))}
                            </Select>
                        </FormControl>
                        <Typography fontSize={14} variant="body1" mb={.5}>Latest Comment: </Typography>
                        <TextField variant="outlined" className="localization-provider"
                            onChange={(e) => this.getLatestComment(e)} />
                        <Typography fontSize={14} variant="body1" mb={.5}>Reservation Type: </Typography>
                        <FormControl>
                            <Select
                                className="localization-provider"
                                value={this.state.reservationType}
                                onChange={(e) => this.handleOpenReservationType(e)}>
                                {RESERVATION_TYPE.map((e, i) => (
                                    <MenuItem key={i} value={e}>{e}</MenuItem>))}
                            </Select>
                        </FormControl>
                        <Box style={{ display: 'flex', flexDirection: 'row', alignItems: 'right', justifyContent: 'right', marginTop: 40 }}>
                            < Button onClick={() => this.submitReservation()} variant="contained" className="user-page-submit-bt-4">Submit</Button>
                        </Box>
                    </Box>
                </Box>
            </Box>
        );
    }
};
