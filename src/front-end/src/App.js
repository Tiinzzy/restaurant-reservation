import { Box, Divider } from "@mui/material";
import React from "react";


var f = () => alert(1232345235);

const App = () => {
    return (<>
        <Box p={5}>
            <Divider />
            Hello React, Now I am not using react-script any more
            <Divider />
            <div className="divy" onClick={() => f()}>
                YOU A CLICKER
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