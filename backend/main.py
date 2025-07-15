import uvicorn
from src.core.config import ENV


if __name__ == "__main__":
    uvicorn.run(
        "src.api.app:app",
        reload=ENV == "dev",
        port=8000,
        host="0.0.0.0",
        workers=5,
    )
