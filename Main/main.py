from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_test

app = FastAPI()


@app.post("/")
async def handle_request(request: Request):

    payload = await request.json()

    intent=payload['queryResult']['intent']['displayName']
    parameters=payload['queryResult']['parameters']['Object-name']

    if intent == "Object":
        return track_object(parameters[0])


def track_object(parameters: str):
    result = db_test.find(parameters)

    if result:
        fulfillment_text = result
    else:
        fulfillment_text = f"No {parameters} object was found in database" \
                           f"I can help you to find objects such as cell phone, bottle, backpack, umbrella, handbag, suitcase, laptop, mouse, remote, keyboard, scissors, hair dryer, toothbrush"

    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

# print(db_test.find('laptop'))