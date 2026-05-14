import { BrowserRouter, Routes, Route } from "react-router-dom";

import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import Alerts from "./pages/Alerts";
import Devices from "./pages/Devices";
import Threats from "./pages/Threats";

export default function App() {
    return (
        <BrowserRouter>
            <div className="layout">
                <Sidebar />
                <div className="content">
                    <Routes>
                        <Route path="/" element={<Dashboard />} />
                        <Route path="/alerts" element={<Alerts />} />
                        <Route path="/devices" element={<Devices />} />
                        <Route path="/threats" element={<Threats />} />
                    </Routes>
                </div>
            </div>
        </BrowserRouter>
    );
}