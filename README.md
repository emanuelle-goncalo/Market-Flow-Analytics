## Market-Flow Analytics: Crypto Data Pipeline

#### Professional Profile & Project Intent
As a developer focused on automation and high-performance data engineering, I have a strong interest in the Cryptocurrency market. Driven by this interest, I built this specialized data pipeline to analyze the historical performance of assets over the **last 5 years** (including BTC, ETH, and ADA). 

The goal of this project is to transform raw market data into clear, actionable visual intelligence using modern software architecture.

#### Performance with Polars
One of the core strengths of this project is the use of the **Polars** library. 
* **Why Polars?** Unlike traditional Pandas, Polars is built in Rust and designed for parallel execution (multithreading). 
* **The Result:** While standard tools might struggle with large datasets, this pipeline processes 5 years of data in **just a few seconds**, ensuring maximum efficiency and low memory usage.



#### Mathematical Rule: Normalization (Base 100)
To compare assets with completely different price points Bitcoin at $60k vs. Cardano at $0.50, I implemented Base 100 Normalization.

The Logic:
1. We set the first price in the history (5 years ago) as the value 100.
2. Every subsequent price is calculated proportionally using this formula:  
   $$V_{normalized} = \left( \frac{Current Price}{Initial Price} \right) \times 100$$

**Why it matters:** Without normalization, high-priced assets would dominate the chart, making smaller assets look like flat lines. With Base 100, we focus on **percentage growth**, allowing us to see exactly which asset provided the best return on investment regardless of its nominal price.



#### Why this Dashboard is Secure
This custom-built tool is more reliable and secure than generic web dashboards for three reasons:

1. Direct Source Data: Data is fetched directly from financial APIs (Yahoo Finance), eliminating middleman manipulation.
2. Auditable Code: Since it is open-source, the logic is transparent. There are no "black-box" algorithms or hidden fees.
3. Privacy: The processing happens locally on your machine. Your search interests and financial data are not shared with third-party marketing platforms.

---

#### Project Structure
```text
Market-Flow-Analytics/
├── src/
│   ├── main.py          # Orchestration and execution
│   └── utils.py         # Core logic and processing functions
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
