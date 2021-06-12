"""Get visual similarity distance using turicreate"""
import turicreate as tc

reference_data  = tc.image_analysis.load_images('.//id_drawings')
reference_data = reference_data.add_row_number()
model = tc.image_similarity.create(reference_data)
query_results = model.query(reference_data[0:370], k=370)
query_results.save('.//turi_distances.csv', format='csv')
