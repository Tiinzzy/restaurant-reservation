import React, { useState, useEffect } from "react";

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
const FOOTER_OFFSET = 200

let callCounter = 0;

function checkUserLogin(setIsLogin, setUser, setPageReady) {
    let sessionId = localStorage.getItem('sessionId');
    window.history.pushState({}, "", "/");
    backend.authentication_is_login(sessionId, (data) => {
        if (data.is_login) {
            setIsLogin(true);
            setUser({ username: data.user, roles: data.roles, sessionId: data.session_id });
        } else {
            setIsLogin(false);
            setUser(null);
        }
        setPageReady(true);
    })
}

function getWindowSize() {
    return { h: window.innerHeight, w: window.innerWidth }
}

export default function App() {
    const [isLogin, setIsLogin] = useState(false);
    const [user, setUser] = useState(null);
    const [pageReady, setPageReady] = useState(false);
    const [windowSize, setWindowSize] = useState(getWindowSize());

    if (callCounter++ < 1) {
        checkUserLogin(setIsLogin, setUser, setPageReady);
    }

    useEffect(() => {
        function resizeHandler() {
            setWindowSize(getWindowSize())
        }
        window.addEventListener('resize', resizeHandler);
        return () => window.removeEventListener('resize', resizeHandler);
    })

    return (
        <div>
            {pageReady && (isLogin ?
                <>
                    <HeaderLogin user={user} />
                    <div style={{ height: windowSize.h - FOOTER_OFFSET }}>
                        {user !== null && user.roles.includes('Admin') && <AdminHomePage user={user} />}
                        {user !== null && user.roles.includes('Customer') && <UserHomePage user={user} />}
                        {user !== null && user.roles.includes('Waiter') && <WaiterHomePage user={user} />}
                    </div>
                    <Footer />
                </>
                :
                <>
                    <Header />
                    <div style={{ height: windowSize.h - FOOTER_OFFSET }}>
                        {(CURRENT_PATH === '/login' && user === null) && <Login />}
                        {((CURRENT_PATH === '/' || CURRENT_PATH === '/home') && user === null) && <Home />}
                        {CURRENT_PATH === '/signup' && <Signup />}
                        {CURRENT_PATH === '/menu' && <Menu />}
                        {CURRENT_PATH === '/reservation' && <Reservation />}
                    </div>
                    <Footer />
                </>
            )}
        </div>
    );
};



