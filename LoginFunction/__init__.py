import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Login function received a request.")

    try:
        req_body = req.get_json()
        email = req_body.get("email")
        password = req_body.get("password")

        # Basit kontrol, gerçek projede DB veya başka servis
        if email == "test@example.com" and password == "1234":
            return func.HttpResponse(
                json.dumps({"message": "Login successful!"}),
                mimetype="application/json",
                status_code=200
            )
        else:
            return func.HttpResponse(
                json.dumps({"detail": "Invalid credentials"}),
                mimetype="application/json",
                status_code=401
            )

    except ValueError:
        return func.HttpResponse(
            json.dumps({"detail": "Invalid JSON"}),
            mimetype="application/json",
            status_code=400
        )
