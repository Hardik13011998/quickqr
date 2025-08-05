from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "QuickQR API"
    
    # CORS Configuration
    BACKEND_CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "https://quickqr-frontend.vercel.app",
        "https://quickqr-frontend.onrender.com",
        "https://quickqr-frontend.netlify.app"
    ]
    
    # Environment
    ENVIRONMENT: str = "development"
    
    # Port configuration for deployment
    PORT: Optional[int] = None
    
    # AI Configuration
    OPENAI_API_KEY: Optional[str] = None
    
    # QR Code Configuration
    QR_DEFAULT_SIZE: int = 10
    QR_DEFAULT_ERROR_CORRECTION: str = "M"  # L, M, Q, H
    QR_DEFAULT_BORDER: int = 4
    
    # File Storage
    UPLOAD_DIR: str = "uploads"
    STATIC_DIR: str = "static"
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

# Ensure directories exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.STATIC_DIR, exist_ok=True) 

# Get port from environment variable (for deployment)
def get_port():
    return int(os.environ.get("PORT", 8000)) 