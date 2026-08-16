<h1 align="center">🧠 LifeOS</h1>

<p align="center"> <strong>AI Behavioral Operating System</strong><br> Tynovate AI Internship Program 2026 </p>

<p align="center">


</p>

📌 Project Overview

LifeOS is an AI-powered Behavioral Operating System developed during the Tynovate AI Internship Program 2026.

The system collects behavioral data from multiple sources, processes and analyzes activity patterns, applies Machine Learning models for behavioral prediction, and generates insights and adaptive interventions to support productivity and goal alignment.

The project was developed using modular programming, clean architecture, RESTful API design, Machine Learning, interactive visualization, automated testing, and containerized deployment.

🚀 Weekly Progress
```md
Week	Theme	Status
Week 1	Foundations & Environment Setup	✅
Week 2	Behavioral Data Ingestion & Preprocessing	✅
Week 3	Behavioral Engine & Life Graph	✅
Week 4	Prediction Engine & Causal Discovery	✅
Week 5	Real-Time Intervention System	✅
Week 6	Discipline Score & Backend API	✅
Week 7	Dashboard, Goal Alignment & Simulation	✅
Week 8	LLM Coach, Deployment & Showcase	✅

Internship project status: 100% complete ✅
```

📂 Project Structure
```text
LifeOS/
│
├── data/
├── docs/
├── images/
├── models/
├── output/
│
├── src/
│   ├── api/
│   │   ├── app.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── database.py
│   │
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── layout.py
│   │   ├── metrics.py
│   │   ├── charts.py
│   │   ├── goal_alignment.py
│   │   ├── simulation.py
│   │   ├── feedback.py
│   │   └── utils.py
│   │
│   ├── parser.py
│   ├── validation.py
│   ├── feature_engineering.py
│   ├── database.py
│   ├── entropy.py
│   ├── context_switch.py
│   ├── sequence_mining.py
│   ├── life_graph.py
│   ├── behavioral_engine.py
│   ├── report_generator.py
│   ├── data_preparation.py
│   ├── xgboost_model.py
│   ├── hmm_model.py
│   ├── granger_causality.py
│   ├── prediction_comparison.py
│   ├── notification.py
│   ├── triggers.py
│   ├── contextual_bandit.py
│   ├── feedback.py
│   ├── intervention_engine.py
│   ├── discipline_score.py
│   ├── behavioral_debt.py
│   └── main.py
│
├── tests/
│   ├── test_discipline_score.py
│   ├── test_behavioral_debt.py
│   ├── test_integration.py
│   └── load_test.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```
⚙️ Technology Stack
```md
Technology	Purpose
Python	Core Development
Pandas	Data Processing
SQLite	Database
NLTK	Natural Language Processing
NetworkX	Life Graph
Matplotlib	Visualization
Scikit-learn	Machine Learning
XGBoost	Behavioral Prediction
hmmlearn	Hidden Markov Model
statsmodels	Granger Causality
plyer	Desktop Notifications
python-telegram-bot	Telegram Alerts
FastAPI	REST API
Pydantic	Data Validation
pytest	Testing
Streamlit	Interactive Dashboard
Plotly	Interactive Visualization
Anthropic API	LLM Coach
Docker	Containerization
Docker Compose	Multi-service Deployment
GitHub Actions	CI/CD Automation
GitHub	Version Control & Hosting
```
🛠️ Installation
1. Clone Repository
git clone https://github.com/YasmeenGull/LifeOS.git
cd LifeOS
2. Install Requirements
pip install -r requirements.txt
3. Run LifeOS
python src/main.py
🌐 API

Start the FastAPI server:

uvicorn src.api.app:app --reload

Open Swagger documentation:

http://127.0.0.1:8000/docs
Main API Endpoints
GET  /
GET  /health
POST /log
GET  /logs
GET  /score
GET  /debt
POST /goals
GET  /goals
📊 Dashboard

Run the Streamlit dashboard:

streamlit run src/dashboard/app.py

🐳 Docker Deployment

Build the Docker images:

docker compose build

Start the services:

docker compose up -d

Check running containers:

docker compose ps
API
http://localhost:8000

Swagger:

http://localhost:8000/docs
Dashboard
http://localhost:8501

Stop the services:

docker compose down
🔄 CI/CD

GitHub Actions is used to automate project workflows and support continuous integration.

The project repository:

https://github.com/YasmeenGull/LifeOS
🧠 Week 8 — LLM Coach & Deployment

The final internship phase focused on transforming LifeOS into a deployable and user-facing system.

📈 Roadmap
```md
✅ Week 1 — Foundations
✅ Week 2 — Data Ingestion
✅ Week 3 — Behavioral Engine
✅ Week 4 — Prediction & Causal Discovery
✅ Week 5 — Intervention System
✅ Week 6 — Backend API
✅ Week 7 — Dashboard & Simulation
✅ Week 8 — LLM Coach & Deployment
🎯 Final Status: Completed
```
💡 Software Engineering Principles
Clean Architecture
Modular Programming
Separation of Concerns
Single Responsibility Principle
Reusable Components
Machine Learning Integration
RESTful API Design
Interactive Dashboard Design
Automated Testing
CI/CD
Containerization
Maintainable Code
Scalable Design
👩‍💻 Developer

Yasmeen Gull
BS Computer Science
Tynovate AI Internship Program — 2026

<p align="center">

⭐ If you found this project useful, please consider giving it a Star!

</p>