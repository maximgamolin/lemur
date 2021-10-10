import React, { useEffect, useState } from "react";
import { useTabState, Tab, TabList, TabPanel } from "reakit/Tab";
import { connect } from "redux-zero/react";
import toast from 'react-hot-toast';

import Heading from "../../../typography/Heading";
import styles from './index.module.css';
import addIcon from './add.svg';
import removeIcon from './remove.svg';
import classNames from "classnames";

import DataProcessingView from './../../../blocks/DataProcessingView';
import Stages from "../../../blocks/Stages";
import actions from "../../../redux/actions";
import { Button } from "reakit/Button";
import api from "../../../api";


function PrepareSelection({ workpiece, dataOperators, ...rest }) {
    const [selections, setSelections] = useState([]);
    const [selectionId, setSelectionId] = useState(0);
    const [selectedSelection, setSelectedSelection] = useState();
    const [currentOperators, setCurrentOperators] = useState([...dataOperators.common, ...dataOperators.filter]);

    const [filterData, setFilterData] = useState({});
    const [aggregateData, setAggregateData] = useState({});
    const [featureData, setFeatureData] = useState({});

    const tab = useTabState({ selectedId: "filterTab" });

    useEffect(() => {
        const node = document.querySelector(`.${styles.isNew} input`);
        if (node)
            node.select();
    }, [selections]);

    function handleChangeSelectionName(selection, e) {
        selection.name = e.target.value;
        setSelections([...selections.filter((item) => item.id !== selection.id), selection]);
    }

    function handleMoveToSelection(dataset) {
        setSelections([...selections, {
            id: selectionId,
            name: dataset.name,
            dataset: [dataset],
            is_new: true,
        }]);
        setSelectionId(selectionId + 1);
    }

    function handleDeleteSelection(e, id) {
        e.stopPropagation()
        setSelections([...selections.filter((x) => x.id !== id)]);
        if (selectedSelection && id === selectedSelection.id)
            setSelectedSelection();
    }

    function handleSelectSelection(selection) {
        setSelectedSelection(selectedSelection && selection.id === selectedSelection.id ? -1 : selection);
    }

    function handleChangeOperators(category) {
        if (category === 'filter')
            setCurrentOperators([...dataOperators.common, ...dataOperators.filter]);
        else if (category === 'feature')
            setCurrentOperators([...dataOperators.common, ...dataOperators.feature]);
    }

    function handleSave(e) {
        console.log(filterData);
        console.log(featureData);
        console.log(aggregateData);
        // api.post(api.URLS.createDataPeace, {
        //     name: selectedSelection.name,
        //     dataset_id: selectedSelection.dataset[0].id,
        //     workpiece_id: workpiece.id,
        //     raw_filtering: filterData,
        //     raw_features: featureData,
        //     raw_aggregation: aggregateData,
        // })
        //     .then((res) => toast.success('Выборка сохранена!'))
        //     .catch((res) => toast.error('Ошибка при сохранении выборки'))
    }

    function handleAggregation(field) {
        if (field in aggregateData)
            return () => setAggregateData([...aggregateData.filter((item) => item !== field)])
        return () => setAggregateData([...aggregateData, field]);

    }

    return (
        <>
            <Stages stages={['Создание нового датасета', 'Подготовка выборки', 'Объединение выборок', 'Экспорт']}
                    activeNum={1} />

            <div className={styles.wrapper}>
                <div className={styles.list}>
                    <Heading className={styles.heading} size="h3">Датасеты</Heading>
                    {workpiece.parental_datasets && workpiece.parental_datasets.map((item) => (
                        <div onClick={() => handleMoveToSelection(item)} className={styles.datasetPreview}>
                            <span>{item.name}</span>
                            <img src={addIcon} alt=""/>
                        </div>
                    ))}
                </div>
                <div className={styles.list}>
                    <Heading className={styles.heading} size="h3">Выборки</Heading>
                    {selections.sort((a, b) => a.id < b.id).map((item) => {
                        const is_new = item.is_new;
                        item.is_new = false;
                        return (
                            <div onClick={() => handleSelectSelection(item)}
                                 className={classNames(styles.datasetPreview, styles.selectionPreview, {
                                     [styles.previewActive]: selectedSelection && item.id === selectedSelection.id,
                                     [styles.isNew]: is_new,
                                 })}>
                                <input type="text" value={item.name}
                                       onClick={(e) => e.preventDefault()}
                                       onChange={(e) => handleChangeSelectionName(item, e)}/>
                                <img src={removeIcon} alt=""
                                     onClick={(e) => handleDeleteSelection(e, item.id)}/>
                            </div>
                        )
                    })}
                </div>
            </div>

            {selectedSelection ? (
                <>
                    <TabList className={styles.tabHeader} {...tab} aria-label="My tabs">
                        <div>
                            <Tab {...tab} id="filterTab">Фильтрация</Tab>
                            <Tab {...tab}>Агрегация</Tab>
                            <Tab {...tab}>Добавление фичей</Tab>
                        </div>
                        <div>
                            <Button>Продолжить</Button>
                            <Button onClick={handleSave} className={styles.saveButton}>Сохранить выборку</Button>
                        </div>
                    </TabList>
                    <div className={styles.editor}>
                        <TabPanel {...tab} onClick={() => handleChangeOperators('filter')}>
                            <DataProcessingView
                                onChange={(data) => setFilterData(data)}
                                operators={currentOperators}
                                addResBlock
                                datasets={selectedSelection.dataset}/>
                        </TabPanel>
                        <TabPanel {...tab}>
                            <div className={styles.checkboxWrapper}>
                                {selectedSelection.dataset && selectedSelection.dataset[0].fields && selectedSelection.dataset[0].fields.map((field) => (
                                    <label className={styles.checkbox}>
                                        <input type="checkbox" onClick={handleAggregation}/>
                                        {field.name}
                                    </label>
                                ))}
                            </div>
                        </TabPanel>
                        <TabPanel {...tab} onClick={() => handleChangeOperators('feature')}>
                            <DataProcessingView
                                onChange={(data) => {
                                    console.log('f');
                                    setFeatureData(data);
                                }}
                                operators={currentOperators}
                                datasets={selectedSelection.dataset}/>
                        </TabPanel>
                    </div>
                </>
            ) : <Button>Продолжить</Button>}
        </>
    )
}

const mapToProps = ({ workpiece, dataOperators }) => ({ workpiece, dataOperators });

export default connect(mapToProps, actions)(PrepareSelection);
