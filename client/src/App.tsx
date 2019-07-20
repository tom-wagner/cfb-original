import React, { useEffect } from 'react';
const axios = require('axios');

const App: React.FC = () => {
  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/")
      .then((data: string) => {
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
