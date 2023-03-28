import React from "react";
import { useState } from "react";

import Header from './components/Header';
import Footer from './components/Footer';
import Signup from './components/front-page/Signup';
import Login from './components/front-page/Login';
import Menu from './components/front-page/Menu';
import Reservation from './components/front-page/Reservation';
import Home from './components/front-page/Home';
import UserHomePage from "./components/user-page/UserHomePage";

import BackEndConnection from './components/backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();
const CURRENT_PATH = window.location.pathname;

function checkUserLogin(setIsLogin) {
    backend.authentication_is_login((data) => {
        if (data.is_login) {
            setIsLogin(true);
        }
    })
}

export default function App(props) {
    const [isLogin, setIsLogin] = useState(false);
    const [user, setUser] = useState(null);

    if(user !== null){
        checkUserLogin(setIsLogin);
    }

    function callBack(user) {
        setUser(user);
    }

    return (
        <div>
            {isLogin ?
                <>
                    <Header />
                    {(user !== null) && <UserHomePage user={user} />}
                    <Footer />
                </>
                :
                <>
                    <Header />
                    {(CURRENT_PATH === '/login') && <Login callBack={callBack} />}
                    {(CURRENT_PATH === '/' || CURRENT_PATH === '/home') && <Home />}
                    {(CURRENT_PATH === '/signup') && <Signup />}
                    {(CURRENT_PATH === '/menu') && <Menu />}
                    {(CURRENT_PATH === '/reservation') && <Reservation />}
                    <Footer />

                </>
            }

        </div>
    );
};


