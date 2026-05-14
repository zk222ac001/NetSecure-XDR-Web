import { Link } from "react-router-dom";

export default function Sidebar() {
    return (
        <div className="sidebar">
            <h2>XDR</h2>

            <Link to="/">Dashboard</Link>
            <Link to="/alerts">Alerts</Link>
            <Link to="/devices">Devices</Link>
            <Link to="/threats">Threats</Link>
        </div>
    );
}