import json
from typing import List

class ResourceRetriever:
    """
    Retrieve learning path topics and path urls
    """
    def __init__(self, dataset):
        self.dataset = dataset

    def retrieve_learning_topics(self) -> List[str]:
        """
        return learning path topics
        """
        labels = list(self.dataset)
        return labels
    
    def retrieve_url(self, topic) -> str:
        """
        return learning path url
        """
        url = self.dataset.get(topic)
        url = "learning path not available" if not url else url
        return url