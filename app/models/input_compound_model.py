from typing import List
from .similar_compound_model import SimilarCompound

class InputCompound():
	id: str
	smiles: str
	name: str
	mw: float
	mf: str
	iupac: str
	alias: str
	inchi: str
	svg: str
	smiles_input: str
	fingerprint: str
	similar_compounds: List[SimilarCompound] = None

class SmilesUploadRequest():
	smiles_list: List[str]

class SmilesUploadResponse():
	compounds: List[InputCompound]