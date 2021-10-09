import cookies from "browser-cookies";

const HOST = 'http://127.0.0.1:8000/api/v1/';

const api = {
    URLS: {
        getDatasets: 'stock/datasets/',
        addToCollection: 'market/collection-items/',
    },

    formatUrl: function () {
        let s = arguments[0];
        for (let i = 0; i < arguments.length - 1; i++) {
            const reg = new RegExp("\\{" + i + "\\}", "gm");
            s = s.replace(reg, arguments[i + 1]);
        }
        return s;
    },

    post: (url, data) => {
        return fetch(HOST + url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-CSRFToken': cookies.get('csrftoken'),
            },
            body: JSON.stringify(data),
        })
            .then((res) => res.json());
    },

    get: function (url) {
        return fetch(HOST + url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-CSRFToken': cookies.get('csrftoken'),
            },
        })
            .then((res) => res.json());
    }
}

export default api;
