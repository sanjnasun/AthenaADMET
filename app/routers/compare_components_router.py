from fastapi import APIRouter, HTTPException
from typing import List
from app.services import compare_compounds_service
from app.services import computeSmiles_service
from app.models.input_compound_model import InputCompound, SmilesUploadRequest, SmilesUploadResponse
from app.models.similar_compound_model import SimilarCompound

router = APIRouter(prefix="", tags=["similarity"])

# computes all RDKit values for a list of SMILES
@router.post("/sendSmiles", response_model=SmilesUploadResponse)
def send_smiles_endpoint(req: SmilesUploadRequest) -> SmilesUploadResponse:
	if not req.smiles_list:
		raise HTTPException(status_code=400, detail="SMILES list cannot be empty")
	
	try:
		upload_req = SmilesUploadRequest(smiles_list=req.smiles_list)
		response = computeSmiles_service.compute_rdkit_values(upload_req)
		return SmilesUploadResponse(compounds=response.compounds)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))



# gets all similar compounds for one InputCompound
@router.post("/getCompounds", response_model=List[SimilarCompound])
def get_compound_endopoint(req: InputCompound) -> List[SimilarCompound]:
	
	try:
		response = compare_compounds_service.get_compounds(req)
		return response
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))



# gets all similar compounds for a list of InputCompounds
@router.get("/sendComponent", response_mode=SmilesUploadResponse)
def send_component_endpoint(req: SmilesUploadResponse) -> SmilesUploadResponse:
	
	for compound in req.compounds:
		compound.similar_compounds = compare_compounds_service.get_compounds(compound)
	
	return req