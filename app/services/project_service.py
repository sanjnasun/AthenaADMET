from app.models.project_model import (
	ProjectResponse, 
	ProjectCreateRequest, 
	AddCompoundsRequest, 
	ProjectCreateResponse,
)

def create_project(req: ProjectCreateRequest) -> ProjectCreateResponse:
	return

def add_compounds(req: AddCompoundsRequest) -> ProjectResponse:
	return

def get_project_with_results(project_id: str) -> ProjectResponse:
	return