# QuickQR - AI-Powered QR Code Generator

A modern, AI-enhanced QR code generator application with a beautiful user interface.

## 🚀 Features

- **AI-Powered QR Generation**: Smart suggestions and content optimization
- **Modern UI**: Beautiful, responsive design with Tailwind CSS
- **Multiple QR Types**: URL, text, contact info, WiFi, and more
- **Customization**: Colors, logos, and styling options
- **Real-time Preview**: Instant QR code generation and preview
- **Export Options**: PNG, SVG, and PDF formats
- **User-Friendly**: Intuitive interface for all users

## 🛠️ Tech Stack

### Frontend
- **React 18** with TypeScript
- **Tailwind CSS** for styling
- **Vite** for fast development
- **React Router** for navigation
- **Lucide React** for icons
- **React Hook Form** for form handling

### Backend
- **Python FastAPI** for API
- **Pydantic** for data validation
- **QR Code generation** with qrcode library
- **AI Integration** for smart suggestions
- **CORS** enabled for frontend communication

## 📁 Project Structure

```
QuickQR/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── services/       # API services
│   │   ├── types/          # TypeScript type definitions
│   │   └── utils/          # Utility functions
│   ├── public/             # Static assets
│   └── package.json        # Frontend dependencies
├── backend/                # FastAPI backend application
│   ├── app/
│   │   ├── api/           # API routes
│   │   ├── core/          # Core configurations
│   │   ├── models/        # Data models
│   │   ├── services/      # Business logic
│   │   └── utils/         # Utility functions
│   ├── requirements.txt    # Python dependencies
│   └── main.py           # FastAPI application entry
├── docs/                  # Documentation
└── README.md             # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ 
- Python 3.8+
- npm or yarn

### Backend Setup
```bash
cd backend
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Access the Application
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 🎨 Features Overview

### QR Code Types Supported
- **URL QR Codes**: Direct links to websites
- **Text QR Codes**: Plain text content
- **Contact QR Codes**: vCard format contact information
- **WiFi QR Codes**: Network credentials
- **Email QR Codes**: Pre-filled email composition
- **Phone QR Codes**: Direct phone number dialing
- **SMS QR Codes**: Pre-filled text messages

### AI Features
- **Smart Content Suggestions**: AI-powered content recommendations
- **URL Optimization**: Intelligent URL shortening and validation
- **Content Analysis**: AI analysis of QR code content
- **Usage Analytics**: Smart insights on QR code usage

### Customization Options
- **Color Schemes**: Custom foreground and background colors
- **Logo Integration**: Add company logos to QR codes
- **Style Variations**: Different QR code styles
- **Size Options**: Multiple size configurations
- **Error Correction**: Adjustable error correction levels

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

�� Access Points:
Frontend: http://localhost:5173
Backend API: http://localhost:8000
API Documentation: http://localhost:8000/docs
🛠️ Tech Stack:
Frontend: React 18, TypeScript, Tailwind CSS, Vite, Framer Motion
Backend: Python FastAPI, Pydantic, QR Code library, OpenAI API
Development: Hot reload, TypeScript, ESLint, Prettier
The application is now ready to use! It includes everything you requested:
✅ Latest frontend technologies (React 18, TypeScript, Tailwind CSS)
✅ Python FastAPI backend with AI integration
✅ User-friendly modern UI
✅ AI-powered QR code generation
✅ Proper project structure and documentation
Ganapati Bappa Moriya! 🐘🙏 Your QuickQR application is now complete and ready to generate beautiful QR codes with AI intelligence!

**Ganapati Bappa Moriya!** 🐘🙏 