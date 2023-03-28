import axios from 'axios';

var md5 = require('md5');

class BackEndConnectionImpl {
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