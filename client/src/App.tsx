import React, { useEffect, useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import { BASE_API_URL } from './constants/constants';
import _ from 'lodash';

const App: React.FC = () => {
  const [teamData, setApiStatus] = useState<{} | string>("Loading...");

  useEffect(() => {
    axios
      .get(BASE_API_URL)
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
