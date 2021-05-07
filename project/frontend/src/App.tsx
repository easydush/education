
import React from 'react';
import { Routes as R } from './constants';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { Login, Main } from './pages';
import { PrivateRoute } from './components/PrivateRoute';
import { Registration } from "./pages/Registration";

function App(): JSX.Element {
  return (
    <Router>
      <Switch>
        <Route exact component={Login} path={R.LOGIN} />
        <Route exact component={Registration} path={R.REGISTRATION} />
        <PrivateRoute exact component={Main} path={R.ROOT} />
        <PrivateRoute exact component={Main} path={R.MAIN} />
      </Switch>
    </Router>
  );
}

export default App;
