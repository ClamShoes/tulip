import streamlit as st
import requests
import pandas as pd
import altair as alt

# Set the backend API endpoint
BACKEND_API_URL = 'http://13.236.135.206:5000'

# Function to reset the game
def reset_game():
    response = requests.post(f'{BACKEND_API_URL}/reset_game')
    if response.status_code == 200:
        st.success('Game reset successful')
    else:
        st.error('Failed to reset game')

# Function to start the game
def start_game():
    response = requests.post(f'{BACKEND_API_URL}/start_game')
    if response.status_code == 200:
        st.success('Game started successfully')
    else:
        st.error('Failed to start game')

# Function to stop the game
def stop_game():
    response = requests.post(f'{BACKEND_API_URL}/stop_game')
    if response.status_code == 200:
        st.success('Game stopped successfully')
    else:
        st.error('Failed to stop game')

# Fetch coin status
def fetch_coin_status():
    response = requests.get(f'{BACKEND_API_URL}/coin_status')
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch coin status')
        return None

# Fetch price history
def fetch_price_history():
    response = requests.get(f'{BACKEND_API_URL}/price_history')
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch price history')
        return []

# UI setup
st.title('Trading Game Dashboard')

if st.button('Start Game'):
    start_game()

if st.button('Stop Game'):
    stop_game()

if st.button('Reset Game'):
    reset_game
