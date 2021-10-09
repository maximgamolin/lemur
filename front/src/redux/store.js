import createStore from "redux-zero";

const initialState = {
    availableTags: ['datasets', 'marketing', 'economy'],

    dataOperators: {
        common: [
            // { id: 1, category: 'Математика', name: 'sum', title: 'Сложение', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 2, category: 'Строки', name: 'str_len', title: 'Длина строки', inPorts: ['str'], outPorts: ['enl'] },
        ],
        filter: [
            { id: 5, category: 'Сравнение', name: 'eq', title: 'a == b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 6, category: 'Сравнение', name: 'gt', title: 'a > b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 7, category: 'Сравнение', name: 'gte', title: 'a >= b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 8, category: 'Сравнение', name: 'lt', title: 'a < b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 9, category: 'Сравнение', name: 'lte', title: 'a <= b', inPorts: ['a', 'b'], outPorts: ['res'] },
        ],
        feature: [],
        join: [],
    },
    datasetsInCollection: [
        {
            id: 1,
            name: 'group',
            schema: {
                'id': 'int',
            },
        },
        {
            id: 2,
            name: 'user',
            schema: {
                'id': 'int',
                'name': 'string',
                'session_id': 'int',
                'group_id': 'int',
            },
        },
        {
            id: 3,
            name: 'session',
            schema: {
                'id': 'int',
                'name': 'string',
            },
        },
    ],
    allDatasets: [],
    profile: {}
};

const store = createStore(initialState);

export default store;
