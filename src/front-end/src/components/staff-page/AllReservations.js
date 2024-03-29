import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import Dialog from "@mui/material/Dialog";
import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';

import EditReservationDialog from "./EditReservationDialog";

import BackEndConnection from '../backend-connection/BackEndConnection';
import { Button } from "@mui/material";

const backend = BackEndConnection.INSTANCE();

export default class AllReservations extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            openDialog: false,
            changesMade: false,
            openSnack: false
        }
        this.handleCloseDialog = this.handleCloseDialog.bind(this);
    }

    componentDidMount() {
        backend.all_reservations((data) => {
            let that = this;
            that.setState({ data });
        })
    }

    openReservationsDialog(e) {
        this.setState({ openDialog: true, reservationId: e });
    }

    handleCloseDialog(data) {
        if (data && data.action === 'changes-made-successfully') {
            this.setState({ openDialog: false, changesMade: true, openSnack: true }, () => {
                this.componentDidMount();
            });
        } else {
            this.setState({ openDialog: false }, () => {
                this.componentDidMount();
            });
        }
    }

    closeAlert() {
        this.setState({ openSnack: false });
    }

    render() {
        return (
            <Box className="satff-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">All Reservation</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">Click on any reservation to view and edit.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                <Box className="staff-all-reservations-main-box">
                    {this.state.data && this.state.data.map((e, i) => (
                        <Box key={i} className="all-reservations-single-box">
                            <Box className="all-reservations-data-box">
                                <Box style={{ display: 'flex', flexDirection: 'row' }}>
                                    <Typography fontSize={18} fontWeight="700">Reservation ID:</Typography>
                                    <Typography fontSize={18} fontWeight="500" ml={1.5}>{e.id}</Typography>
                                </Box>
                                <Box style={{ display: 'flex', flexDirection: 'row' }}>
                                    <Typography fontSize={18} fontWeight="700">Customer Name:</Typography>
                                    <Typography fontSize={18} fontWeight="500" ml={1.5}>{e.customer_name}</Typography>
                                </Box>
                                <Box style={{ display: 'flex', flexDirection: 'row' }}>
                                    <Typography fontSize={18} fontWeight="700">Timestamp:</Typography>
                                    <Typography fontSize={18} fontWeight="500" ml={1.5}>{e.timestamp}</Typography>
                                </Box>
                                <Box style={{ display: 'flex', flexDirection: 'row' }}>
                                    <Typography fontSize={18} fontWeight="700">Date:</Typography>
                                    <Typography fontSize={18} fontWeight="500" ml={1.5}>{e.for_date}</Typography>
                                </Box>
                            </Box>
                            <Box className="all-reservations-edit-one-box">
                                <Button variant="contained" onClick={() => this.openReservationsDialog(e.id)} >Edit</Button>
                            </Box>
                        </Box>
                    ))}
                </Box>
                <Dialog open={this.state.openDialog} onClose={() => this.handleCloseDialog()} fullWidth={true}>
                    <EditReservationDialog closeDialog={this.handleCloseDialog} reservationId={this.state.reservationId} />
                </Dialog>
                {this.state.changesMade === true &&
                    <Snackbar open={this.state.openSnack} onClose={() => this.closeAlert()} autoHideDuration={5000} anchorOrigin={{ vertical: "top", horizontal: "center" }}>
                        <Alert severity="success">
                            Changes Made Successfully!
                        </Alert>
                    </Snackbar>}
            </Box>
        );
    }
};