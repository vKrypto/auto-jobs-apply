from config.db import get_db
from config.logger import logger


class ApplicationRepository:
    def save(self, application):
        # TODO: Implement save application to database
        # - Get database connection
        # - Save application to database (table/collection)
        # - Add timestamp (server-side or client-side)
        # - Handle errors (validation, connection errors)
        # - Support different database types (SQL, NoSQL)
        db = get_db()
        if not db:
            logger.debug("Mock: Saving application (database not configured)")
            return
        logger.debug(f"Saving application: {application.get('applicationId', 'N/A')}")
        # Leave implementation empty
        pass

    def get_all(self):
        # TODO: Implement get all applications from database
        # - Get database connection
        # - Fetch all applications from database (table/collection)
        # - Convert to Application models
        # - Add sorting/pagination if needed
        # - Return list of applications
        # - Handle errors (connection errors)
        # - Support different database types (SQL, NoSQL)
        db = get_db()
        if not db:
            logger.debug("Mock: Returning empty history")
            return []
        logger.debug("Getting all applications")
        # Leave implementation empty
        return []

application_repository = ApplicationRepository()
