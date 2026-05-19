import uvicorn
import os
from app import create_app, generate_app_config


def main():
    app_config = generate_app_config(
        root_path=os.getenv("ROOT_PATH"), app_version=os.getenv("APP_VERSION")
    )
    app = create_app(             
        
        
        app_config)
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("SERVER_PORT", 8000)))


if __name__ == "__main__":
    main()
