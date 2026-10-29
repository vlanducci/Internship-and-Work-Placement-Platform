"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("Connecting to backend...");

  useEffect(() => {
    fetch("/api/test")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Backend request failed");
        }
        return response.json();
      })
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("Could not connect to FastAPI"));
  }, []);

  return (
    <main className="flex min-h-screen items-center justify-center p-8">
      <div className="text-center">
        <h1 className="text-3xl font-bold">
          Internship Platform
        </h1>
        <p className="mt-4">{message}</p>
      </div>
    </main>
  );
}