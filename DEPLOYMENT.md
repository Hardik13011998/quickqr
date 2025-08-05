# 🌐 QuickQR Internet Deployment Guide

## 🚀 Deploy to the Internet

This guide will help you deploy your QuickQR application to the internet so you can scan QR codes from anywhere!

## 📋 Prerequisites

1. **GitHub Account** (free)
2. **Railway Account** (free tier available)
3. **Vercel Account** (free tier available)

## 🔧 Step 1: Deploy Backend to Railway

### 1.1 Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/quickqr.git
git push -u origin main
```

### 1.2 Deploy to Railway
1. Go to [Railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your QuickQR repository
5. Set the root directory to `backend`
6. Railway will automatically detect it's a Python app
7. Deploy!

### 1.3 Get Your Backend URL
After deployment, Railway will give you a URL like:
`https://quickqr-backend-production.up.railway.app`

## 🔧 Step 2: Deploy Frontend to Vercel

### 2.1 Update API URL
Edit `frontend/src/services/api.ts`:
```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://your-railway-url.up.railway.app/api/v1'
```

### 2.2 Deploy to Vercel
1. Go to [Vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click "New Project"
4. Import your GitHub repository
5. Set the root directory to `frontend`
6. Deploy!

### 2.3 Get Your Frontend URL
After deployment, Vercel will give you a URL like:
`https://quickqr-frontend.vercel.app`

## 🔧 Step 3: Update CORS Settings

Update `backend/app/core/config.py` with your Vercel URL:
```python
BACKEND_CORS_ORIGINS: list = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:5174",
    "https://your-frontend-url.vercel.app",  # Add your Vercel URL here
]
```

## 🌐 Alternative: Deploy to Render (Free)

### Backend on Render
1. Go to [Render.com](https://render.com)
2. Sign up with GitHub
3. Click "New Web Service"
4. Connect your GitHub repo
5. Set:
   - **Name:** `quickqr-backend`
   - **Root Directory:** `backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Deploy!

### Frontend on Render
1. Click "New Static Site"
2. Connect your GitHub repo
3. Set:
   - **Name:** `quickqr-frontend`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `dist`
4. Deploy!

## 📱 Test Your Deployment

1. **Access your frontend:** `https://your-frontend-url.vercel.app`
2. **Generate a QR code** with any URL
3. **Scan with your mobile device** from anywhere in the world!
4. **The QR code should work perfectly!** 🎉

## 🔗 Quick Deploy Links

### Railway (Backend)
- **URL:** https://railway.app
- **Free tier:** 500 hours/month
- **Auto-deploy:** Yes

### Vercel (Frontend)
- **URL:** https://vercel.com
- **Free tier:** Unlimited
- **Auto-deploy:** Yes

### Render (Both)
- **URL:** https://render.com
- **Free tier:** 750 hours/month
- **Auto-deploy:** Yes

## 🛠️ Troubleshooting

### If backend deployment fails:
1. Check `requirements.txt` is in the backend folder
2. Verify `Procfile` exists
3. Check logs in Railway/Render dashboard

### If frontend can't connect to backend:
1. Update CORS settings with your frontend URL
2. Check environment variables
3. Verify backend URL is correct

### If QR codes don't work:
1. Make sure you're using the deployed frontend URL
2. Test with a simple URL first
3. Check browser console for errors

## 🎯 Benefits of Internet Deployment

- ✅ **Access from anywhere** - No network restrictions
- ✅ **Real-world testing** - Test QR codes on any device
- ✅ **Share with others** - Anyone can use your app
- ✅ **Always available** - 24/7 uptime
- ✅ **Professional URLs** - Clean, shareable links

## 📞 Quick Start Commands

```bash
# Deploy backend to Railway
railway login
railway init
railway up

# Deploy frontend to Vercel
vercel login
vercel --prod
```

Your QuickQR app will be live on the internet! 🌍✨ 