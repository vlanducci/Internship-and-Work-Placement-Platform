# test_ai.py
# Tests Sentence Transformers by comparing a student's skills and experience with an internship description and calculating their semantic similarity.

from sentence_transformers import SentenceTransformer, util

# Loads a pretrained sentence-embedding model for comparing text.
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Example student profile describing their skills and experience.
student = "I study software engineering and know Python, SQL and backend development."
# Example internship description listing the required skills.
internship = "Software developer internship requiring Python, databases and API development." 

# Converts the student profile into a numerical embedding for semantic comparison.
student_embedding = model.encode(student, convert_to_tensor=True)
# Converts the internship description into a numerical embedding.
internship_embedding = model.encode(internship, convert_to_tensor=True)

# Calculates cosine similarity between the two embeddings.
similarity = util.cos_sim(student_embedding, internship_embedding)

print(f"Similarity score: {similarity.item():.4f}")