from services.auto_apply_service import auto_apply_service
from repositories.application_repository import application_repository

class AutoApplyController:
    async def auto_apply(self, preferences):
        # TODO: Add request validation
        # - Validate preferences structure
        # - Check required fields
        # - Handle validation errors
        
        if not preferences:
            return {
                "success": False,
                "message": "Preferences are required"
            }
        
        try:
            result = await auto_apply_service.execute_auto_apply(preferences)
            
            return {
                "success": result["application"].success,
                "message": "Successfully applied!" if result["application"].success else "Application failed",
                "jobTitle": result["selected_job"].title,
                "company": result["selected_job"].company,
                "applicationId": result["application"].application_id
            }
        except Exception as error:
            return {
                "success": False,
                "message": str(error) or "Internal server error"
            }

    async def get_history(self):
        # TODO: Add pagination
        # - Add limit and offset parameters
        # - Add sorting options
        # - Handle errors
        
        try:
            history = application_repository.get_all()
            return {
                "success": True,
                "history": [app.to_dict() if hasattr(app, 'to_dict') else app for app in history]
            }
        except Exception as error:
            return {
                "success": False,
                "message": str(error) or "Internal server error"
            }

auto_apply_controller = AutoApplyController()

