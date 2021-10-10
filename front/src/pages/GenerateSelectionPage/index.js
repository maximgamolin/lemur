import { BrowserRouter as Router, Route, Switch, useRouteMatch } from "react-router-dom";
import React from "react";

import CreateSelection from './CreateSelection';
import PrepareSelection from './PrepareSelection';


function GenerateSelectionPage({ ...rest }) {
    let match = useRouteMatch();

    console.log(match);

    return (
        <div>
            <Switch>
                <Route path={`${match.url}/prepare`}>
                    <PrepareSelection/>
                </Route>
                <Route path={`${match.url}`}>
                    <CreateSelection/>
                </Route>
            </Switch>
        </div>
    );
}

export default GenerateSelectionPage;
