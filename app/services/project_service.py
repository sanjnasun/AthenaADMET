from dataclasses import dataclass
from app.models.similar_compound_model import SimilarCompound

@dataclass
class Project:
	id: str
	name: str
	inputs: list[str]
	results: dict[str, list[SimilarCompound]]

def create_project(name: str) -> Project:
	return

def add_compounds(project_id: str, compounds: list[str]) -> Project:
	return

def get_project_with_results(project_id: str) -> Project:
	return