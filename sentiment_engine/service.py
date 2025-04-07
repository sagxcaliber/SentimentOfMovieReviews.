import os
import cohere
from fastapi.encoders import jsonable_encoder
import json

from config import api_key, prompt, max_token, model, temperature
from sentiment_engine.helper.sentiment_helper import SentimentAnalysisInput, AnalysisResponses, AnalysisResponse
from type import ReviewInput


class SentimentService:
    def __init__(self):
        self.co = cohere.Client(api_key)
        self.data = []

    def check_sentiment(self, review: SentimentAnalysisInput):
        response = self.co.generate(
            model=model
            , prompt=prompt.format(review=review.review)
            , max_tokens=max_token
            , temperature=temperature
        )
        return response.generations[0].text.strip()

    def fetch_sentiment(self, review: ReviewInput):
        final_response = AnalysisResponses(response=[
            AnalysisResponse(
                review=review.review
                , result=self.check_sentiment(
                    review=SentimentAnalysisInput(
                        review=review.review
                    )
                )
            )
        ])
        res = jsonable_encoder(final_response)
        self.data.append(res.get('response')[0])
        self.dump_reviews()
        return res

    def list_reviews(self):
        with open('./output.json', 'r') as f:
            output_data = json.load(f)

        return [] if not output_data else output_data

    def dump_reviews(self):
        res:list = self.list_reviews()
        res.extend(self.data)
        with open('./output.json', 'a') as f:
            json.dump(res, f)
