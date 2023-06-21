const kue = require('kue')
const push_notification_code_2 = kue.createQueue()


const blackList = ['4153518780', '4153518781']

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100)
    
    if (blackList.includes(phoneNumber)) {
        const err = new Error(`Phone number ${phoneNumber} is blacklisted`)
        done(err);
    } else {
        job.progress(50, 100)
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        setTimeout(() => {
            job.progress(100, 100);
            done();
        }, 2000);
    }
}

push_notification_code_2.process('Job2', 2, (job, done) => {
    const { phoneNumber, message } = job.data
    // job.progress(0)
    sendNotification(phoneNumber, message, job, done)
})