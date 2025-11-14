from typing import List

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

class SmilesUploadRequest():
	project_id: str
	smiles_list: List[str]

class SmilesUploadResponse():
	project_id: str
	compounds: List[InputCompound]