import './App.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { useState } from 'react';

function App() {
  const loadingMessages = ["Predicting...", "Backpropagating", "Optimizing", "Checking dataset", "Calculating accuracy"];
  const [input, setInput] = useState('');


  const handleChange = (e) => {
    setInput(e.target.value);
  }

  const predict = () => {
    fetch('/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: {
        text: input
      }
    })
  }

  return (
    <div className="App">
      <div className="Main">
        <div className="Input">
          <div className="News-input">
            <FontAwesomeIcon color="var(--accent)" icon="magic"/>
            <input onChange={handleChange} onKeyDown={(e) => {
              if(e.key = 'enter') predict()
            }} className=""></input>
          </div>
        </div>
        <div className="Actions">
          <span id="Result"> Predicting... </span>
        </div>
        <div className="Actions">
          <button onClick={predict}> Predict </button>
          <button> Random </button>
        </div>
      </div>
    </div>
  );
}

export default App;
