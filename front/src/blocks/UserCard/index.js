import React from "react";
import classNames from "classnames";

import styles from './index.module.css';
import Heading from "../../typography/Heading";
import avatarPlaceholderIcon from './placeholder.svg';


function UserCard({ onClick, className, avatar, ...rest }) {
    return (
        <div onClick={onClick} className={classNames(className, styles.wrapper)} {...rest}>
            <div className={styles.avatar}>
                <img src={avatar??avatarPlaceholderIcon} alt=""/>
            </div>
            <div className={styles.namesurname}>
                <Heading className={styles.text} size="h3">Иия</Heading>
                <Heading className={styles.text} size="h3">Фамилия</Heading>
            </div>
        </div>
    )
}

export default UserCard;
