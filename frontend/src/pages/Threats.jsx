import { useEffect, useState } from "react";

export default function Threats() {
    const [threats, setThreats] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/threats")
            .then(res => res.json())
            .then(setThreats);
    }, []);

    return (
        <div>
            <h1>Threat Intel</h1>

            {threats.map((t, i) => (
                <div key={i}>
                    {t.name} - {t.level}
                </div>
            ))}
        </div>
    );
}