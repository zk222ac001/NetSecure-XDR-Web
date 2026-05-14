import { useEffect, useState } from "react";

function LiveAlerts() {

    const [alerts, setAlerts] = useState([]);

    useEffect(() => {

        const socket = new WebSocket(

            "ws://localhost:8000/ws"
        );

        socket.onmessage = (event) => {

            setAlerts(prev => [

                ...prev,
                event.data
            ]);
        };

    }, []);

    return (

        <div>

            <h2>Live Alerts</h2>

            {alerts.map((alert, index) => (

                <div key={index}>

                    {alert}

                </div>

            ))}

        </div>
    );
}

export default LiveAlerts;