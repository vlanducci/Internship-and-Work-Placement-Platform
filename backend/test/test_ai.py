from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

student = "I study software engineering and know Python, SQL and backend development."
internship = "Software developer internship requiring Python, databases and API development."

student_embedding = model.encode(student, convert_to_tensor=True)
internship_embedding = model.encode(internship, convert_to_tensor=True)

similarity = util.cos_sim(student_embedding, internship_embedding)

print(f"Similarity score: {similarity.item():.4f}")