import ReactDOM from 'react-dom/client';
// import App from './App.tsx';
import Chat from './Chat.tsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
<div>
    <div className="chatbot-container">
      <h1 className="chatbot-title">Medicine Chatbot</h1> {/* Add the chatbot-title class */}
      <Chat />
    </div>
  </div>
);
