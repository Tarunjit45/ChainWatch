# 🚀 ChainWatch

![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Production-Active-success?style=for-the-badge)

## 📌 Overview

ChainWatch is a flight data recorder for multi-step AI systems. It's a CLI-based tool that records every step in an AI decision chain, links them together in order, prevents tampering, and allows you to verify the chain's integrity and replay the full decision flow.

## ✨ Key Features & Architecture

- **High-Performance Codebase:** Built using `Python` and modern engineering principles.
- **Modular & Scalable Design:** Structured directory tree for seamless development and deployment.

## 🛠️ Tech Stack & Dependencies

- **Core Language:** `Python`
- **Libraries & Tools:** Python
- **Deployment Infrastructure:** Vercel Edge / Cloud Services

## 📁 Architecture & File Layout

```text
ChainWatch/
├── .github
├── .github/ISSUE_TEMPLATE
├── .github/ISSUE_TEMPLATE/bug_report.md
├── .github/ISSUE_TEMPLATE/feature_request.md
├── .github/PULL_REQUEST_TEMPLATE.md
├── .github/workflows
├── .github/workflows/ci.yml
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── chains
├── chains/chain_001.jsonl
├── chains/chain_002.jsonl
├── chainwatch
└── ... [additional codebase files]
```

## 🚀 Quickstart & Installation

### Prerequisites
- Python 3.9+
- pip package manager

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tarunjit45/ChainWatch.git
   cd ChainWatch
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute application:**
   ```bash
   python main.py
   ```

## 📜 Author & License

Architected & Developed by **[Tarunjit Biswas](https://github.com/Tarunjit45)**.  
Distributed under the **MIT License**.
