# ACE Dataphon AWS challenge 

## Description

Certain minority stakeholders are often inadvertently overlooked when implemented (government) policies. We provide a web application that takes in a policy in the format of a string, identifies the key stakeholders that may be marginalised and provides a short summary on each of them.

## Setup

- Run `python3 setup.py` to run the backend server. It assumes that the AWS endpoint is running.
- `cd frontend` to navigate to the frontend. Then run `npm install` and `npm start` to install the necessary packages and launch the React frontend.

## File hierarchy

```
/frontend
  /public  - Public resources
  /src  - Frontend resources
    App.css
    App.js
    Container.js
    index.css
    index.js
    TileContainer.css
    TileContainer.js
  package.json  - Package installations
  package-lock.json
server.py  - Runs local backend server that makes the communication between frontend and AWS endpoint.
utils.py. - Code to process responses from AWS endpoint and generate final json output.
```

## Todo

- Fix frontend bugs
- Incorporate generated images of stakeholders next to summaries
