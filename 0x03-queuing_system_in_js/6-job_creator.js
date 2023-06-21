var kue = require('kue')
const push_notification_code = kue.createQueue();

const jobData = {
    phoneNumber: '203-456-9090',
    message: 'Create job using Kue',
}

const job = push_notification_code
.create('jobData', jobData)
.save((err) => {
    if (!err) {
        console.log('Notification job created:', job.id);
    }
})

job.on('completed',  () => {
    console.log('Notification job completed');
})

job.on('failed',  () => {
    console.log('Notification job failed');
})