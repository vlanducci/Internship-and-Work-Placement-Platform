// page.tsx
// Defines the main homepage of the Internship Platform frontend.
// Sends a request to the FastAPI backend and displays the connection status.

"use client";

import { useEffect, useState } from "react";

export default function Home() {
  // Stores the message displayed to the user while checking the backend connection.
  const [message, setMessage] = useState("Connecting to backend...");

  // Runs once when the homepage loads to test communication with FastAPI.
  useEffect(() => {
    // Sends a GET request through the Next.js API rewrite to the backend.
    fetch("/api/test")
      .then((response) => {
        // Throws an error if the backend returns an unsuccessful HTTP status.
        if (!response.ok) {
          throw new Error("Backend request failed");
        }
        // Converts the successful response body into a JavaScript object.
        return response.json();
      })
      // Displays the message returned by the FastAPI endpoint.
      .then((data) => setMessage(data.message))
      // Displays an error message if the request fails.
      .catch(() => setMessage("Could not connect to FastAPI"));
  }, []);

  // Renders the homepage and the current backend connection status.
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