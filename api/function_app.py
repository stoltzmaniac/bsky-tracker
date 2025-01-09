import azure.functions as func
import logging
import json


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="message")
def message(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    msg = json.dumps(
        {
            "hello": "there"
        }
    )

    return func.HttpResponse(
            msg,
            status_code=200
    )