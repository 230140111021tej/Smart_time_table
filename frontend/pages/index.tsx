import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [demo, setDemo] = useState<any[]>([]);

  useEffect(() => {
    async function loadDemo() {
      try {
        const resp = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/schedule/demo`);
        setDemo(resp.data);
      } catch (err) {
        console.error("Failed to fetch demo timetable", err);
      }
    }
    loadDemo();
  }, []);

  return (
    <main style={{ padding: 24, fontFamily: "Inter, sans-serif" }}>
      <h1>Smart Timetabling — Demo</h1>
      <p>Simple demo timetable from backend:</p>
      <pre style={{ background: "#f5f5f5", padding: 12 }}>{JSON.stringify(demo, null, 2)}</pre>
      <p>Next steps: implement dashboard, calendar view, drag/drop editor, and scheduler config UI.</p>
    </main>
  );
}
