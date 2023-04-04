import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class AllReservations extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    componentDidMount() {
        backend.all_reservations((data) => {
            let that = this;
            that.setState({ data });
        })
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">All Reservation</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">Click on any reservation to view and edit.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                <Box style={{ display: 'flex', flexDirection: 'row', marginBottom: 40, overflowY: 'scroll' }}>
                    {this.state.data && this.state.data.map((e, i) => (
                        <Box key={i}>
                            id: {e.id}
                            <br/>
                            customer name: {e.customer_name}
                            <br/>
                            timestamp: {e.timestamp}
                            <br/>
                            customer id: {e.customer_id}
                            <br/>
                            seat count: {e.seat_count}
                            <br/>
                            table id: {e.table_id}
                            <br/>
                            for date: {e.for_date}
                            <br/>
                            for how long: {e.for_how_long}
                            <br/>
                            status: {e.status}
                            <br/>
                            comment: {e.comment}
                            <br/>
                            waiter id:{e.waiter_id}
                            <br/>
                            reservation type: {e.reservation_type}
                            <br/>
                            total price: {e.total_price}
                            <br/>
                            tip percent: {e.tip_percent}
                        </Box>
                    ))}
                </Box>
            </Box>
        );
    }
};