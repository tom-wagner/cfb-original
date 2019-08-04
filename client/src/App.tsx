import React from 'react';
import 'semantic-ui-css/semantic.min.css'
import { createBrowserHistory } from 'history';
import { Grid } from 'semantic-ui-react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import NavBar from './modules/Nav/NavBar';
import TeamRatingsTable from './modules/TeamRatings/TeamRatingsTable';
import SimulationTable from './modules/SimulationTable/SimluationTable';

const history = createBrowserHistory();
history.listen((location, action) => {
  // location is an object like window.location
  console.log(action, location.pathname, location.state);
});

const App: React.FC = () => (
  <Router>
    <Route component={NavBar} />
    <Grid style={{ padding: '20px 50px' }}>
      <Route exact path="/home" component={() => <p>Home Page TBD</p>}/>
      <Route path="/team-ratings" component={TeamRatingsTable}/>
      <Route path="/simulate" component={SimulationTable}/>
    </Grid>
  </Router>
);

export default App;
