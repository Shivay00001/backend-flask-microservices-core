from celery import shared_task
import time

@shared_task
def example_task(user_id):
    """
    Example background task that simulates work.
    """
    print(f"Starting background task for user {user_id}")
    time.sleep(5)
    print(f"Finished background task for user {user_id}")
    return True
