# ⛓️ ChainWatch — Flight Data Recorder for Multi-Step AI Systems

[![Python](https://img.shields.io/badge/Language-Python%203.10%2B-blue?style=flat-square&logo=python)](https://python.org)
[![Architecture](https://img.shields.io/badge/Security-Cryptographic%20Hash%20Chains-black?style=flat-square)](chainwatch/)
[![CLI](https://img.shields.io/badge/Tool-CLI%20Flight%20Recorder-purple?style=flat-square)](chainwatch/cli.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

**ChainWatch** is a flight data recorder for multi-step autonomous AI agent systems. It deterministically records every step in an agent's decision chain, links states cryptographically with SHA-256 hashes, prevents log tampering, and allows developers to verify execution integrity and replay the complete decision flow.

---

## 🌟 Key Features

* **Cryptographic Hash Chaining:** Every step references the hash of the preceding decision state—forming a verifiable, tamper-evident audit ledger.
* **Flight Data Recording:** Logs inputs, LLM thought chains, tool invocations, parameters, and return payloads into structured `.jsonl` chain files.
* **Integrity Verifier:** Inspects logged decision chains and flags modified steps, truncated traces, or broken hashes.
* **Deterministic Decision Replay:** Step-by-step playback utility to reproduce failure states, debug regressions, and examine agent reasoning.
* **Audit & Compliance Reports:** Exports clean audit summaries for AI safety and compliance reviews.

---

## 📁 Repository Structure

```
ChainWatch/
├── chainwatch/
│   ├── cli.py          # Command line interface commands
│   ├── hashing.py      # Cryptographic hashing & tamper-prevention algorithms
│   ├── models.py       # Pydantic / dataclass schemas for decision nodes
│   ├── recorder.py     # Non-blocking flight data recording hooks
│   ├── replay.py       # Decision chain step-by-step replayer
│   ├── verifier.py     # Hash integrity validation engine
│   └── report.py       # Formatted audit reports generator
├── chains/             # Example recorded decision chain logs (.jsonl)
├── pyproject.toml      # Package configuration & dependencies
└── README.md           # Documentation
```

---

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/Tarunjit45/ChainWatch.git
cd ChainWatch
pip install -e .
```

### 2. CLI Usage

```bash
# Verify integrity of a recorded decision chain
chainwatch verify chains/chain_001.jsonl

# Replay an agent's multi-step decision trajectory
chainwatch replay chains/chain_001.jsonl

# Generate an executive audit report
chainwatch report chains/chain_001.jsonl
```

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
