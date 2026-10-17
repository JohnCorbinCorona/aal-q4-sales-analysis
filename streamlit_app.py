"""Host the verified AAL website and notebook report on Streamlit."""
from pathlib import Path
import base64
import re
import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="AAL | Q4 Sales Analysis", page_icon="📊", layout="wide")
st.markdown("<style>.block-container{padding-top:1rem}iframe{border:0}</style>", unsafe_allow_html=True)
requested = st.query_params.get("view", "site")
options = ["Sales website", "Full analysis report", "Download project files"]
page = st.sidebar.radio("AAL · Q4 2020", options, index=1 if requested == "report" else 0)
st.sidebar.caption("Applied Data Science with Python · Project 1")


@st.cache_data
def standalone(filename):
    document = (ROOT / filename).read_text()
    document = document.replace('<link rel="stylesheet" href="style.css">',
                                '<style>' + (ROOT / 'style.css').read_text() + '</style>')
    for script in ['data.js', 'app.js']:
        document = document.replace(f'<script src="{script}"></script>',
                                    '<script>' + (ROOT / script).read_text() + '</script>')
    for image in ['dashboard.png', 'distributions.png']:
        encoded = base64.b64encode((ROOT / image).read_bytes()).decode()
        uri = 'data:image/png;base64,' + encoded
        document = document.replace(f'src="{image}"', f'src="{uri}"')
        document = document.replace(f'href="{image}"', f'href="{uri}" target="_blank"')
    document = document.replace('href="report.html"', 'href="https://johncorbin-aal-sales.streamlit.app/?view=report" target="_top"')
    document = document.replace('href="index.html"', 'href="https://johncorbin-aal-sales.streamlit.app/?view=site" target="_top"')
    document = document.replace('href="index.html#', 'href="#')
    # Native download controls below the website work reliably on hosted browsers.
    for filename in ['Project_1_AAL_Sales_Analysis.ipynb', 'AusApparalSales4thQrt2020.csv']:
        document = document.replace(f'href="{filename}" download', 'href="#files"')
    document = document.replace('The notebook contains the Python code, Markdown explanations, weekly/monthly/quarterly reports, and the full Seaborn dashboard.',
        'The notebook contains all code and reports. Use the Download project files page in the sidebar for the notebook, CSV, and report downloads.')
    document = re.sub(r'<a class="button(?: secondary)?" href="#files">(?:Notebook ↓|Source CSV ↓)</a>', '', document)
    return document


if page == "Sales website":
    components.html(standalone('index.html'), height=3400, scrolling=True)
elif page == "Full analysis report":
    components.html(standalone('report.html'), height=1400, scrolling=True)
else:
    st.title("Project files")
    st.write("Download the notebook and CSV into the same folder before running the notebook in JupyterLab.")
    for label, filename, mime in [
        ("Download notebook", 'Project_1_AAL_Sales_Analysis.ipynb', 'application/x-ipynb+json'),
        ("Download source CSV", 'AusApparalSales4thQrt2020.csv', 'text/csv'),
        ("Download full report", 'report.html', 'text/html'),
        ("Download dashboard", 'dashboard.png', 'image/png'),
    ]:
        payload = standalone('report.html').encode() if filename == 'report.html' else (ROOT / filename).read_bytes()
        st.download_button(label, payload, file_name=filename, mime=mime)
    st.caption("The complete website source is also available in the GitHub repository.")
