import React, { useState } from "react";
import './App.css';
import TileContainer from './TileContainer';

function App() {
  const [inputValue, setInputValue] = useState("");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleButtonClick = () => {
    console.log("Button clicked");
    setResponse(false);
    setLoading(true);
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body : JSON.stringify({data : inputValue})
    };
    console.log("Request options: " + requestOptions);
    fetch("http://localhost:8000/generate_response", requestOptions) 
      .then((response) => response.json())
      // .then((response) => response.json())
      .then((data) => {
        setResponse(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error(error);
        setLoading(false);
      });
  };

  return (
    <div className="container">
      <div className="logo">
        ImpactTracker
      </div>
      <div className="upper">
      <input
          type="text"
          className="input"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Enter text here..."
        />
        <button className="button" onClick={handleButtonClick}>
          Evaluate
        </button>
        {/* <div class="header">
          <h1>Known Impact</h1>
        </div>
        <div class="content">
        </div> */}
      </div>
      <div className="lower">
        {loading && <div className="box"> <div className="spinner"></div> </div>}
        {response && (
          <div style={{ '--num-tiles': response.length }}>
            <TileContainer data={response} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
