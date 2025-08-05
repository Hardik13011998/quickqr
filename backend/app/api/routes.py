from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional
from app.models.qr_models import (
    QRCodeRequest, QRCodeResponse, AISuggestionRequest, AISuggestionResponse
)
from app.services.qr_service import QRCodeService
from app.services.ai_service import AIService

# Create routers
qr_router = APIRouter()
ai_router = APIRouter()

# Initialize services
qr_service = QRCodeService()
ai_service = AIService()

@qr_router.post("/generate", response_model=QRCodeResponse)
async def generate_qr_code(request: QRCodeRequest):
    """Generate a QR code with the specified parameters"""
    try:
        # Validate content
        if not request.content.strip():
            raise HTTPException(status_code=400, detail="Content cannot be empty")
        
        # Generate QR code
        result = qr_service.generate_qr_code(request)
        
        if result["success"]:
            return QRCodeResponse(
                success=True,
                qr_code_data=result["qr_code_data"],
                metadata=result["metadata"]
            )
        else:
            raise HTTPException(status_code=500, detail=result["error"])
            
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate QR code: {str(e)}")

@qr_router.get("/types")
async def get_qr_types():
    """Get available QR code types"""
    return {
        "types": [
            {"value": "url", "label": "URL", "description": "Website links"},
            {"value": "text", "label": "Text", "description": "Plain text content"},
            {"value": "contact", "label": "Contact", "description": "Contact information (vCard)"},
            {"value": "wifi", "label": "WiFi", "description": "WiFi network credentials"},
            {"value": "email", "label": "Email", "description": "Email address"},
            {"value": "phone", "label": "Phone", "description": "Phone number"},
            {"value": "sms", "label": "SMS", "description": "Text message"}
        ]
    }

@qr_router.get("/error-correction-levels")
async def get_error_correction_levels():
    """Get available error correction levels"""
    return {
        "levels": [
            {"value": "L", "label": "Low (7%)", "description": "Lowest error correction"},
            {"value": "M", "label": "Medium (15%)", "description": "Default level"},
            {"value": "Q", "label": "Quartile (25%)", "description": "Higher error correction"},
            {"value": "H", "label": "High (30%)", "description": "Highest error correction"}
        ]
    }

@qr_router.post("/validate-url")
async def validate_url(url: str):
    """Validate URL format"""
    is_valid = qr_service.validate_url(url)
    return {
        "url": url,
        "is_valid": is_valid,
        "suggestions": [] if is_valid else ["Add https:// protocol", "Check URL format"]
    }

@ai_router.post("/suggestions", response_model=AISuggestionResponse)
async def get_ai_suggestions(request: AISuggestionRequest):
    """Get AI-powered suggestions for QR code content"""
    try:
        if not request.content.strip():
            raise HTTPException(status_code=400, detail="Content cannot be empty")
        
        result = await ai_service.get_suggestions(
            request.content, 
            request.qr_type, 
            request.context
        )
        
        return AISuggestionResponse(
            suggestions=result["suggestions"],
            optimized_content=result["optimized_content"],
            confidence_score=result["confidence_score"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get AI suggestions: {str(e)}")

@ai_router.post("/analyze")
async def analyze_content(content: str, qr_type: str):
    """Analyze QR code content for potential issues"""
    try:
        if not content.strip():
            raise HTTPException(status_code=400, detail="Content cannot be empty")
        
        analysis = await ai_service.analyze_content(content, qr_type)
        return analysis
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to analyze content: {str(e)}")

@ai_router.get("/health")
async def ai_health_check():
    """Check AI service health"""
    return {
        "status": "healthy",
        "ai_available": ai_service.client is not None,
        "service": "QuickQR AI Service"
    } 