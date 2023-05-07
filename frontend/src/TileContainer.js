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

  for (let i = 0; i < data.length; i++) {
    // const { name, impact, p_impact, n_impact, overall} = data[i];
    console.log(data[i]);

    tiles.push(
      <div key={i} className="tile">
        <div className="header">{data[i].Name}</div>
        <div className="value">{data[i].Impact}</div>
      </div>
    //   Container({name, impact, p_impact, n_impact, overall})
    );
  }

  return <div className="tile-container">{tiles}</div>;
}

export default TileContainer;