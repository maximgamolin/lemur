import React, { useEffect } from "react";
import { Input } from "reakit/Input";
import { connect } from "redux-zero/react";
import toast from 'react-hot-toast';

import Heading from "../../typography/Heading";
import styles from './index.module.css';
import searchIcon from './img/search.svg';
import settingsIcon from './img/settings.svg';
import actions from "../../redux/actions";

import DatasetPreview from "../../blocks/DatasetPreview";


function DatasetListPage({ availableTags, addToCollection, allDatasets, loadDataset, ...rest }) {
    function handleAddDataset(id) {
        addToCollection(id);
    }

    useEffect(() => {
        loadDataset();
    }, []);

    console.log(allDatasets);

    return (
        <>
            <div>
                <Heading size="h1">VTB Datasets</Heading>
            </div>

            <div className={styles.searchInputRow}>
                <div className={styles.searchWrapper}>
                    <img src={searchIcon} className={styles.searchIcon} alt=""/>
                    <Input className={styles.searchInput} placeholder="Найти датасет" />
                    <div className={styles.filterWrapper}>
                        <img src={settingsIcon} alt=""/>
                        <button>
                            Фильтры
                        </button>
                    </div>
                </div>
                <div className={styles.tagsWrapper}>
                    {availableTags.map((item) => (
                        <button>{item}</button>
                    ))}
                </div>
            </div>

            <div>
                <Heading size="h2">Последние датасеты</Heading>
                <div className={styles.datasetList}>
                    {allDatasets.map((dataset) => (
                        <DatasetPreview key={dataset.id} id={dataset.id} onAddClick={() => handleAddDataset(dataset.id)}
                                        title={dataset.name} owner={dataset.owner} updated={new Date(dataset.updated_at)}
                                        descr={dataset.description} />
                    ))}
                </div>
            </div>
        </>
    )
}

const mapToProps = ({availableTags, allDatasets}) => ({availableTags, allDatasets});

export default connect(mapToProps, actions)(DatasetListPage);
