import React from "react";
import classNames from "classnames";
import moment from "moment";
import 'moment/locale/ru';

import styles from './index.module.css';
import Heading from "../../typography/Heading";
import Text from "../../typography/Text";
import ownerIcon from './owner.svg';
import clockIcon from './clock.svg';
import placeholderIcon from './placeholder.svg';
import addIcon from './add.svg';


moment.locale('ru');

function DatasetPreview({ onClick, className, img, title, owner, updated, descr, onAddClick, ...rest }) {
    return (
        <div onClick={onClick} className={classNames(className, styles.wrapper)} {...rest}>
            <img className={styles.img} src={img??placeholderIcon} alt="" />
            <div className={styles.content}>
                <Heading size="h3">{title}</Heading>
                <div className={styles.info}>
                    <Text className={styles.text} size="xs">
                        {owner ? (<>
                            <img src={clockIcon} alt=""/>
                            {owner}
                        </>) : ''}
                    </Text>
                    <Text className={styles.text} size="xs">
                        {updated ? (<>
                            <img src={clockIcon} alt=""/>
                            {moment(updated).fromNow()}
                        </>) : ''}
                    </Text>
                </div>
                <Text className={classNames(styles.text, styles.descr)} size="xs">{descr}</Text>
            </div>
            <img className={styles.addIcon} onClick={onAddClick} src={addIcon} alt=""/>
        </div>
    )
}

export default DatasetPreview;
