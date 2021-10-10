import { BrowserRouter as Router, Route, Switch, useRouteMatch } from "react-router-dom";
import React, { useEffect } from "react";

import CreateSelection from './CreateSelection';
import PrepareSelection from './PrepareSelection';
import JoinSelections from './JoinSelections';
import SendToExport from './SendToExport';
import { connect } from "redux-zero/react";
import actions from "../../redux/actions";


function GenerateSelectionPage({ getActiveWorkpiece,...rest }) {
    let match = useRouteMatch();

    useEffect(() => {
        getActiveWorkpiece();
    }, []);

    return (
        <div>
            <Switch>
                <Route path={`${match.url}/export/`}>
                    <SendToExport/>
                </Route>
                <Route path={`${match.url}/join/`}>
                    <JoinSelections/>
                </Route>
                <Route path={`${match.url}/prepare/`}>
                    <PrepareSelection/>
                </Route>
                <Route path={`${match.url}`}>
                    <CreateSelection/>
                </Route>
            </Switch>
        </div>
    );
}

const mapToProps = ({  }) => ({  });

export default connect(mapToProps, actions)(GenerateSelectionPage);
