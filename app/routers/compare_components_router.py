from fastapi import APIRouter, HTTPException, Query
from app.models.similar_compound_model import SimilarCompound
from typing import List
from app.services import compare_compounds_service
from app.models.input_compound_model import InputCompound, SmilesUploadRequest, SmilesUploadResponse
router = APIRouter(prefix="", tags=["similarity"])
from app.services import computeSmiles_service


@router.post("/sendSmiles", response_model=SmilesUploadResponse)
def send_smiles_endpoint(req: SmilesUploadRequest) -> SmilesUploadResponse:
	if not req.smiles_list:
		raise HTTPException(status_code=400, detail="SMILES list cannot be empty")
	
	try:
		compounds = computeSmiles_service.compute_rdkit_values(req.smiles_list)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
	
	return SmilesUploadResponse(compounds=compounds)


# idk how we're gonna implement multi-threading yet like prob changing this
@router.get("/getCompounds", response_model=List[SimilarCompound])
def get_compound_endopoint(req: InputCompound) -> List[SimilarCompound]:
	if not InputCompound.fingerprint:
		raise HTTPException(status_code=400, detail="Cannot have no input compound")
	
	try:
		compounds = compare_compounds_service.get_compounds(req)
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
	
	return compounds