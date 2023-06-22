from typing import List
from transformers import pipeline


class ZeroShotClassifier:
    """
    Zero shot classifier class
    """

    def __init__(self):
        self.classifier = pipeline(
            "zero-shot-classification", model="textattack/roberta-base-MNLI")

    def classify(self, text: str, candidate_labels: List[str]) -> str:
        """
        classify text as learning path topic
        """
        result = self.simple_search(text, candidate_labels)
        if result:
            return result[0], result[1]
        result = self.classifier(text, candidate_labels)
        return result["labels"][0], result["scores"][0]

    def simple_search(self, text: str, candidate_labels: List[str]) -> dict:
        """
        Simply search for keywords
        """
        for label in candidate_labels:
            if label in text:
                return label, 1.0
        return "", 0.0
