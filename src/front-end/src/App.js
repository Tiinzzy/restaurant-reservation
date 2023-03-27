import React from "react";

import Header from './components/Header';
import Footer from './components/Footer';
import Signup from './components/front-page/Signup';
import Login from './components/front-page/Login';
import Menu from './components/front-page/Menu';
import Reservation from './components/front-page/Reservation';
import Home from './components/front-page/Home';

import BackEndConnection from './components/backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();
const CURRENT_PATH = window.location.pathname;

export default function App() {

    console.log(CURRENT_PATH, '<<<')

    return (
        <>
            <Header />
            {CURRENT_PATH === '/login' && <Login />}
            {CURRENT_PATH === '/' && <Home />}

            {/* <Home /> */}
            {/* <Login /> */}
            {/* <Signup /> */}
            {/* <Menu /> */}
            <Footer />
        </>
    );
};


