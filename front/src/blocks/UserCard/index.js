import React from "react";
import classNames from "classnames";

import styles from './index.module.css';
import Heading from "../../typography/Heading";
import avatarPlaceholderIcon from './placeholder.svg';
import {connect} from "redux-zero/react";
import actions from "../../redux/actions";


function UserCard({ onClick, className, avatar, profile, ...rest }) {
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

const mapToProps = ({profile}) => ({profile});

export default connect(mapToProps, actions)(UserCard);
