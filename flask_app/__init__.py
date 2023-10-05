from flask import Flask, render_template, request, redirect, session
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
app.api_key = os.getenv('API_KEY')