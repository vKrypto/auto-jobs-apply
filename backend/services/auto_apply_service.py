from services.job_scraper_service import job_scraper_service
from services.ai_service import ai_service
from services.application_service import application_service
from repositories.preferences_repository import preferences_repository
from repositories.application_repository import application_repository
from config.logger import logger

class AutoApplyService:
    async def execute_auto_apply(self, preferences):
        logger.info("Starting auto-apply process...")
        logger.debug(f"User preferences: {preferences}")
        
        # TODO: Add orchestration logic
        # - Validate preferences
        # - Handle errors at each step
        # - Add retry logic for failed steps
        # - Track progress and status
        # - Send notifications at each step
        # - Support batch processing multiple jobs
        # - Rate limiting and throttling
        
        # Step 1: Scrape jobs
        logger.info("Step 1: Scraping jobs...")
        jobs = await job_scraper_service.scrape_jobs(preferences)
        if not jobs:
            logger.warning("No jobs found")
            raise Exception("No jobs found")
        logger.info(f"Found {len(jobs)} jobs")

        # Step 2: AI selects best job
        logger.info("Step 2: AI selecting best job...")
        selected_job = await ai_service.select_best_job(jobs, preferences)
        logger.info(f"Selected: {selected_job.title} at {selected_job.company}")

        # Step 3: AI generates cover letter
        logger.info("Step 3: Generating cover letter...")
        cover_letter = await ai_service.generate_cover_letter(selected_job, preferences)
        logger.info("Cover letter generated")

        # Step 4: Apply to job
        logger.info("Step 4: Applying to job...")
        application = await application_service.apply_to_job(selected_job, cover_letter)
        logger.info(f"Application {'successful' if application.success else 'failed'}")

        # Step 5: Save to repositories
        logger.info("Step 5: Saving to database...")
        preferences_repository.save("user1", preferences)
        application_repository.save(application.to_dict())
        logger.info("Data saved")
        
        logger.info("Auto-apply process completed!")
        
        return {
            "application": application,
            "selected_job": selected_job,
            "cover_letter": cover_letter
        }

auto_apply_service = AutoApplyService()
