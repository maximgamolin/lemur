import React, { useState } from "react";
import { useTabState, Tab, TabList, TabPanel } from "reakit/Tab";
import { connect } from "redux-zero/react";

import Heading from "../../../typography/Heading";
import styles from './index.module.css';
import addIcon from './add.svg';
import removeIcon from './remove.svg';
import classNames from "classnames";

import DataProcessingView from './../../../blocks/DataProcessingView';
import actions from "../../../redux/actions";


function PrepareSelection({ datasetsInCollection, dataOperators, ...rest }) {
    const [selections, setSelections] = useState([]);
    const [datasets, setDatasets] = useState(datasetsInCollection);
    const [selectionId, setSelectionId] = useState(0);
    const [selectedSelection, setSelectedSelection] = useState();
    const [currentOperators, setCurrentOperators] = useState([...dataOperators.common, ...dataOperators.filter]);

    const tab = useTabState({ selectedId: "filterTab" });

    function handleChangeSelectionName(selection, e) {
        selection.name = e.target.value;
        setSelections([...selections.filter((item) => item.id !== selection.id), selection]);
    }

    function handleMoveToSelection(dataset) {
        setSelections([...selections, {
            id: selectionId,
            name: dataset.name,
            dataset: [dataset],
        }]);
        setSelectionId(selectionId + 1);
    }

    function handleDeleteSelection(e, id) {
        e.stopPropagation()
        setSelections([...selections.filter((x) => x.id !== id)]);
        if (selectedSelection && id === selectedSelection.id)
            setSelectedSelection({});
    }

    function handleSelectSelection(selection) {
        setSelectedSelection(selectedSelection && selection.id === selectedSelection.id ? -1 : selection);
    }

    console.log(currentOperators);

    return (
        <>
            <Heading size="h1">Подготовка выборок</Heading>

            <div className={styles.wrapper}>
                <div className={styles.list}>
                    {datasets.map((item) => (
                        <div onClick={() => handleMoveToSelection(item)} className={styles.datasetPreview}>
                            <span>{item.name}</span>
                            <img src={addIcon} alt=""/>
                        </div>
                    ))}
                </div>
                <div className={styles.list}>
                    {selections.sort((a, b) => a.id < b.id).map((item) => {
                        return (
                            <div onClick={() => handleSelectSelection(item)}
                                 className={classNames(styles.datasetPreview, styles.selectionPreview, {
                                     [styles.previewActive]: selectedSelection && item.id === selectedSelection.id
                                 })}>
                                <input type="text" value={item.name} onClick={(e) => e.preventDefault()}
                                       onChange={(e) => handleChangeSelectionName(item, e)}/>
                                <img src={removeIcon} alt=""
                                     onClick={(e) => handleDeleteSelection(e, item.id)}/>
                            </div>
                        )
                    })}
                </div>
            </div>

            {selectedSelection && (
                <>
                    <TabList {...tab} aria-label="My tabs">
                        <Tab {...tab} id="filterTab">Фильтрация</Tab>
                        <Tab {...tab}>Агрегация</Tab>
                        <Tab {...tab}>Добавление фичей</Tab>
                    </TabList>
                    <div className={styles.editor}>
                        <TabPanel {...tab}>
                            <DataProcessingView
                                operators={currentOperators}
                                addResBlock
                                datasets={selectedSelection.dataset}/>
                        </TabPanel>
                        <TabPanel {...tab}>Tab 2</TabPanel>
                        <TabPanel {...tab}>Tab 3</TabPanel>
                    </div>
                </>
            )}
        </>
    )
}

const mapToProps = ({ datasetsInCollection, dataOperators }) => ({ datasetsInCollection, dataOperators });

export default connect(mapToProps, actions)(PrepareSelection);
