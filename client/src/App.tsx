import React, { useEffect, useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import { BASE_API_URL } from './constants/constants';
import _ from 'lodash';
// TODO: Figure out how to use path properly
// import path from 'path';

const App: React.FC = () => {
  const [teamData, setApiStatus] = useState<{} | string>("Loading...");

  useEffect(() => {
    axios
      // TODO move all API logic to an \`api` file
      .get(`${BASE_API_URL}/schedule`, { 'params': { 'year': 2019 }})
      .then((data: AxiosResponse) => {
        console.log({ data });
        setApiStatus(data)
      })
      .catch(() => setApiStatus("error!!"))
  }, [])

  let pageContent;

  if (typeof teamData === "string") {
    pageContent = <p>{teamData}</p>
  }

  if (typeof teamData === "object") {
    return (
      <ul>
        {_.map(teamData, team => <li>{JSON.stringify(team)}</li>)}
      </ul>
    )
  }

  return (
    <div>
      <header>
        {pageContent}
      </header>
    </div>
  );
}

export default App;
