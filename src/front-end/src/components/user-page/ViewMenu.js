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

                <Box style={{ display: 'flex', justifyContent: 'space-evenly' }}>
                    <Box className="menu-box-left-side-user">
                        <Typography fontFamily="serif" fontWeight="bold" fontSize="1.3em" mb={1.6} mt={1.6}>Entrée</Typography>
                        {this.state.entrees && this.state.entrees.map((e, i) => (
                            <Box key={i} className="each-menu-item-box">
                                <span style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-betwee' }}>
                                    <Typography fontFamily="serif" fontWeight="bold" fontSize="1em" color="rgb(37, 37, 37)">{e.name}</Typography>
                                    <Box display="flex" flexGrow={1} />
                                    <Typography fontFamily="serif" fontWeight="600" fontSize=".9em" color="rgb(37, 37, 37)">${e.price}</Typography>
                                </span>
                                <Typography fontFamily="serif" fontSize=".8em" color="rgb(94, 94, 94)">{e.description}</Typography>
                            </Box>
                        ))}
                        <Typography fontFamily="serif" fontWeight="bold" fontSize="1.3em" mb={1.6} mt={1.6}>Main Course</Typography>
                        {this.state.mainCourse && this.state.mainCourse.map((e, i) => (
                            <Box key={i} className="each-menu-item-box">
                                <span style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-betwee' }}>
                                    <Typography fontFamily="serif" fontWeight="bold" fontSize="1em" color="rgb(37, 37, 37)">{e.name}</Typography>
                                    <Box display="flex" flexGrow={1} />
                                    <Typography fontFamily="serif" fontWeight="600" fontSize=".9em" color="rgb(37, 37, 37)">${e.price}</Typography>
                                </span>
                                <Typography fontFamily="serif" fontSize=".8em" color="rgb(94, 94, 94)">{e.description}</Typography>
                            </Box>
                        ))}
                    </Box>
                    <Box className="menu-box-right-side-user">
                        <Typography fontFamily="serif" fontWeight="bold" fontSize="1.3em" mb={1.6} mt={1.6}>Drinks</Typography>
                        {this.state.drinks && this.state.drinks.map((e, i) => (
                            <Box key={i} className="each-menu-item-box">
                                <span style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-betwee' }}>
                                    <Typography fontFamily="serif" fontWeight="bold" fontSize="1em" color="rgb(37, 37, 37)">{e.name}</Typography>
                                    <Box display="flex" flexGrow={1} />
                                    <Typography fontFamily="serif" fontWeight="600" fontSize=".9em" color="rgb(37, 37, 37)">${e.price}</Typography>
                                </span>
                                <Typography fontFamily="serif" fontSize=".8em" color="rgb(94, 94, 94)">{e.description}</Typography>
                            </Box>
                        ))}
                        <Typography fontFamily="serif" fontWeight="bold" fontSize="1.3em" mb={1.6} mt={1.6}>Dessert</Typography>
                        {this.state.dessert && this.state.dessert.map((e, i) => (
                            <Box key={i} className="each-menu-item-box">
                                <span style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-betwee' }}>
                                    <Typography fontFamily="serif" fontWeight="bold" fontSize="1em" color="rgb(37, 37, 37)">{e.name}</Typography>
                                    <Box display="flex" flexGrow={1} />
                                    <Typography fontFamily="serif" fontWeight="600" fontSize=".9em" color="rgb(37, 37, 37)">${e.price}</Typography>
                                </span>
                                <Typography fontFamily="serif" fontSize=".8em" color="rgb(94, 94, 94)">{e.description}</Typography>
                            </Box>
                        ))}
                    </Box>
                </Box>
            </Box>
        );
    }
};