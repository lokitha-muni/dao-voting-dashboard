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

## Data fetched by Aptos:
![Screenshot 2025-04-13 164757](https://github.com/user-attachments/assets/084238c7-2ab1-4ed2-aaff-ed8173ff2031)
![Screenshot 2025-04-13 164811](https://github.com/user-attachments/assets/19ea082d-1e0a-4901-af77-71ecdc6f5b81)

## When you give your own csv file:
![Screenshot 2025-04-13 165023](https://github.com/user-attachments/assets/f1f397e9-9719-44bb-bbeb-969c46455be1)
![Screenshot 2025-04-13 165014](https://github.com/user-attachments/assets/23b56f3a-9b20-404e-a4fb-d2ac3c5b9798)
![Screenshot 2025-04-13 164958](https://github.com/user-attachments/assets/741aa108-3486-4f7e-8630-7771131640fa)



### Landing Website (Local)
![Screenshot 2025-04-13 165526](https://github.com/user-attachments/assets/46498bf4-8463-49d7-915e-260bfa440d7e)
![Screenshot 2025-04-13 165614](https://github.com/user-attachments/assets/df854bcf-e219-4122-8ecc-e016e1553ade)
![Screenshot 2025-04-13 165557](https://github.com/user-attachments/assets/32f6e3ee-8f95-43e7-8dc1-3c6087160ca8)
![Screenshot 2025-04-13 165541](https://github.com/user-attachments/assets/e24cf98e-dfb2-4d08-809a-461911958cbc)

---

## 🧪 Run Dashboard Locally

```bash
git clone https://github.com/lokitha-muni/dao-voting-dashboard.git
cd dao-voting-dashboard
pip install -r requirements.txt
python app2.py
