from fastapi import FastAPI, Body, HTTPException, status, Depends
from starlette.requests import Request

from models import Argument,\
                    ArgumentResponse

from transformer_model import Sentiment_Analyser

CONSTANTS = {
    "statusResponse": {
        "status": "Sentiment API up and running!"
    },
    "sentimentExample": {
        "body": "seni çok seviyorum",
        "domain": "general"
    }
        }

tags_metadata = [
    {
        "name": "Status",
    },
    {
        "name": "Evaluations",
        "description": "Operations to Make Predictions for text.",
    }
]

app = FastAPI(
    title= "Sentiment App",
    version="0.1",
    description="Simple Service for NLP",
    openapi_tags=tags_metadata
)

global sentiment_model
sentiment_model = Sentiment_Analyser()

@app.get('/status', tags=["Status"])
def status_check():
    return CONSTANTS["statusResponse"]


@app.post('/sentiment-analysis', summary = "Sentiment Analysis for Text", status_code = 200, tags=["Evaluations"])
def sentiment_eva(request: Request, argument: Argument = Body(..., example = CONSTANTS["sentimentExample"])):
    evaluation = sentiment_model.predict(argument.body)
    response = ArgumentResponse(body = argument.body, evaluation = evaluation)
    return response
