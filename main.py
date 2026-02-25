"""
Machine Predictive Maintenance Classification API — Entry Point

This is the slim entry point that creates the app via the factory pattern.
Run with: uvicorn main:app --reload
"""

from app import create_app

app = create_app()
