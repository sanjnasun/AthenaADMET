from app.models.input_compound_model import InputCompound
from app.models.similar_compound_model import SimilarCompound
from typing import List

def get_compounds(req: InputCompound) -> List[SimilarCompound]:
	"""
	Compares a list of compounds and returns a list of similar compounds
	Uses the compare_compounds_service to compare the compounds
	"""
	return