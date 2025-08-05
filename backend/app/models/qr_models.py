from pydantic import BaseModel, HttpUrl, validator
from typing import Optional, Literal
from enum import Enum

class QRCodeType(str, Enum):
    URL = "url"
    TEXT = "text"
    CONTACT = "contact"
    WIFI = "wifi"
    EMAIL = "email"
    PHONE = "phone"
    SMS = "sms"

class ErrorCorrectionLevel(str, Enum):
    L = "L"  # 7% recovery
    M = "M"  # 15% recovery
    Q = "Q"  # 25% recovery
    H = "H"  # 30% recovery

class QRCodeRequest(BaseModel):
    content: str
    qr_type: QRCodeType = QRCodeType.URL
    size: int = 10
    error_correction: ErrorCorrectionLevel = ErrorCorrectionLevel.M
    border: int = 4
    foreground_color: str = "#000000"
    background_color: str = "#FFFFFF"
    logo_url: Optional[str] = None
    
    @validator('size')
    def validate_size(cls, v):
        if v < 1 or v > 40:
            raise ValueError('Size must be between 1 and 40')
        return v
    
    @validator('border')
    def validate_border(cls, v):
        if v < 0 or v > 10:
            raise ValueError('Border must be between 0 and 10')
        return v

class ContactInfo(BaseModel):
    name: str
    phone: Optional[str] = None
    email: Optional[str] = None
    company: Optional[str] = None
    title: Optional[str] = None
    address: Optional[str] = None
    website: Optional[str] = None

class WiFiInfo(BaseModel):
    ssid: str
    password: str
    encryption: Literal["WPA", "WEP", "nopass"] = "WPA"
    hidden: bool = False

class EmailInfo(BaseModel):
    email: str
    subject: Optional[str] = None
    body: Optional[str] = None

class SMSInfo(BaseModel):
    phone: str
    message: str

class QRCodeResponse(BaseModel):
    success: bool
    qr_code_data: Optional[str] = None  # Base64 encoded image
    qr_code_url: Optional[str] = None
    error: Optional[str] = None
    metadata: Optional[dict] = None

class AISuggestionRequest(BaseModel):
    content: str
    qr_type: QRCodeType
    context: Optional[str] = None

class AISuggestionResponse(BaseModel):
    suggestions: list[str]
    optimized_content: Optional[str] = None
    confidence_score: float 