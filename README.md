# B82 Bus Analysis

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/drod75)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/david-rodriguez-nyc)

## Table of Contents
- [B82 Bus Analysis](#b82-bus-analysis)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Preplanning](#preplanning)
  - [Analysis](#analysis)
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

## Preplanning
Before we first get started on analyzing the data, finding trends, and joining any data, first we need to plan out what it is we want to analyze, our main goals are to:
- Highlight ridership patterns
- Highlight trave patterns
- Highlight neighborhood details
  
To do this we have several datasets that we will be using, most of which are from the MTA, these datasets include:

- 2020 Neighborhood Tabulation Areas
- MTA Bus Routes
- MTA Bus Stops
- MTA Bus Stop-Level Ridership
- MTA Bus Hourly Ridership
- MTA Bus Route Segment Speeds

Our first goal will be to showcase the different areas the individual stops are located in, this way when we compare ridership, transfers, and trips, we can highlight different travel patterns between neighborhoods, and also notice what neighborhoods contain more riders.

## Analysis
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
   
   uv sync
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

| Library | Purpose |
|---------|---------|
| ![pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat-square&logo=pandas&logoColor=white) | Data manipulation and analysis of ridership and route data |
| ![seaborn](https://img.shields.io/badge/seaborn-%23419082.svg?style=flat-square) | Statistical data visualization to uncover trends and patterns |
| ![scipy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=flat-square&logo=scipy&logoColor=white) | Scientific computing for advanced data processing |
| ![requests](https://img.shields.io/badge/requests-%23000000.svg?style=flat-square) | HTTP library for fetching data from external APIs |
| ![python-dotenv](https://img.shields.io/badge/python--dotenv-%23F7DF1E.svg?style=flat-square) | Loading environment variables and configuration |
| ![ipykernel](https://img.shields.io/badge/ipykernel-%23F37626.svg?style=flat-square&logo=jupyter&logoColor=white) | IPython kernel for interactive Jupyter notebook development |
| ![geopandas](https://img.shields.io/badge/geopandas-139C5A?style=flat-square) | Geospatial data manipulation and analysis |
| ![folium](https://img.shields.io/badge/folium-77B829?style=flat-square) | Interactive leaflet maps for geographic data visualization |

### Datasets Used

| Dataset | Source | Description |
|---------|--------|-------------|
| **[2020 Neighborhood Tabulation Areas](https://data.cityofnewyork.us/City-Government/2020-Neighborhood-Tabulation-Areas-NTAs-/9nt8-h7nd/about_data)** | ![NYC Open Data](https://img.shields.io/badge/NYC_Open_Data-black?style=flat-square) | Provides boundaries for NYC's Neighborhood Tabulation Areas to contextualize route demographics. |
| **[MTA Bus Routes](https://data.ny.gov/Transportation/MTA-Bus-Routes/bzwk-3hb4/about_data)** | ![Data.NY.gov](https://img.shields.io/badge/Data.NY.gov-1f54a0?style=flat-square) | Provides geographic alignments and details for MTA bus routes to plot the full paths. |
| **[MTA Bus Stops](https://data.ny.gov/Transportation/MTA-Bus-Stops/2ucp-7wg5/about_data)** | ![Data.NY.gov](https://img.shields.io/badge/Data.NY.gov-1f54a0?style=flat-square) | Contains geographic locations and other details of all MTA bus stops to map the B82 route. |
| **[MTA Bus Stop-Level Ridership](https://data.ny.gov/Transportation/MTA-Bus-Stop-Level-Ridership-Beginning-2024/fvdm-uavx/about_data)** | ![Data.NY.gov](https://img.shields.io/badge/Data.NY.gov-1f54a0?style=flat-square) | Details ridership at the individual stop level, highlighting the most heavily utilized stops on the route. |
| **[MTA Bus Hourly Ridership](https://data.ny.gov/Transportation/MTA-Bus-Hourly-Ridership-Beginning-2025/gxb3-akrn/about_data)** | ![Data.NY.gov](https://img.shields.io/badge/Data.NY.gov-1f54a0?style=flat-square) | Provides hourly ridership estimates for MTA bus routes, enabling time-of-day volume analysis. |
| **[MTA Bus Route Segment Speeds](https://data.ny.gov/Transportation/MTA-Bus-Route-Segment-Speeds-Beginning-2025/kufs-yh3x/about_data)** | ![Data.NY.gov](https://img.shields.io/badge/Data.NY.gov-1f54a0?style=flat-square) | Provides bus speed data along different route segments to analyze traffic and delays. |

### License
This project is licensed under the [Apache License 2.0](LICENSE) - see the LICENSE file for details.

<p align="right"><a href="#readme-top">Back to top</a></p>