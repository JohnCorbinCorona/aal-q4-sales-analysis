# AAL Q4 2020 Sales Analysis

Applied Data Science with Python — Project 1.

Live website: https://johncorbin-aal-sales.streamlit.app/

## Explore
- Open `index.html` for the interactive website (keep style.css, data.js, and app.js beside it).
- Open `report.html` for the complete notebook report with verified outputs and expandable code.
- Open `Project_1_AAL_Sales_Analysis.ipynb` in JupyterLab, with the supplied CSV in the same folder, and choose Run All Cells.

## Main findings
- Total sales: 340,302,500 (assumed AUD); units: 136,121.
- VIC leads state revenue; WA has the lowest revenue.
- Men lead demographic sales; Seniors are lowest, with a small gap.
- Morning leads time-of-day revenue; Evening is lowest.
- October 31 and December 31 are absent; no zero sales are imputed.

## Website
Static HTML/CSS/JavaScript; no build step or external services required. Use a static host, or run `python -m http.server 8000` in this directory. The demographic filter updates state rankings. Daily, weekly, monthly, and quarterly trend views include exact totals and coverage.

## Reproduce the notebook
Install packages in requirements.txt. The uploaded notebook is preserved as supplied; the HTML report uses a fresh successful execution of that notebook. Weekly periods run Monday–Sunday, with edge weeks restricted to Q4. No missing values or exact duplicate rows were found. Revenue is not profit, and store counts are unavailable.

Data source: the supplied course CSV. Currency is assumed AUD and is not specified in the source.
