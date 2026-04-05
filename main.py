"""
Main FastAPI application for Sentiment Analysis
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from config.settings import settings
from app.routes import router

# Create FastAPI app instance
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware to allow requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

# Welcome route
@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Sentiment Analysis API",
        "docs": "/docs",
        "version": settings.API_VERSION
    }

# Error handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

if __name__ == "__main__":
    import uvicorn
    
    print(f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║        Sentiment Analysis API - Starting Server              ║
    ║─────────────────────────────────────────────────────────────║
    ║  API Docs:     http://{settings.HOST}:{settings.PORT}/docs          ║
    ║  ReDoc:        http://{settings.HOST}:{settings.PORT}/redoc         ║
    ║  API Info:     http://{settings.HOST}:{settings.PORT}/info          ║
    ║─────────────────────────────────────────────────────────────║
    ║  Model: {settings.MODEL_NAME}  ║
    ║  Version: {settings.API_VERSION}                                     ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
