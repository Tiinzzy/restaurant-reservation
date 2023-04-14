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
                <Box className="home-main-box-about-us">
                    <Carousel>
                        <CarouselItem>
                            <img src="https://www.mtlblog.com/media-library/image.jpg?id=26905670&width=1245&height=700&quality=85&coordinates=0%2C106%2C0%2C106" height={550} width={800}/>
                            <Box className="home-main-box-about-us">
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={2}>Discover the World </Typography>
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={2}>of Fine Dining</Typography>
                                <Typography fontFamily="serif" fontWeight="400" fontSize="1.5em" mb={2}>ALWAYS EXCITING, ALWAYS TASTY, ALWAYS FRESH.</Typography>
                            </Box>
                        </CarouselItem>
                        <CarouselItem>
                            <img src="https://phosphor.utils.elfsightcdn.com/?url=https%3A%2F%2Fscontent-sof1-1.cdninstagram.com%2Fv%2Ft51.2885-15%2F331000746_178562018221392_3118651375992759611_n.jpg%3Fstp%3Ddst-jpg_e35_s750x750_sh0.08%26_nc_ht%3Dscontent-sof1-1.cdninstagram.com%26_nc_cat%3D100%26_nc_ohc%3DnM30fEgpRkIAX8w-9rb%26edm%3DAPU89FABAAAA%26ccb%3D7-5%26oh%3D00_AfAH-xnljQ65KtsUvMgQp-5EkfyIGRfTXiThZoA63Raz-A%26oe%3D643D17C1%26_nc_sid%3D86f79a" height={550} />
                            <Box className="home-main-box-about-us">
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={2}>Our Exclusive Menu</Typography>
                                <Box>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[5]}</Typography>
                                    <Typography fontFamily="serif" fontSize="1.1em">{HOME_PAGE_DATA[6]}</Typography>
                                    <Box className="home-main-box-buttons">
                                        <a href="/menu">
                                            Checkout Our Menu
                                        </a>
                                    </Box>
                                </Box>
                            </Box>
                        </CarouselItem>
                        <CarouselItem>
                            <img src="https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2014/05/1399503143258.jpeg" height={550} />
                            <Box className="home-main-box-about-us">
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={2}>Like What You</Typography>
                                <Typography fontFamily="serif" fontWeight="bold" fontSize="5em" mb={2}>See Already?</Typography>
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