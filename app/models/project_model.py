from typing import List, Dict
from .similar_compound_model import SimilarCompound

class ProjectCreateRequest():
	"""
	Request body for POST /newProject
	"""
	name: str

class AddCompoundsRequest():
	"""
	Request body for POST /{project_id}/addCompounds
	"""
	compounds: List[str]

class ProjectResponse():
	"""
	Basic project info returned after creation or fetch
	"""
	project_id: str
	name: str

class ProjectResultsResponse():
	"""
	Returning similarity results in a project
	inputs is a list of input SMILES for the project
	results is a mapping of the input SMILES to a list of similar compounds
	"""
	project_id: str
	name: str
	inputs: List[str]
	results: Dict[str, List[SimilarCompound]]
