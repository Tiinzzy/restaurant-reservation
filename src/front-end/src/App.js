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
import WaiterHomePage from "./components/staff-page/WaiterHomePage";

import BackEndConnection from './components/backend-connection/BackEndConnection';

const backend = BackEndConnection.INSTANCE();
const CURRENT_PATH = window.location.pathname;
const usrParams = new URLSearchParams(window.location.search);


function checkUserLogin(setIsLogin, setUser, setPageReady) {
    let user = usrParams.get('user');
    window.history.pushState({}, "", "/");
    backend.authentication_is_login(user, (data) => {
        if (data.is_login) {
            setIsLogin(true);
            setUser(user);
        } else {
            setIsLogin(false);
            setUser(null);
        }
        setPageReady(true);
    })
}

export default function App() {
    const [isLogin, setIsLogin] = useState(false);
    const [user, setUser] = useState(null);
    const [pageReady, setPageReady] = useState(false);

    checkUserLogin(setIsLogin, setUser, setPageReady);

    return (
        <div>
            {pageReady && (isLogin ?
                <>
                    <HeaderLogin user={user} />
                    {user !== null && <UserHomePage user={user} />}
                    <Footer />
                </>
                :
                <>
                    <Header />
                    {(CURRENT_PATH === '/login' && user === null) && <Login />}
                    {((CURRENT_PATH === '/' || CURRENT_PATH === '/home') && user === null) && <Home />}
                    {CURRENT_PATH === '/signup' && <Signup />}
                    {CURRENT_PATH === '/menu' && <Menu />}
                    {CURRENT_PATH === '/reservation' && <Reservation />}
                    <Footer />
                </>
            )}
        </div>
    );
};