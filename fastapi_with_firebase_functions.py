from firebase_functions import https_fn,options
import io
from typing import Any, Optional, Dict, List, Tuple, Callable
from starlette.testclient import TestClient
import logging
import traceback
from typing import Optional, Union
logger = logging.getLogger("firebase_handler")
logger.setLevel(logging.INFO)

app = FastAPI()
@https_fn.on_request()
def Maike_Agent_With_Web_Search(req: https_fn.Request) -> https_fn.Response:
    """
    HTTP function handler that forwards requests to a FastAPI application.
    
    Args:
        req: The HTTP request object from Firebase Functions.
        
    Returns:
        An HTTP response from the FastAPI application.
    """
    try:
        # Log incoming request
        logger.info(f"Received {req.method} request to {req.path}")
        
        # Create test client for our FastAPI app
        client = TestClient(app)
        
        # Prepare request details
        method = req.method
        path = req.path
        headers = dict(req.headers)
        
        # Handle query string if present
        query_string = ""
        if hasattr(req, "query_string") and req.query_string:
            query_string = req.query_string.decode("utf-8")
            logger.debug(f"Query string: {query_string}")
        
        # Build full URL
        full_url = path
        if query_string:
            full_url += f"?{query_string}"
        
        # Get request body if present
        body: Optional[Union[bytes, str]] = None
        if req.method in ("POST", "PUT", "PATCH"):
            body = req.get_data()
            if body:
                content_length = len(body)
                logger.debug(f"Request body size: {content_length} bytes")
        
        # Make internal request to FastAPI app
        logger.debug(f"Forwarding {method} request to FastAPI at {full_url}")
        response = client.request(
            method=method,
            url=full_url,
            headers=headers,
            content=body,  # Using content instead of data for better compatibility
        )
        
        # Log response details
        logger.info(f"FastAPI responded with status code {response.status_code}")
        
        # Create and return Firebase HTTP Response
        return https_fn.Response(
            response=response.content,
            status=response.status_code,
            headers=dict(response.headers),
        )
    
    except Exception as e:
        # Log the error with traceback
        logger.error(f"Error in firebase_handler: {str(e)}")
        logger.error(traceback.format_exc())
        
        # Return a 500 error response
        return https_fn.Response(
            response=f"Internal server error: {str(e)}",
            status=500,
            headers={"Content-Type": "text/plain"},
        )
