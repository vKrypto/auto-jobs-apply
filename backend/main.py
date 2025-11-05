from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.db import initialize_db
from config.openai_config import initialize_openai
from config.logger import logger
from routes.auto_apply_routes import router

app = FastAPI()

def initialize_services():
    # Initialize services
    logger.info("Initializing backend services...")
    initialize_db()
    initialize_openai()
    logger.info("Backend services initialized")

def shutdown_services():
    # Shutdown services
    logger.info("Shutting down backend services...")
    logger.info("Backend services shut down")

def lifespan(app: FastAPI):
    initialize_services()
    yield
    logger.info("Shutting down backend services...")
    shutdown_services()
    logger.info("Backend services shut down")


# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/health")
def health_check():
    logger.debug("Health check requested")
    return {"status": "ok", "message": "Backend is running"}

# API routes
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting backend server on port 5000")
    uvicorn.run(app, host="0.0.0.0", port=5000)
