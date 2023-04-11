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

    async authentication_login(user, password, userId, callback) {
        this.#user = user;

        let query = { user, 'password': md5(password), 'user_id': userId }
        return axios.post('/api/authentication/login', query, {})
            .then(function (response) {
                if (callback) {
                    localStorage.setItem('sessionId', response.data.session_id);
                    callback(response.data);
                }
                return response.data;
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async authentication_is_login(sessionId, callback) {
        return axios.post('/api/authentication/is_login', { 'session_id': sessionId }, {})
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

    async authentication_logout(sessionId, callback) {
        return axios.post('/api/authentication/logout', { 'session_id': sessionId }, {})
            .then(function (response) {
                if (callback) {
                    localStorage.setItem('sessionId', null);
                    callback(response.data);
                }
                return response.data;
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async add_menu_item(name, category, price, description, callback) {
        let query = { 'name': name, 'category': category, 'price': price, 'description': description };
        return axios.post('/api/menu-item/add', query, {})
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

    async all_menu_items(callback) {
        return axios.post('/api/menu-item/all', {}, {})
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

    async load_menu_item(id, callback) {
        return axios.post('/api/menu-item/load', { 'id': id }, {})
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

    async update_menu_item(id, name, category, price, description, callback) {
        let query = { 'id': id, 'name': name, 'category': category, 'price': price, 'description': description };
        return axios.post('/api/menu-item/update', query, {})
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

    async add_reservation(query, callback) {
        return axios.post('/api/reservation/add', query, {})
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

    async all_reservations(callback) {
        return axios.post('/api/reservation/all', {}, {})
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

    async load_reservation(id, callback) {
        return axios.post('api/reservation/load', { 'id': id }, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async update_reservation(query, callback) {
        return axios.post('api/reservation/update', query, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async load_user_by_email(email, callback) {
        return axios.post('api/user/load-by-email', { 'email': email }, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async update_user(query, callback) {
        return axios.post('api/user/update', query, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async add_order_item(query, callback) {
        return axios.post('api/order-item/add', query, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async all_order_items(reservationId, callback) {
        return axios.post('api/order-item/all', { 'reservation_id': reservationId }, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async update_order_item(query, callback) {
        return axios.post('api/order-item/update', query, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async delete_order_item(query, callback) {
        return axios.post('api/order-item/delete', query, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async add_user_role(query, callback) {
        return axios.post('api/user/add-role', query, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
            })
            .catch(function (error) {
                console.log(error);
                return false;
            })
    }

    async delete_menu_item(callback) {
        return axios.post('api/menu-item/delete', {}, {})
            .then(function (response) {
                if (callback) {
                    callback(response.data);
                }
                return response.data
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