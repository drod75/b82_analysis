# B82 Bus Analysis

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/drod75)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/david-rodriguez-nyc)

## Table of Contents
- [B82 Bus Analysis](#b82-bus-analysis)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Analysis Methods](#analysis-methods)
  - [Findings](#findings)
  - [Proposed Improvements](#proposed-improvements)
  - [Technical Details](#technical-details)
    - [Running Locally](#running-locally)
      - [Method 1: Using uv (Preferred)](#method-1-using-uv-preferred)
      - [Method 2: Using pip](#method-2-using-pip)
    - [Libraries Used](#libraries-used)
    - [Datasets Used](#datasets-used)
    - [License](#license)

## Introduction
The B82 Bus, a bus I rather frequently use, either to transfer to the F train, or to head to tranfer to the B44/B44-SBS in order to get to Brooklyn College. 

![Image of B82 route to Brooklyn College]()

The B82 has always one flaw however, depending on the time of day, there may be traffic which causes delays, or a load of passengers which makes the bus crowded. This problem is especially shown during the late afternoon, which I can one time where the bus took forever, although I eventually returned home the trip felt very long, longer than it probably was. 

![Image of B82 route during late affernoon]()

This project aims to analyze the B82 and B82-SBS bus line, and figure out what areas could use improvment. Several aspects aimed to be analyzed, including the average time it takes to get between each stop, the traffic in each street it passes by, and the amount of passengers that get on and off the bus at each stop.

## Analysis Methods
*Placeholder: Details on data collection, processing, and analysis techniques will be added here.*

<p align="right"><a href="#readme-top">Back to top</a></p>

## Findings
*Placeholder: Key findings and visualizations from the analysis will be added here.*

<p align="right"><a href="#readme-top">Back to top</a></p>

## Proposed Improvements
*Placeholder: Recommendations for improving the B82 bus line based on the analysis will be added here.*

<p align="right"><a href="#readme-top">Back to top</a></p>

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

### Libraries Used
tbd...

### Datasets Used
- [MTA Bus Hourly Ridership](https://data.ny.gov/Transportation/MTA-Bus-Hourly-Ridership-Beginning-2025/gxb3-akrn/about_data)
- [MTA Bus Stops](https://data.ny.gov/Transportation/MTA-Bus-Stops/2ucp-7wg5/about_data)
- [MTA Bus Stop-Level Ridership](https://data.ny.gov/Transportation/MTA-Bus-Stop-Level-Ridership-Beginning-2024/fvdm-uavx/about_data)
- [2020 Neighborhood Tabulation Areas (NTAs)](https://data.cityofnewyork.us/City-Government/2020-Neighborhood-Tabulation-Areas-NTAs-/9nt8-h7nd/about_data)
- [MTA Bus Routes](https://data.ny.gov/Transportation/MTA-Bus-Routes/bzwk-3hb4/about_data)

### License
This project is licensed under the [Apache License 2.0](LICENSE) - see the LICENSE file for details.

<p align="right"><a href="#readme-top">Back to top</a></p>