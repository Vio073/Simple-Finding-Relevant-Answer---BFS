from collections import deque

def bfs_faq_search(faq_graph, query):
    if query not in faq_graph:
        return "Query not found in FAQ graph"
    queue = deque([query])
    visited = set()  
    while queue:
        node = queue.popleft()
        if node in faq_graph["answers"]:
            return faq_graph["answers"][node] 
        if node not in visited:
            visited.add(node)
            queue.extend(faq_graph.get(node, []))  
    return "No relevant answer found"

faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

query = "What is AI?"
print(bfs_faq_search(faq_graph, query))
