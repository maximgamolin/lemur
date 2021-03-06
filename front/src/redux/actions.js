import toast from 'react-hot-toast';

import api from '../api';


const actions = store => ({
    loadDataset: async (state) => {
        api.get(api.URLS.getDatasets)
            .then((res) => {
                if (res)
                    store.setState({ allDatasets: res });
                else
                    toast.error('Не удалось загрузить датасеты');
            })
            .catch((err) => toast.error('Не удалось загрузить датасеты'));
    },
    addToCollection: async (state, id) => {
        api.post(api.URLS.addToCollection, { dataset_id: id })
            .then((res) => {
                if (res) {
                     toast.success('Датасет добавлен в коллекцию!');
                }
                else
                    toast.error('Не удалось загрузить датасеты');
            })
            .catch((err) => toast.error('Не удалось загрузить датасеты'));
    },

    initWorkpiece: async (state, name) => {
        return api.post(api.URLS.initWorkpiece, { name: name })
            .then((res) => {
                if (res) {
                    store.setState({ workpiece: res });
                }
                else
                    toast.error('Не удалось создать выборку');
            })
            .catch((err) => toast.error('Не удалось создать выборку'));
    },
    getActiveWorkpiece: async (state) => {
        api.get(api.URLS.getActiveWorkpiece)
            .then((res) => {
                if (res)
                    store.setState({ workpiece: res });
                else
                    toast.error('Не удалось загрузить выборку');
            })
            .catch((err) => toast.error('Не удалось загрузить выборку'));
    },

    loadProfile: async (state) => {
        // api.get(api.URLS.me)
        //     .then((res) => {
        //         console.log(res);
        //         if (res)
        //             store.setState({ profile: res });
        //         else
        //             toast.error('Не удалось загрузить профиль');
        //     })
        //     .catch((err) => toast.error('Не удалось загрузить профиль'));
    }
});

export default actions;
