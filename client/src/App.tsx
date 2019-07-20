import React, { useEffect, useState } from 'react';
import axios, { AxiosResponse } from 'axios';
import { BASE_API_URL } from './constants/constants';

const App: React.FC = () => {
  const [apiStatus, setApiStatus] = useState<string>("Maybe");

  useEffect(() => {
    axios
      .get(BASE_API_URL)
      .then((data: AxiosResponse) => setApiStatus("Yes"))
      .catch(() => setApiStatus("No"))
  }, [])

  return (
    <div>
      <header>
        <p>Is flask working? {apiStatus}</p>
      </header>
    </div>
  );
}

export default App;
