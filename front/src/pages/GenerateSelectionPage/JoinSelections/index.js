import React from "react";
import { useHistory } from "react-router-dom";
import toast from 'react-hot-toast';
import Stages from "../../../blocks/Stages";
import { connect } from "redux-zero/react";
import actions from "../../../redux/actions";
import DataProcessingView from "../../../blocks/DataProcessingView";
import styles from "./index.module.css";
import Button from "react-bootstrap/Button";


function JoinSelections({ dataOperators, workpiece, ...rest }) {
    const history = useHistory();

    function handleContinue() {
        history.push('/collections/export/');
    }

    return (
        <>
            <Stages stages={['Создание нового датасета', 'Подготовка выборки', 'Объединение выборок', 'Экспорт']}
                    activeNum={2} />

            <div className={styles.continueWrapper}>
                <Button onClick={handleContinue}>Продолжить</Button>
            </div>
            {workpiece.parental_datasets && (
                <DataProcessingView
                    operators={dataOperators.common}
                    addResBlock
                    datasets={workpiece.parental_datasets}/>
            )}

        </>
    )
}

const mapToProps = ({workpiece, dataOperators}) => ({workpiece, dataOperators});

export default connect(mapToProps, actions)(JoinSelections);
