# Flood Frequency Analysis – Ganga River

**Author:** Drishti Lunia  
**Data source:** DAHITI satellite altimetry (Ganges station ID 19519)  
**Why this project?**  
I wanted to understand flood risk on the Ganga River using real data. This analysis estimates how often extreme high water levels occur — useful for flood damage assessment and nature-based solutions.

## What I did
- Collected annual max water levels (2010–2024) from DAHITI
- Used Python (Pandas, SciPy, Matplotlib) to fit a Gumbel distribution
- Calculated return periods (2, 5, 10, 25, 50, 100 years)

## Files in this repo
- `ganga_water_level.csv` – the data I used
- `flood_frequency.py` – the code
- `flood_frequency_plot.png` – final plot

## Key result
The 50‑year return period water level is ~146.5 m. Major flood years (2013, 2019) clearly stand out.

## What I learned
- Flood frequency analysis using Weibull + Gumbel
- Working with satellite altimetry data
- Making reproducible research public on GitHub

## Next step (if I get the internship)
Apply this method to flood damage assessment for the business sector — one of Prof. Dewals' research topics at ULiège.


This is my first self‑directed research project in hydrology.
Open to feedback and suggestions!
