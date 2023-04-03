import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class MakeOrder extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    componentDidMount() {
        backend.all_menu_items((data) => {
            let that = this;
            that.setState({ data });
        })
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Make an Order</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">To make an order, just click on the + to add.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
                <Box className="user-page-reservation-form-4">
                    {this.state.data && this.state.data.map((e, i) => (
                        <Box key={i}>
                            <Box style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-betwee', alignItems: 'center' }}>
                            <Typography fontFamily="serif" fontWeight="bold" fontSize="1em" color="rgb(37, 37, 37)">{e.name}</Typography>
                                <Box display="flex" flexGrow={1} />
                                <span>
                                <span fontFamily="serif" color="rgb(37, 37, 37)">${e.price}</span>
                                    <IconButton aria-label="add">
                                        <AddCircleOutlineIcon />
                                    </IconButton>
                                </span>
                            </Box>
                            <br />
                            <Typography fontFamily="serif" fontSize=".8em" color="rgb(94, 94, 94)">{e.description}</Typography>
                            <Divider />
                        </Box>))}
                </Box>
            </Box>
        );
    }
};