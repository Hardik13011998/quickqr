import { useState } from 'react'
import { UseFormRegister, FieldErrors } from 'react-hook-form'
import { QRCodeRequest, QRCodeType } from '../types'
import { Globe, FileText, User, Wifi, Mail, Phone, MessageSquare } from 'lucide-react'

interface QRCodeFormProps {
  register: UseFormRegister<QRCodeRequest>
  errors: FieldErrors<QRCodeRequest>
  onSubmit: (data: QRCodeRequest) => void
  isGenerating: boolean
}

const QRCodeForm = ({ register, errors, onSubmit, isGenerating }: QRCodeFormProps) => {
  const [qrType, setQrType] = useState<QRCodeRequest['qr_type']>('url')

  const qrTypeOptions = [
    { value: 'url', label: 'URL', icon: Globe, description: 'Website links' },
    { value: 'text', label: 'Text', icon: FileText, description: 'Plain text content' },
    { value: 'contact', label: 'Contact', icon: User, description: 'Contact information' },
    { value: 'wifi', label: 'WiFi', icon: Wifi, description: 'Network credentials' },
    { value: 'email', label: 'Email', icon: Mail, description: 'Email address' },
    { value: 'phone', label: 'Phone', icon: Phone, description: 'Phone number' },
    { value: 'sms', label: 'SMS', icon: MessageSquare, description: 'Text message' }
  ]

  const getPlaceholder = (type: string) => {
    switch (type) {
      case 'url':
        return 'https://example.com'
      case 'text':
        return 'Enter your text here...'
      case 'contact':
        return 'John Doe, john@example.com, +1234567890'
      case 'wifi':
        return 'NetworkName, Password, WPA'
      case 'email':
        return 'john@example.com'
      case 'phone':
        return '+1234567890'
      case 'sms':
        return '+1234567890:Your message here'
      default:
        return 'Enter content...'
    }
  }

  return (
    <form onSubmit={(e) => e.preventDefault()}>
      {/* QR Type Selection */}
      <div className="mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-3">
          QR Code Type
        </label>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
          {qrTypeOptions.map((option) => {
            const Icon = option.icon
            return (
              <button
                key={option.value}
                type="button"
                onClick={() => setQrType(option.value as QRCodeType)}
                className={`p-3 rounded-lg border-2 transition-all duration-200 text-left ${
                  qrType === option.value
                    ? 'border-primary-500 bg-primary-50 text-primary-700'
                    : 'border-gray-200 hover:border-gray-300 bg-white'
                }`}
              >
                <div className="flex items-center space-x-2">
                  <Icon className="w-4 h-4" />
                  <span className="text-sm font-medium">{option.label}</span>
                </div>
                <p className="text-xs text-gray-500 mt-1">{option.description}</p>
              </button>
            )
          })}
        </div>
        <input
          type="hidden"
          {...register('qr_type')}
          value={qrType}
        />
      </div>

      {/* Content Input */}
      <div className="mb-6">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Content
        </label>
        <textarea
          {...register('content', { required: 'Content is required' })}
          placeholder={getPlaceholder(qrType)}
          className={`input min-h-[100px] resize-none ${
            errors.content ? 'border-error-500 focus:border-error-500 focus:ring-error-500' : ''
          }`}
        />
        {errors.content && (
          <p className="mt-1 text-sm text-error-600">{errors.content.message}</p>
        )}
      </div>

      {/* Generate Button */}
      <button
        type="submit"
        onClick={() => onSubmit({ content: '', qr_type: qrType, size: 10, error_correction: 'M', border: 4, foreground_color: '#000000', background_color: '#FFFFFF' })}
        disabled={isGenerating}
        className="w-full btn-primary py-3 text-base font-medium"
      >
        {isGenerating ? (
          <div className="flex items-center justify-center">
            <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
            Generating...
          </div>
        ) : (
          <div className="flex items-center justify-center">
            <Globe className="w-5 h-5 mr-2" />
            Generate QR Code
          </div>
        )}
      </button>
    </form>
  )
}

export default QRCodeForm 