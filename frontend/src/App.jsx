import { useEffect, useState } from "react";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from "recharts";

import "./App.css";


function App() {

  const [revenue, setRevenue] = useState(null);
  const [region, setRegion] = useState(null);
  const [forecast, setForecast] = useState(null);
  const [risk, setRisk] = useState(null);
  const [revenueHistory, setRevenueHistory] = useState([]);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");


  useEffect(() => {
    loadDashboard();
  }, []);


  async function loadDashboard() {

    try {

      // Revenue
      const revenueResponse = await fetch(
        "http://127.0.0.1:5000/api/revenue"
      );

      const revenueData = await revenueResponse.json();

      setRevenue(revenueData);


      // Best region
      const regionResponse = await fetch(
        "http://127.0.0.1:5000/api/region"
      );

      const regionData = await regionResponse.json();

      setRegion(regionData);


      // Forecast
      const forecastResponse = await fetch(
        "http://127.0.0.1:5000/api/forecast"
      );

      const forecastData = await forecastResponse.json();

      setForecast(forecastData);


      // Customer risk
      const riskResponse = await fetch(
        "http://127.0.0.1:5000/api/risk"
      );

      const riskData = await riskResponse.json();

      setRisk(riskData);


      // Revenue history
      const historyResponse = await fetch(
        "http://127.0.0.1:5000/api/revenue-history"
      );

      const historyData = await historyResponse.json();


      const chartData = historyData.months.map(
        (month, index) => ({
          month: month,
          revenue: historyData.revenue[index]
        })
      );


      setRevenueHistory(chartData);


    } catch (error) {

      console.error(
        "Error loading dashboard:",
        error
      );

    }
  }


  async function askAgent() {

    if (!question.trim()) {

      setAnswer(
        "Please enter a question."
      );

      return;
    }


    setAnswer("Thinking...");


    try {

      const response = await fetch(
        "http://127.0.0.1:5000/api/ask",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            question: question
          })
        }
      );


      const data = await response.json();


      if (data.answer) {

        setAnswer(data.answer);

      } else {

        setAnswer(
          "Unable to get a response from RevOpsAI."
        );

      }


    } catch (error) {

      setAnswer(
        "Unable to connect to RevOpsAI backend."
      );

      console.error(error);

    }
  }


  return (

    <div className="dashboard">


      {/* Header */}

      <header>

        <h1>
          RevOpsAI
        </h1>

        <p>
          Revenue Intelligence & AI-Powered Business Insights
        </p>

      </header>



      {/* Dashboard Cards */}

      <div className="cards">


        {/* Total Revenue */}

        <div className="card">

          <h3>
            Total Revenue
          </h3>

          <h2>

            {revenue

              ? `₹${revenue.total_revenue.toLocaleString()}`

              : "Loading..."}

          </h2>

        </div>



        {/* Best Region */}

        <div className="card">

          <h3>
            Best Region
          </h3>

          <h2>

            {region

              ? region.best_region

              : "Loading..."}

          </h2>


          {region && (

            <p>
              ₹{region.revenue.toLocaleString()}
            </p>

          )}

        </div>



        {/* Revenue Forecast */}

        <div className="card">

          <h3>
            Revenue Forecast
          </h3>

          <h2>

            {forecast

              ? `₹${Math.round(
                forecast.predicted_revenue
              ).toLocaleString()}`

              : "Loading..."}

          </h2>

        </div>



        {/* Expected Growth */}

        <div className="card">

          <h3>
            Expected Growth
          </h3>

          <h2>

            {forecast

              ? `${forecast.expected_growth.toFixed(2)}%`

              : "Loading..."}

          </h2>

        </div>


      </div>



      {/* Revenue Trend */}

      <div className="section">

        <h2>
          Revenue Trend
        </h2>


        <ResponsiveContainer
          width="100%"
          height={300}
        >

          <LineChart
            data={revenueHistory}
          >

            <CartesianGrid
              strokeDasharray="3 3"
            />


            <XAxis
              dataKey="month"
            />


            <YAxis
              tickFormatter={(value) =>
                `₹${(
                  value / 100000
                ).toFixed(1)}L`
              }
            />


            <Tooltip
              formatter={(value) =>
                `₹${Number(
                  value
                ).toLocaleString()}`
              }
            />


            <Line
              type="monotone"
              dataKey="revenue"
              stroke="#2563eb"
              strokeWidth={3}
              dot={{ r: 4 }}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>



      {/* Customer Risk */}

      <div className="section">

        <h2>
          Customer Risk
        </h2>


        {risk ? (

          <>

            <p>

              <strong>
                High-risk customers:
              </strong>{" "}

              {risk.customer_ids}

            </p>


            <p>

              <strong>
                Revenue at risk:
              </strong>{" "}

              ₹{risk.revenue_at_risk.toLocaleString()}

            </p>


            <p>

              <strong>
                Priority customer:
              </strong>{" "}

              {risk.priority_customer}

              {" — ₹"}

              {risk.priority_customer_revenue.toLocaleString()}

            </p>

          </>

        ) : (

          <p>
            Loading risk information...
          </p>

        )}

      </div>



      {/* AI Agent */}

      <div className="section">

        <h2>
          Ask RevOpsAI
        </h2>


        <div className="ask-box">


          <input
            type="text"
            value={question}

            onChange={(e) =>
              setQuestion(e.target.value)
            }

            onKeyDown={(e) => {

              if (e.key === "Enter") {

                askAgent();

              }

            }}

            placeholder="Example: Which customers might churn?"
          />


          <button
            onClick={askAgent}
          >
            Ask
          </button>


        </div>


        <div className="answer">

          {answer ||

            "Ask a question to get a business insight."}

        </div>


      </div>


    </div>

  );
}


export default App;