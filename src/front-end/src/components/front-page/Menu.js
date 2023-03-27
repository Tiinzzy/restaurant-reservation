import React from "react";

import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

export default class Menu extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="menu-main-box">
                <Box className="menu-box-menu-logo">
                    <Typography fontFamily="serif" fontWeight="bold" fontSize="2em">Menu</Typography>
                </Box>
                <Box style={{display:'flex', justifyContent: 'space-evenly'}}>
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