import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";

const App = () => (
  <div>
    <h1>Heyyo welcome to the Coop</h1>
    <h3>Currently logged in as: <strong>???</strong></h3>
    <DataProvider 
      endpoint="api/products/"
      render={data => <Table data={data} />} 
    />
  </div>
);

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;
