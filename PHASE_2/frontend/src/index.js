import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

const apiFetch = (end_date, start_date, key_terms, location) => { 
  return new Promise((resolve, reject) => {
      fetch(`https://seng3011-bobby-tables-backend.herokuapp.com/article?end_date=${end_date}T00%3A00%3A00&start_date=${start_date}T00%3A00%3A00&key_terms=${key_terms}&location=${location}&limit=1000&offset=0`)
      .then((response) => {
          if (response.status === 400 || response.status === 403) {
              response.json().then((errorMsg) => {
                  alert(errorMsg['error']);
                  reject(errorMsg['error']);
              });
          }else if(response.status === 200) {
              response.json().then(data => {
                  resolve(data);
              });
          }
      })
      .catch((err) => console.log(err));
  });
}

export default apiFetch