import React from "react";

import Box from '@mui/material/Box';

import BackEndConnection from '../backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();

export default class EditMenuDialog extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            menuItemId: props.menuItemId
        }
    }

    componentDidMount() {
        backend.load_menu_item(this.state.menuItemId, (data) => {
            console.log(data);
        })
    }

    render() {
        return (
            <Box>
                This is a test
            </Box>
        );
    }
};