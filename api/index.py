import sys
import os

# Add project root to path so Vercel can find the 'app' package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app
