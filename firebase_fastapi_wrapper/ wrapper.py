import logging
import traceback
from starlette.testclient import TestClient
from typing import Optional, Union
from firebase_functions import https_fn

# Configure logging
logger = logging.getLogger("firebase_handler")
logger.setLevel(logging.INFO)

class FastAPIWrapper:
    def __init__(self, app):
        self.client = TestClient(app)

    def __call__(self, req) -> "firebase_functions.https_fn.Response":
        """
        Wraps a FastAPI app and adapts it for Firebase HTTP function requests.

        Args:
            req: Firebase https_fn.Request object

        Returns:
            Firebase https_fn.Response object
        """
        try:
            logger.info(f"Received {req.method} request to {req.path}")

            path = req.path
            query = req.query_string.decode("utf-8") if hasattr(req, "query_string") and req.query_string else ""
            full_url = f"{path}?{query}" if query else path

            headers = dict(req.headers)
            body: Optional[Union[bytes, str]] = None
            if req.method in ("POST", "PUT", "PATCH"):
                body = req.get_data()

            logger.debug(f"Forwarding {req.method} to {full_url}")
            response = self.client.request(
                method=req.method,
                url=full_url,
                headers=headers,
                content=body,
            )

            return https_fn.Response(
                response=response.content,
                status=response.status_code,
                headers=dict(response.headers),
            )

        except Exception as e:
            logger.error(f"Error in FastAPIWrapper: {str(e)}")
            logger.error(traceback.format_exc())
            from firebase_functions import https_fn
            return https_fn.Response(
                response=f"Internal server error: {e}",
                status=500,
                headers={"Content-Type": "text/plain"},
            )
