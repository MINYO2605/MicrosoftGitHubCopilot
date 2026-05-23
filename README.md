# Azure Text-to-Speech Streamlit App

This Streamlit app lets you enter text, choose an Azure voice, and generate speech audio using Azure Speech Services.

## Setup

1. Create a Python virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

- Enter your Azure Speech API key and region.
- Select a voice from the dropdown.
- Enter the text you want to hear.
- Click `Read text aloud`.

The app will generate a WAV audio file and show an audio player for playback in the browser.

## Azure Speech resource

Create an Azure Speech resource in the Azure portal and copy the `Key` and `Region` values.
