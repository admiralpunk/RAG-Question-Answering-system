from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
from dotenv import load_dotenv
import os

from routes import pdf_routes, qa_routes

# Load environment variables
load_dotenv()

app = FastAPI(title="PDF QA API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(pdf_routes.router, prefix="/api/pdf", tags=["PDF"])
app.include_router(qa_routes.router, prefix="/api/qa", tags=["QA"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)