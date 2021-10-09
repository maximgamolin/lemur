import React from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
import { Provider } from "redux-zero/react";
import { Toaster } from 'react-hot-toast';
import { Provider as ReakitProvider } from "reakit";
import * as system from "reakit-system-bootstrap";

import DatasetListPage from '../pages/DatasetListPage';
import GenerateSelectionPage from '../pages/GenerateSelectionPage';
import UserCard from "../blocks/UserCard";

import styles from './index.module.css';
import './common.css';
import logo from './logo.svg';
import store from './../redux/store';


function App({ ...rest }) {
    return (
        <Provider store={store}>
            <ReakitProvider unstable_system={system}>
                <Router>
                    <div className={styles.wrapper}>
                        <div className={styles.sideMenu}>
                            <Link to="/"><img className={styles.logo} src={logo} alt="Логотип"/></Link>
                            <UserCard className={styles.userCard}/>
                        </div>

                        <main className={styles.mainBlock}>
                            <Switch>
                                <Route path="/collections">
                                    <GenerateSelectionPage/>
                                </Route>
                                <Route path="/">
                                    <DatasetListPage/>
                                </Route>
                            </Switch>
                        </main>

                        <Toaster toastOptions={{
                            style: {
                                borderRadius: '4px',
                                fontFamily: 'VTBGroupUI',
                            },
                        }}/>
                    </div>
                </Router>
            </ReakitProvider>
        </Provider>
    )
}

export default App;
