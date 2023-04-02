import React from "react";

import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';


import './user-styling.scss';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();


export default class ViewMenu extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    componentDidMount() {
        backend.all_menu_items((data) => {
            let that = this;
            let drinks = [];
            let dessert = [];
            let mainCourse = [];
            let entrees = [];
            for (let i in data) {
                if (data[i].category === 'Desert') {
                    dessert.push(data[i]);
                } else if (data[i].category === 'Drink') {
                    drinks.push(data[i]);
                } else if (data[i].category === 'Main Course') {
                    mainCourse.push(data[i]);
                } else if (data[i].category === 'Entrees') {
                    entrees.push(data[i]);
                }
            }
            that.setState({ drinks, dessert, mainCourse, entrees });
        })
    }

    render() {
        return (
            <Box className="delete-account-main-box">
                <Box className="top-header-reservation">
                    <Typography fontSize={20} fontWeight="bold">Our Menu</Typography>
                    <Box display="flex" flexGrow={1} />
                    <Typography fontSize={16} variant="body1">You can brows our latest menu options.</Typography>
                </Box>
                <Divider style={{ margingTop: 10, marginBottom: 25 }} />
            </Box>
        );
    }
};