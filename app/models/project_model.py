from .input_compound_model import SmilesUploadResponse

class ProjectCreateRequest():
	name: str

class AddCompoundsRequest():
	project_id: str
	compounds: SmilesUploadResponse

class ProjectResponse():
	project_id: str
	name: str
	compounds: SmilesUploadResponse

class ProjectCreateResponse():
	project_id: str
	name: str