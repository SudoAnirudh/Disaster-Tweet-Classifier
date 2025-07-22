# Disaster Tweet Sentiment Analysis

This app fetches tweets about disasters, analyzes their sentiment/emotion using a BERT model, and visualizes them on a map.

## How to Run Locally

1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Run the app:
   ```powershell
   streamlit run app.py
   ```

## Deployment
You can deploy this app publicly using [Streamlit Community Cloud](https://streamlit.io/cloud):
- Push your code to GitHub.
- Go to Streamlit Cloud, sign in, and create a new app from your repo.
- Set your Twitter API keys as secrets in the Streamlit Cloud settings.

## Notes
- You need valid Twitter API credentials.
- The emotion model used: `mrm8488/bert-tiny-5-finetuned-emotion`.

---
Developed by @SudoAnirudh
Model by @mrm8488
Built with Streamlit and Folium
