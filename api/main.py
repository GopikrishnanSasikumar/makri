import json
from fastapi import FastAPI
from api.classifier import ZeroShotClassifier
from api.models import ClassificationRequest
from api.resources import ResourceRetriever

app = FastAPI()

dataset = json.load(open("data/learning-paths.json"))
classifier = ZeroShotClassifier()
resource = ResourceRetriever(dataset)

@app.post("/learning-path")
def classify_text(request: ClassificationRequest):
    """
    method for processing learning path request
    """
    candidate_labels = resource.retrieve_learning_topics()
    topic, _ = classifier.classify(request.text, candidate_labels)
    result = resource.retrieve_url(topic)
    return {
        "result": result
    }