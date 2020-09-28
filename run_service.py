from app import create_app
import os

if __name__ == "__main__":
    app = create_app()
    app.config['JSON_AS_ASCII'] = False
    # Run Flask app
    app.run(host='0.0.0.0', port=os.getenv('SERVICE_PORT', 1000), threaded=True)