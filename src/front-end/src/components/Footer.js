import React from "react";

import Box from '@mui/material/Box';

export default class Footer extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="footer-box">
                Designed by Tina Vatanabadi, Copyright © 2023. All Rights Reserved
            </Box>
        );
    }
};