import React from "react";

import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

import { HOME_PAGE_DATA } from "./data";

import "./front-page.scss";

export default class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
        }
    }

    render() {
        return (
            <Box className="home-main-box">
                <img src="https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2014/05/1399503143258.jpeg" height={550} />
                <Box className="home-main-box-about-us">
                    <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={2}>Discover the World of Fine Dining</Typography>
                    {HOME_PAGE_DATA.map((e, i) => (<Typography key={i} fontFamily="serif" fontSize="1.1em">{e}</Typography>))}
                    <Box className="home-main-box-buttons">
                        <a href="#">
                            Checkout Our Menu
                        </a>
                        <a href="#">
                            Make reservation
                        </a>
                    </Box>
                </Box>
            </Box>
        );
    }
};