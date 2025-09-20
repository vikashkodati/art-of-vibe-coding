import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [email, setEmail] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const characters = 'アカサタナハマヤラワガザダバパイキシチニヒミリヰギジヂビピウクスツヌフムユルグズヅブプエケセテネヘメレヱゲゼデベペオコソトノホモヨロヲゴゾドボポヴッン0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const fontSize = 14;
    const columns = canvas.width / fontSize;

    const drops = [];
    for (let x = 0; x < columns; x++) {
      drops[x] = 1;
    }

    function draw() {
      ctx.fillStyle = 'rgba(0, 0, 0, 0.04)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.fillStyle = '#00ff00';
      ctx.font = fontSize + 'px monospace';

      for (let i = 0; i < drops.length; i++) {
        const text = characters.charAt(Math.floor(Math.random() * characters.length));
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
          drops[i] = 0;
        }
        drops[i]++;
      }
    }

    const interval = setInterval(draw, 35);

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    window.addEventListener('resize', handleResize);

    return () => {
      clearInterval(interval);
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (email) {
      setIsSubmitted(true);
    }
  };

  return (
    <div className="App">
      <canvas id="matrix-canvas" className="matrix-canvas"></canvas>
      <header className="App-header">
        <h1>Recipe Sharing</h1>
        <p>Discover and share amazing recipes with food lovers around the world</p>

        {!isSubmitted ? (
          <div className="waitlist-section">
            <h2>Join the Waitlist</h2>
            <p>Be the first to know when we launch!</p>
            <form onSubmit={handleSubmit} className="waitlist-form">
              <input
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="email-input"
              />
              <button type="submit" className="signup-button">
                Join Waitlist
              </button>
            </form>
          </div>
        ) : (
          <div className="success-message">
            <h2>Thank you!</h2>
            <p>You've been added to our waitlist. We'll notify you when we launch!</p>
          </div>
        )}

        <div className="features-section">
          <h2>Platform Features</h2>
          <div className="features-grid">
            <div className="feature">
              <div className="feature-icon">🍳</div>
              <h3>Smart Recipe Discovery</h3>
              <p>AI-powered recommendations based on your taste preferences and dietary restrictions</p>
            </div>
            <div className="feature">
              <div className="feature-icon">👥</div>
              <h3>Community Sharing</h3>
              <p>Connect with fellow food enthusiasts and share your culinary creations with the world</p>
            </div>
            <div className="feature">
              <div className="feature-icon">📱</div>
              <h3>Interactive Cooking</h3>
              <p>Step-by-step guided cooking with timers, tips, and real-time adjustments</p>
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
