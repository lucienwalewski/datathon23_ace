import React from 'react';
import './TileContainer.css';
// import Container from './Container';
// import Card from '@material-ui/core';

function TileContainer({ data }) {
  const tiles = [];

  for (let i = 0; i < data.length; i++) {
    const { name, impact, p_impact, n_impact, overall} = data[i];
    console.log(data[i]);

    tiles.push(
      // <div key={i} className="tile">
      //   <h3>{name}</h3>
      //   <p>{impact}</p>
      // </div>
      <div key={i} className="tile">
        <div className="header">{name}</div>
        <div className="value">{impact}</div>
      </div>
    //   Container({name, impact, p_impact, n_impact, overall})
    );
  }

  return <div className="tile-container">{tiles}</div>;
}

export default TileContainer;