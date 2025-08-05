import axios from 'axios'
import { QRCodeRequest, QRCodeResponse, AISuggestionRequest, AISuggestionResponse } from '../types'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor
api.interceptors.request.use(
  (config) => {
    // Add any auth tokens here if needed
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const message = error.response?.data?.detail || error.message || 'An error occurred'
    return Promise.reject({ message, status: error.response?.status })
  }
)

export const qrCodeAPI = {
  // Generate QR Code
  generateQR: async (request: QRCodeRequest): Promise<QRCodeResponse> => {
    const response = await api.post('/qr/generate', request)
    return response.data
  },

  // Get QR Code Types
  getTypes: async () => {
    const response = await api.get('/qr/types')
    return response.data
  },

  // Get Error Correction Levels
  getErrorCorrectionLevels: async () => {
    const response = await api.get('/qr/error-correction-levels')
    return response.data
  },

  // Validate URL
  validateURL: async (url: string) => {
    const response = await api.post('/qr/validate-url', { url })
    return response.data
  },
}

export const aiAPI = {
  // Get AI Suggestions
  getSuggestions: async (request: AISuggestionRequest): Promise<AISuggestionResponse> => {
    const response = await api.post('/ai/suggestions', request)
    return response.data
  },

  // Analyze Content
  analyzeContent: async (content: string, qr_type: string) => {
    const response = await api.post('/ai/analyze', { content, qr_type })
    return response.data
  },

  // Check AI Health
  checkHealth: async () => {
    const response = await api.get('/ai/health')
    return response.data
  },
}

export const healthAPI = {
  // Check API Health
  checkHealth: async () => {
    const response = await api.get('/health')
    return response.data
  },
}

export default api 