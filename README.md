# DAO Voting Pattern Analyzer 🗳️

This project analyzes DAO voting trends across the Aptos blockchain. It includes a visually rich **dashboard built with Dash** and a **landing website built by teammates** that introduces the project and routes users to the dashboard.

## 🔗 Live Link

- 📊 **Dashboard:** [Explore the Full Dashboard]([https://your-deployment-url.onrender.com](https://dao-voting-dashboard-azwk.onrender.com/))

---

## 🧩 Project Structure

### 🖥️ Landing Website (Local Project by Teammates)
A static frontend website created using HTML, CSS, and JavaScript. Though not deployed, this website serves as a visual overview of the project with:
- 📝 About section
- ✨ Feature highlights like:
  - Proposal Calendar
  - Blockchain Integration
  - Global Impact
- 🚀 Button to open the full dashboard (when hosted locally)

This site was created as part of the project to improve user experience and guide users into the analytical dashboard.

---

### 📊 DAO Voting Dashboard (Dash App)
A Python Dash-based dashboard that fetches and visualizes DAO data from the Aptos blockchain. It includes:

- DAO-specific proposal history
- Voter participation analytics
- Visualizations (bar graphs, pie charts) for trend analysis
- Dashboard navigation through dropdowns and filters

---

## 🔍 Features Summary

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 📅 Proposal Calendar   | View upcoming and past proposal data                                        |
| 🔐 Blockchain Insights | Uses Aptos API for transparency in DAO governance                           |
| 🌍 Global Impact       | Understand how DAOs influence decentralized decisions                       |
| 📊 Visual Analytics    | Clean charts and graphs built using Plotly Dash                             |

---

## 🛠 Tech Stack

- **Landing Website**: HTML, CSS, JavaScript (local only)
- **Dashboard**: Python, Dash, Plotly
- **Blockchain**: Aptos API
- **Deployment**: Render
- **Version Control**: Git & GitHub

---

## 🧠 How It Works

- Connects to Aptos API to fetch DAO-related proposal and voting data
- Visualizes data with graphs and filters in the dashboard
- (Locally) integrates with a landing page that provides an overview

---
## 🖼️ Screenshots

### Dashboard View
![Screenshot 2025-04-13 060816](https://github.com/user-attachments/assets/a7cb4177-88be-464f-9ac6-1464b1be00cb)
![Screenshot 2025-04-13 060902](https://github.com/user-attachments/assets/c71751e8-fdd9-445b-bb9b-b5348817cffb)
![Screenshot 2025-04-13 060839](https://github.com/user-attachments/assets/aba11ac5-e1ab-478a-91ac-4b2d9418e483)


### Landing Website (Local)
![Screenshot 2025-04-13 062037](https://github.com/user-attachments/assets/100190bb-5d7b-43a0-b74e-04ff2b51d717)
![Screenshot 2025-04-13 062010](https://github.com/user-attachments/assets/67b91f29-656d-4f09-8e85-e544f4abc4e9)
![Screenshot 2025-04-13 061956](https://github.com/user-attachments/assets/9d457ff4-4060-43ee-9aa8-5e54bdd132a2)
![Screenshot 2025-04-13 061941](https://github.com/user-attachments/assets/84500a3a-d3e5-4ce5-93df-808d59b5504c)


---

## 🧪 Run Dashboard Locally

```bash
git clone https://github.com/lokitha-muni/dao-voting-dashboard.git
cd dao-voting-dashboard
pip install -r requirements.txt
python app2.py
