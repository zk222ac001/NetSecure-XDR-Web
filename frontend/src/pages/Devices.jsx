import { useEffect, useState } from "react";

export default function Devices() {
    const [devices, setDevices] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/devices")
            .then(res => res.json())
            .then(setDevices);
    }, []);

    return (
        <div>
            <h1>Devices</h1>

            {devices.map(d => (
                <div key={d.id}>
                    {d.ip} - {d.status}
                </div>
            ))}
        </div>
    );
}