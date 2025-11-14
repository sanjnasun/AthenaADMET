from fastapi import APIRouter, HTTPException
from app.models.project_model import (
	ProjectCreateRequest,
	ProjectResponse,
	ProjectCreateResponse,
	AddCompoundsRequest
)
from app.services import project_service

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/newProject", response_model=ProjectCreateResponse)
def create_project_endpoint(req: ProjectCreateRequest) -> ProjectCreateResponse:

	try:
		project = project_service.create_project(req)
		return project
	except project_service.ProjectNameTakenError:
		raise HTTPException(status_code=409, detail="Project name already used")
	


@router.post("/addCompounds", response_model=ProjectResponse)
def add_compounds_to_project_endpoint(req: AddCompoundsRequest) -> ProjectResponse:

	try:
		project = project_service.add_compounds(req)
		return project
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Error saving results: {str(e)}")


@router.get("/{project_id}/results", response_model=ProjectResponse)
def get_project_results_endpoint(project_id: str) -> ProjectResponse:
	
	try:
		project = project_service.get_project_with_results(project_id)
		return project
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Error finding project: {str(e)}")
