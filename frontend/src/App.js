import React, { useState } from 'react';
import Avatar from './components/Avatar';
import axios from 'axios';
import './App.css';

const App = () => {
  const [text, setText] = useState('');
  const [audioUrl, setAudioUrl] = useState(null);

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handleSpeak = async () => {
    const response = await axios.post('http://localhost:8000/api/speak', { text });
    setAudioUrl(response.data.audioUrl);
  };

  return (
    <div className="App">
      <textarea value={text} onChange={handleTextChange} placeholder="Type your text here..."></textarea>
      <button onClick={handleSpeak}>Speak</button>
      <Avatar audioUrl={audioUrl} />
    </div>
  );
};

export default App;
