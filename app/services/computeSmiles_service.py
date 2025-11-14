from app.models.input_compound_model import SmilesUploadRequest, SmilesUploadResponse


def compute_rdkit_values(smiles_list: SmilesUploadRequest) -> SmilesUploadResponse:
	"""
	Processes a list of SMILES strings using rdkit and returns a list of InputCompound objects
	"""
	return