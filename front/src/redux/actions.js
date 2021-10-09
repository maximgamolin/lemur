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
});

export default actions;
