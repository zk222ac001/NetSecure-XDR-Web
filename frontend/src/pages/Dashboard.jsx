import { Line } from "react-chartjs-2";

function Dashboard() {

    const data = {

        labels: ["Mon", "Tue", "Wed", "Thu"],

        datasets: [

            {

                label: "Traffic",

                data: [12, 19, 7, 25],

                borderColor: "#00ff99"
            }
        ]
    };

    return (

        <div className="container">

            <h1>NetSecure XDR</h1>

            <Line data={data} />

        </div>
    );
}

export default Dashboard;