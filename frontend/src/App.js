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
      .then((response) => {
        return response.json();
      })
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
      <div className="upper">
        <input
          type="text"
          className="input"
          value={inputValue}
          onChange={handleInputChange}
          placeholder="Enter text here..."
        />
        <button className="button" onClick={handleButtonClick}>
          Send
        </button>
      </div>
      <div className="lower">
        {loading && <div className="spinner"></div>}
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
