async def run_task_pipeline():
    pipeline = [
        {"$match": {"eventType": {"$in": ["sip-trial-course-record"]}, "isProcess": False}},
        {"$project": {"_id": 0}}
    ]
    data = MongoDB.get_many(p.MONGODB_COLL_KAFKA, pipeline)
    tasks = []
    for event in data:
        logger.debug(f"Process {event.get('eventType')} tasker... {event.get('eventId')}")
        task = consultant_invitation_voice_quality_inspection(event)
        tasks.append(task)
        if len(tasks) >= p.MAX_WORKERS:
            await asyncio.gather(*tasks)
            tasks = []
    if tasks:
        await asyncio.gather(*tasks)