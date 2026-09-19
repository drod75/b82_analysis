# B82 Bus Analysis

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/drod75)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/david-rodriguez-nyc)

## Table of Contents
- [Introduction](#introduction)
- [Analysis Methods](#analysis-methods)
- [Findings](#findings)
- [Proposed Improvements](#proposed-improvements)
- [Technical Details](#technical-details)
  - [Running Locally](#running-locally)
    - [Method 1: Using uv (Preferred)](#method-1-using-uv-preferred)
    - [Method 2: Using pip](#method-2-using-pip)
- [License](#license)

## Introduction
The B82 Bus Analysis project aims to evaluate the performance of the B82 bus line and identify potential areas for improvement. This repository serves both as the source code for the analysis and the foundation for the project's GitHub Pages site.

## Analysis Methods
*Placeholder: Details on data collection, processing, and analysis techniques will be added here.*

## Findings
*Placeholder: Key findings and visualizations from the analysis will be added here.*

## Proposed Improvements
*Placeholder: Recommendations for improving the B82 bus line based on the analysis will be added here.*

## Technical Details

### Running Locally
To run this project locally, first clone the repository and navigate to the directory:

```bash
git clone <repository-url>
cd b82_analysis
```

#### Method 1: Using uv (Preferred)
[uv](https://github.com/astral-sh/uv) is an extremely fast Python package installer and resolver.

1. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   # source .venv/bin/activate
   
   uv pip install -r requirements.txt
   ```

#### Method 2: Using pip
1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   # source .venv/bin/activate
   
   pip install -r requirements.txt
   ```

## License
This project is licensed under the [Apache License 2.0](LICENSE) - see the LICENSE file for details.
