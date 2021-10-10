import createStore from "redux-zero";

const initialState = {
    availableTags: ['datasets', 'marketing', 'economy'],

    dataOperators: {
        common: [
            // { id: 1, category: 'Математика', name: 'sum', title: 'Сложение', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 2, category: 'Строки', name: 'str_len', title: 'Длина строки', inPorts: ['str'], outPorts: ['enl'] },

            { id: 5, category: 'Сравнение', name: 'eq', title: 'a == b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 6, category: 'Сравнение', name: 'gt', title: 'a > b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 7, category: 'Сравнение', name: 'gte', title: 'a >= b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 8, category: 'Сравнение', name: 'lt', title: 'a < b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 9, category: 'Сравнение', name: 'lte', title: 'a <= b', inPorts: ['a', 'b'], outPorts: ['res'] },

            { id: 10, category: 'Математика', name: 'sum', title: 'a + b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 11, category: 'Математика', name: 'sub', title: 'a - b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 12, category: 'Математика', name: 'mul', title: 'a * b', inPorts: ['a', 'b'], outPorts: ['res'] },
            { id: 13, category: 'Математика', name: 'div', title: 'a / b', inPorts: ['a', 'b'], outPorts: ['res'] },
        ],
        filter: [

        ],
        feature: [

        ],
        join: [],
    },
    workpiece: {},
    // dataOperators: {},
    datasetsInCollection: [],
    allDatasets: [],
};

const store = createStore(initialState);

export default store;
