const Kue = require('kue')
const push_notification_code_2 = Kue.createQueue()

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

jobs.forEach((job) => {
    const doJob = push_notification_code_2.create('Job2', job)
    doJob.on('enqueue', () => {
        console.log('Notification job created:', doJob.id);
    })

    doJob.on('completed', () => {
        console.log(`Notification job ${doJob.id} completed`)
        this.remove(); //remove completed job from queue
    });

    doJob.on('failed', (err) => {
        console.log(`Notification job ${doJob.id} failed:`, err)
        // this.remove() //remove failed job from queue
    });

    doJob.on('progress', (progress) => console.log(`Notification job ${doJob.id} ${progress}% complete`));

    doJob.save()
});
