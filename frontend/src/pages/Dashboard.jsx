import { useEffect, useState } from "react";
import StatCard from "../components/StatCard";

export default function Dashboard() {
    const [data, setData] = useState({});

    useEffect(() => {
        fetch("http://127.0.0.1:8000/stats")
            .then(res => res.json())
            .then(setData);
    }, []);

    return (
        <div>
            <h1>Dashboard</h1>

            <div className="grid">
                <StatCard title="Alerts" value={data.alerts} />
                <StatCard title="Devices" value={data.devices} />
                <StatCard title="Threats" value={data.threats} />
                <StatCard title="Vulnerabilities" value={data.vulnerabilities} />
            </div>
        </div>
    );
}