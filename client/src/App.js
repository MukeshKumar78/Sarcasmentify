import './App.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { useState } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  const loadingMessages = ["Predicting...", "Backpropagating", "Optimizing", "Checking dataset", "Calculating accuracy"];
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [outputFlag, setOutputFlag] = useState(false);

  const handleChange = (e) => {
    setInput(e.target.value);
  }

  const notify = () => toast("Coming Soon!");

  const predict = () => {
    setOutputFlag(false);
    loadingMessages.forEach((msg, i) => {
      setTimeout(() => {
        if(!outputFlag)
          setOutput(msg)
      }, i*10)
    })

    fetch('/api/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({text: input})
    })
    .then(res => res.json())
    .then(res => {
      setOutputFlag(true);
      setOutput(res['prediction'] ? 'Sarcastic' : 'Not Sarcastic');
    })
  }

  return (
    <div className="App">
      <div className="Main">
        <div className="Input">
          <div className="News-input">
            <FontAwesomeIcon color="var(--accent)" icon="magic"/>
            <input onChange={handleChange} onKeyDown={(e) => {
              if(e.key == 'Enter') predict()
            }} className=""></input>
          </div>
        </div>
        <div className="Actions">
          <span id="Result" style={{color: output == 'Sarcastic' ? '#238823' : '#D2222D'}}> {output} </span>
        </div>
        <div className="Actions">
          <button onClick={predict}> Predict </button>
          <button onClick={notify}> Random </button>
        </div>
      </div>
      <ToastContainer 
      autoClose={1000}
      hideProgressBar={true}/>
    </div>
  );
}

export default App;
