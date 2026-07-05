import { useState, useEffect } from "react";
import api from "./api/axios";

function App() {
  const [status, setStatus] = useState("Checking backend...");

  useEffect(() => {
    api.get("/health")
      .then((res) => {
        setStatus(res.data.message);
      })
      .catch(() => {
        setStatus("Backend not reachable");
      });
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-900 text-white">
      <h1 className="text-2xl font-bold">GhostWriter Detector</h1>
      <p className="ml-4 text-green-400">{status}</p>
    </div>
  );
}

export default App;