from fastapi import APIRouter, HTTPException
from app.models.project_model import (
	ProjectCreateRequest,
	ProjectResponse,
	ProjectResultsResponse,
	AddCompoundsRequest
)
from app.services import project_service

router = APIRouter(prefix="/projects", tags=["projects"])



@router.post("/newProject", respone_model=ProjectResponse)
def create_project_endpoint(req: ProjectCreateRequest) -> ProjectResponse:

	name = req.name.strip()
	if not name:
		raise HTTPException(status_code=400, detail="Project name cannot be empty")
	
	try:
		project = project_service.create_project(
			name=name,
		)
	except project_service.ProjectNameTakenError:
		raise HTTPException(status_code=409, detail="Project name already used")
	
	return ProjectResponse(
		project_id=project.id,
		name=project.name,
	)




@router.post("/{project_id}/addCompounds", respone_model=ProjectResultsResponse)
def add_compounds_endpoint(
	project_id: str, 
	req: AddCompoundsRequest
) -> ProjectResultsResponse:

	if not req.compounds:
		raise HTTPException(status_code=400, detail="Compounds list cannot be empty")
	
	try:
		project = project_service.add_compounds(
			project_id=project_id,
			compounds=req.compounds,
		)
	except project_service.ProjectNotFoundError:
		raise HTTPException(status_code=404, detail="Project not found")
	
	return ProjectResultsResponse(
		project_id=project.id,
		name=project.name,
		inputs=req.compounds,
		results=project.results,
	)



@router.get("/{project_id}/results", response_model=ProjectResultsResponse)
def get_project_results_endpoint(project_id: str) -> ProjectResultsResponse:
	
	try:
		project = project_service.get_project_with_results(project_id)
	except project_service.ProjectNotFoundError:
		raise HTTPException(status_code=404, detail="Project not found")
	
	return ProjectResultsResponse(
		project_id=project.id,
		name=project.name,
		inputs=project.inputs,
		results=project.results,
	)