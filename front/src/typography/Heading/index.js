import React from "react";
import classNames from "classnames";

import styles from './index.module.css';


function Heading({ className, size, children, ...rest }) {

    switch (size) {
        case 'h1':
            return <h1 className={classNames(className, styles.h, styles.h1)} {...rest}>{children}</h1>;
        case 'h2':
            return <h2 className={classNames(className, styles.h, styles.h2)} {...rest}>{children}</h2>;
        case 'h3':
            return <h3 className={classNames(className, styles.h, styles.h3)} {...rest}>{children}</h3>;
        case 'h4':
            return <h4 className={classNames(className, styles.h, styles.h4)} {...rest}>{children}</h4>;
        default:
            return <span className={styles.h} {...rest}>{children}</span>;
    }
}

export default Heading;
