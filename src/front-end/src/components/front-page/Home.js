import React from "react";

import Box from '@mui/material/Box';
import Typography from "@mui/material/Typography";

import Carousel, { CarouselItem } from "./Carousel";
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
                <Box>
                    <Carousel>
                        <CarouselItem>
                            <img src="https://tinyurl.com/3ue98sn4" height={550} width={800}/>
                            <Box className="home-main-box-about-us-1">
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={2}>Discover the World </Typography>
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={5}>of Fine Dining</Typography>
                                <Typography fontFamily="serif" fontWeight="400" fontSize="1.5em" mb={2}>ALWAYS EXCITING, ALWAYS TASTY, ALWAYS FRESH.</Typography>
                            </Box>
                        </CarouselItem>
                        <CarouselItem>
                            <img src="https://tinyurl.com/mpney5p6" height={550} widht={600}/>
                            <Box className="home-main-box-about-us-2">
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={5}>Our Exclusive Menu</Typography>
                                <Box>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[5]}</Typography>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[6]}</Typography>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[7]}</Typography>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[8]}</Typography>
                                    <Box className="home-main-box-buttons">
                                        <a href="/menu">
                                            Checkout Our Menu
                                        </a>
                                    </Box>
                                </Box>
                            </Box>
                        </CarouselItem>
                        <CarouselItem>
                            <img src="https://tinyurl.com/vkkp2wfj" height={550} />
                            <Box className="home-main-box-about-us-3">
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={2}>Like What You</Typography>
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={5}>See Already?</Typography>
                                <Box>
                                <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[0]}</Typography>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[1]}</Typography>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[2]}</Typography>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[3]}</Typography>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[4]}</Typography>
                                    <Box className="home-main-box-buttons">
                                        <a href="/reservation">
                                            Make reservation
                                        </a>
                                    </Box>
                                </Box>
                            </Box>
                        </CarouselItem>
                    </Carousel>
                </Box>
            </Box>
        );
    }
};