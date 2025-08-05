from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.api.routes import qr_router, ai_router, content_router
from app.core.config import settings, get_port
from app.core.database import create_tables
from app.models.database_models import Base

# Create FastAPI app instance
app = FastAPI(
    title="QuickQR API",
    description="AI-Powered QR Code Generator API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(qr_router, prefix="/api/v1/qr", tags=["QR Codes"])
app.include_router(ai_router, prefix="/api/v1/ai", tags=["AI Features"])
app.include_router(content_router, prefix="/api/v1", tags=["Content"])

# Mount static files for content images and uploads
app.mount("/content", StaticFiles(directory="content"), name="content")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Initialize database tables
@app.on_event("startup")
async def startup_event():
    create_tables()

@app.get("/")
async def root():
    return {
        "message": "QuickQR API is running!",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "QuickQR API"}

if __name__ == "__main__":
    port = get_port()
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=settings.ENVIRONMENT == "development",
        log_level="info"
    ) 