import axios from 'axios';

var md5 = require('md5');

class BackEndConnectionImpl {
    async add_user(fullName, email, password, callback) {
        let query = { 'fullname': fullName, 'email': email, 'password': password }

        return axios.post('/user/add', {})
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