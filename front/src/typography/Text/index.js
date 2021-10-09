import React from "react";
import classNames from "classnames";

import styles from './index.module.css';


function Text({ className, size, children, ...rest }) {
    return (
        <p className={classNames(className, styles.text, styles[`${size}Size`])} {...rest}>{children}</p>
    )
}

export default Text;
