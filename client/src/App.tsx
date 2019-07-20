import React, { useEffect } from 'react';
import axios, { AxiosResponse } from 'axios';

const App: React.FC = () => {
  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/")
      .then((data: AxiosResponse) => {
        console.log('is flask working??', data)
      })
  }, [])

  return (
    <div>
      <header>
        <p>Hello world</p>
      </header>
    </div>
  );
}

export default App;
