import React, { useState } from "react";

import Header from './components/Header';
import Footer from './components/Footer';
import Signup from './components/front-page/Signup';
import Login from './components/front-page/Login';
import Menu from './components/front-page/Menu';
import Reservation from './components/front-page/Reservation';
import Home from './components/front-page/Home';
import UserHomePage from "./components/user-page/UserHomePage";
import AdminHomePage from "./components/admin-page/AdminHomePage";
import HeaderLogin from "./components/HeaderLogin";

import BackEndConnection from './components/backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();
const CURRENT_PATH = window.location.pathname;


function checkUserLogin(setIsLogin, setUser, user) {
    backend.authentication_is_login((data) => {
        if (data.is_login !== false) {
            setIsLogin(true);
        }
    })
}

export default function App() {
    const [isLogin, setIsLogin] = useState(false);
    const [user, setUser] = useState(null);

    checkUserLogin(setIsLogin, setUser);

    function callBack(data) {
        if (data.login) {
            setUser(data.user)
        };
    }

    return (
        <div>
            {/* {isLogin ?
                <> */}
            <HeaderLogin user={user} />
            {/* {user !== null &&  */}
            <AdminHomePage user={user} />
                    {/*  } */}
            <Footer />
            {/* </>
                :
                <>
                    <Header />
                    {(CURRENT_PATH === '/login' && user === null) && <Login callBack={callBack} />}
                    {(CURRENT_PATH === '/' || CURRENT_PATH === '/home') && <Home />}
                    {CURRENT_PATH === '/signup' && <Signup />}
                    {CURRENT_PATH === '/menu' && <Menu />}
                    {CURRENT_PATH === '/reservation' && <Reservation />}
                    <Footer />

                </>
            } */}

        </div>
    );
};