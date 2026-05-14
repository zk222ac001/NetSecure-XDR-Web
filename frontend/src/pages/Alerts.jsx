import { useEffect, useState } from "react";

export default function Alerts() {
    const [alerts, setAlerts] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/alerts")
            .then(res => res.json())
            .then(setAlerts);
    }, []);

    return (
        <div>
            <h1>Alerts</h1>

            {alerts.map(a => (
                <div key={a.id}>
                    {a.msg} - {a.severity}
                </div>
            ))}
        </div>
    );
}