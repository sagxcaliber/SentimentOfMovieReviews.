from dataclasses import dataclass
from typing import List


@dataclass
class SentimentAnalysisInput:
    review: str


@dataclass
class AnalysisResponse:
    review: str
    result: str


@dataclass
class AnalysisResponses:
    response: List[AnalysisResponse] = None
