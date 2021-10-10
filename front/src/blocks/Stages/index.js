import React from "react";
import styles from "./index.module.css";
import classNames from "classnames";


function Stages({ stages, activeNum, ...rest }) {

    let counter = 0;
    let nodes = stages.map(stage => (
        <div className={classNames(styles.stage, {[styles.activeStage]: counter++ === activeNum} )}>
            <span className={styles.stageInner}>{stage}</span>
        </div>
    ));
    return (
        <div className={styles.stages}>
            {nodes}
        </div>
    )
}

export default Stages;
