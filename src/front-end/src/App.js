import { Box, Divider } from "@mui/material";
import React from "react";


const axios = require('axios');

var magicClick = () => {
    axios
        .post("/reservation/all", {}, {})
        .then((response) => {
            console.log(response.data);
        })
        .catch((err) => {
            console.log(err)
        });
}

const App = () => {
    return (<>
        <Box p={5}>
            <Divider />
            Hello React, Now I am not using react-script any more
            <Divider />
            <div className="divy" onClick={() => magicClick()}>
                You a "girl who tries to programm"
            </div>
            <Divider />
            <div className='newDiv'>
                This is our key to get out of the home!!!! please!
            </div>
        </Box>
    </>);
};

export default App;


// https://www.educative.io/answers/how-to-create-a-react-application-with-webpack