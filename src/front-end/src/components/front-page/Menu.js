import React from "react";

import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class Menu extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    componentDidMount() {
        backend.all_menu_items((data) => {
            let that = this;
            let drinks = [];
            let desert = [];
            let mainCourse = [];
            let entrees = [];
            for (let i in data) {
                if (data[i].category === 'Desert') {
                    desert.push(data[i]);
                } else if (data[i].category === 'Drink') {
                    drinks.push(data[i]);
                } else if (data[i].category === 'Main Course') {
                    mainCourse.push(data[i]);
                } else if (data[i].category === 'Entrees') {
                    entrees.push(data[i]);
                }
            }
            that.setState({ drinks, desert, mainCourse, entrees });
        })
    }

    render() {
        return (
            <Box className="menu-main-box">
                <Box className="menu-box-menu-logo">
                    <Typography fontFamily="serif" fontWeight="bold" fontSize="2em">Menu</Typography>
                </Box>
                <Box style={{ display: 'flex', justifyContent: 'space-evenly' }}>
                    <Box className="menu-box-left-side">
                        <Typography fontFamily="serif" fontWeight="bold" fontSize="1.2em">Entrée</Typography>
                        <Typography fontFamily="serif" fontWeight="bold" fontSize="1.2em">Main</Typography>
                    </Box>
                    <Box className="menu-box-right-side">
                        <Typography fontFamily="serif" fontWeight="bold" fontSize="1.2em">Drinks</Typography>
                        <Typography fontFamily="serif" fontWeight="bold" fontSize="1.2em">Dessert</Typography>
                    </Box>
                </Box>
            </Box>
        );
    }
};