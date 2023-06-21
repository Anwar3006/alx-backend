
const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array')
    }

    jobs.forEach((job) => {
        const createJob = queue.create('push_notification_code_3', job)
        createJob.on('enqueue', () => {
            console.log(`Notification job ${createJob.id} completed`);
        })
        createJob.on('failed', (error) => {
            console.log(`Notification job JOB_ID failed: ${error}`);
            done()
        })
        createJob.on('progress', (progress) => {
            console.log(`Notification job ${createJob.id} ${progress}% complete`);
        })
        createJob.save('completed', () => {
            console.log(`Notification job created: ${createJob.id}`);
        })
    })
}

module.exports = createPushNotificationsJobs