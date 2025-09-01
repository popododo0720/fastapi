from fastapi import FastAPI
import uvicorn
from core import message_hub

def create_app() -> FastAPI:
    """Create FASTAPI APP"""
    app = FastAPI(title="pythion-bind", version="1.0.0")
    
    @app.get("/")
    def root():
        return {
            "message": "message hub",
            "queue_status": message_hub.get_queue_sizes()
        }
    
    @app.get("/1")
    def trigger_program1():
        """program1 trigger"""
        success = message_hub.send_message("program1", "get from api!!!")
        return {
            "message": "send program 1",
            "success": success
        }
    
    @app.get("/2")
    def trigger_program2():
        """program2 trigger"""
        success = message_hub.send_message("program2", "get from api!!!")
        return {
            "message": "send program 2", 
            "success": success
        }
    
    @app.get("/3")
    def trigger_program3():
        """program3 trigger"""
        success = message_hub.send_message("program3", "get from api!!!")
        return {
            "message": "send program 3",
            "success": success
        }
    
    @app.get("/4")
    def trigger_program4():
        """program4 trigger"""
        success = message_hub.send_message("program4", "Hello from API!")
        return {
            "message": "send program 4 (C binding Hello World)",
            "success": success
        }
    
    @app.get("/status")
    def get_status():
        """system status"""
        return {
            "queues": message_hub.get_queue_sizes(),
            "total_pending": sum(message_hub.get_queue_sizes().values())
        }
    
    return app

def run_server(host: str = "0.0.0.0", port: int = 3312):
    """start api server"""
    app = create_app()
    uvicorn.run(app, host=host, port=port, log_level="warning")