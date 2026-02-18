import React, { useState } from "react";
import axios from "axios";

const PredictForm = () => {
  const [features, setFeatures] = useState([
    0.0077721980079471205,
    0.46153846153846156,
    0.0,
    0.0,
    0.0,
    0.11908418421807722,
    0.7942634013278564,
    0.17217382428507993,
    0.7869361310365848,
    0.0,
    0.0,
    0.0,
    0.41400308521923995,
    0.1869060352964757,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    1.0,
    0.0
  ]); // Adjust for your feature count
  const [prediction, setPrediction] = useState(null);
  const [probability, setProbability] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (index, value) => {
    const updatedFeatures = [...features];
    updatedFeatures[index] = parseFloat(value) || 0;
    setFeatures(updatedFeatures);
  };

  const handlePredict = async () => {
    try {
      setError(null);
      const response = await axios.post("http://127.0.0.1:5000/predict", {
        features: features,
      });
      setPrediction(response.data.prediction);
      setProbability(response.data.probability);
    } catch (error) {
      console.error("Error during prediction:", error);
      setError(error.message);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif", maxWidth: "800px", margin: "0 auto" }}>
      <h1 style={{ color: "#333", textAlign: "center" }}>🔐 SafePayAI - Fraud Detection</h1>
      <h2 style={{ color: "#666" }}>Random Forest Prediction</h2>
      
      <div style={{ 
        display: "grid", 
        gridTemplateColumns: "repeat(auto-fit, minmax(150px, 1fr))",
        gap: "15px",
        marginBottom: "20px"
      }}>
        {features.map((feature, index) => (
          <div key={index} style={{ 
            padding: "10px",
            border: "1px solid #ddd",
            borderRadius: "5px",
            backgroundColor: "#f9f9f9"
          }}>
            <label style={{ display: "block", marginBottom: "5px", fontWeight: "bold", fontSize: "12px" }}>
              Feature {index + 1}
            </label>
            <input
              type="number"
              step="0.01"
              value={feature.toFixed(4)}
              onChange={(e) => handleInputChange(index, e.target.value)}
              style={{
                width: "100%",
                padding: "8px",
                border: "1px solid #ccc",
                borderRadius: "4px",
                boxSizing: "border-box"
              }}
            />
          </div>
        ))}
      </div>
      
      <button 
        onClick={handlePredict}
        style={{
          width: "100%",
          padding: "12px",
          backgroundColor: "#4CAF50",
          color: "white",
          border: "none",
          borderRadius: "4px",
          fontSize: "16px",
          fontWeight: "bold",
          cursor: "pointer",
          marginBottom: "20px"
        }}
        onMouseOver={(e) => e.target.style.backgroundColor = "#45a049"}
        onMouseOut={(e) => e.target.style.backgroundColor = "#4CAF50"}
      >
        🔍 Predict
      </button>

      {error && (
        <div style={{
          padding: "15px",
          backgroundColor: "#f8d7da",
          color: "#721c24",
          border: "1px solid #f5c6cb",
          borderRadius: "4px",
          marginBottom: "20px"
        }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {prediction !== null && (
        <div style={{
          padding: "20px",
          backgroundColor: "#d4edda",
          border: "1px solid #c3e6cb",
          borderRadius: "4px",
          color: "#155724"
        }}>
          <h3>✅ Prediction Result</h3>
          <p style={{ fontSize: "18px", fontWeight: "bold" }}>
            {prediction === 1 ? "🚨 FRAUDULENT" : "✅ LEGITIMATE"}
          </p>
          
          {probability && (
            <div>
              <h4>Confidence Scores:</h4>
              <ul style={{ margin: "10px 0", paddingLeft: "20px" }}>
                <li>Legitimate: {(probability[0] * 100).toFixed(2)}%</li>
                <li>Fraudulent: {(probability[1] * 100).toFixed(2)}%</li>
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default PredictForm;
