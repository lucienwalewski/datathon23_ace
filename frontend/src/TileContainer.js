import React from 'react';
import './TileContainer.css';
// import Container from './Container';
// import Card from '@material-ui/core';

function TileContainer({ data }) {

  const capitalizeFirst = str => {
    str = str.trim();
    return str.charAt(0).toUpperCase() + str.slice(1);
  };

  const tiles = [];
  // console.log(data);
  // console.log(data.length);
  // console.log(data[0].Name);
  // console.log(typeof(data));

  // data = JSON.parse(data);

  for (let i = 0; i < data.length; i++) {
    // const { name, impact, p_impact, n_impact, overall} = data[i];
    console.log(data[i]);

    tiles.push(
      <div key={i} className="tile">
        <div className="header">{data[i].Name}</div>
        <div className="value">{data[i].Impact}</div>
        <div className="value">
          <h3>Positive Impact</h3>
          <ul>
          {data[i].PositiveImpact.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
          </div>
        <div className="value">
          <h3>Negative Impact</h3>
          <ul>
          {data[i].NegativeImpact.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
        </div>
      </div>
    //   Container({name, impact, p_impact, n_impact, overall})
    );
  }

  return <div className="tile-container">{tiles}</div>;
}

export default TileContainer;