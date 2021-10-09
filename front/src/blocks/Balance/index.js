import React from "react";
import classNames from "classnames";
import { Link } from "react-router-dom";

import styles from './index.module.css';
import Text from "../../typography/Text";
import moneyIcon from './money.svg'


function UserCard({ onClick, className, avatar, ...rest }) {
    return (
        <div className={classNames(className, styles.wrapper)} {...rest}>
            <div className={styles.inner}>
                <img src={moneyIcon} alt=""/>
                <div>
                    <Text size="s">256 000.00 ₽</Text>
                    <Link>Пополнить баланс</Link>
                </div>
            </div>
        </div>
    )
}

export default UserCard;
