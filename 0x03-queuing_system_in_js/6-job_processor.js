const Kue = require('kue')
const push_notification_code = Kue.createQueue()


const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

push_notification_code.process('jobData', (job, done) => {
        const { phoneNumber, message } = job.data;
        sendNotification(phoneNumber, message)

        done();
    }
)
