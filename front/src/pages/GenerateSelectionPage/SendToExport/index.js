import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import toast from 'react-hot-toast';
import Stages from "../../../blocks/Stages";
import { connect } from "redux-zero/react";
import actions from "../../../redux/actions";
import styles from "./index.module.css";
import Button from "react-bootstrap/Button";
import api from "../../../api";


function SendToExport({ dataOperators, workpiece, ...rest }) {
    const [res, setRes] = useState('adwwadawd');


    function handleSend() {
        api.post(api.URLS.createTask, { workpiece_id: workpiece.id })
            .then((res) => {
                toast.success('Задание создано!')
                setRes(res);
            })
            .catch(() => toast.error('Не удалось создать задание'))
    }

    return (
        <>
            <Stages stages={['Создание нового датасета', 'Подготовка выборки', 'Объединение выборок', 'Экспорт']}
                    activeNum={3} />

            <div className={styles.wrapper}>
                <Button className={styles.button} onClick={handleSend}>Отправить на обработку</Button>
            </div>

            {res && (
                <div className={styles.result}>
                    {res}
                </div>
            )}

        </>
    )
}

const mapToProps = ({workpiece, dataOperators}) => ({workpiece, dataOperators});

export default connect(mapToProps, actions)(SendToExport);
