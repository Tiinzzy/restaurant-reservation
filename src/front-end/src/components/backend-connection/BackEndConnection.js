import axios from 'axios';

var md5 = require('md5');

class BackEndConnectionImpl {
    #user = null;

    async add_user(name, email, password, birthday, callback) {
        let query = { name, email, 'password': md5(password), birthday }
        return axios.post('api/user/add', query, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data;
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async authentication_login(user, password, callback) {
        this.#user = user;

        let query = { user, 'password': md5(password) }
        return axios.post('/api/authentication/login', query, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data;
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async authentication_is_login(callback) {
        return axios.post('/api/authentication/is_login', { 'username': this.#user }, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data;
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async authentication_logout(user, callback) {
        return axios.post('/api/authentication/logout', { 'username': user }, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data;
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

}

export default class BackEndConnection {
    static #object = null;

    static INSTANCE() {
        if (BackEndConnection.#object === null) {
            BackEndConnection.#object = new BackEndConnectionImpl();
        }
        return BackEndConnection.#object;
    }

}