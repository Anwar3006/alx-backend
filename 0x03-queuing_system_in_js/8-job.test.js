import sinon from 'sinon';
const { expect } = require('chai');
const { createQueue } = require('kue');
const createPushNotificationsJobs = require('./8-job.js');

describe('createPushNotificationsJobs', () => {
  const BIG_BROTHER = sinon.spy(console);
  const QUEUE = createQueue({ name: 'push_notification_code_test' });

  before(() => {
    QUEUE.testMode.enter();
  });

  after(() => {
      QUEUE.testMode.exit();
    });
    
    afterEach(() => {
      QUEUE.testMode.clear();
  });

  it('displays an error message if jobs is not an array', () => {
    expect(
      createPushNotificationsJobs.bind(createPushNotificationsJobs, {}, QUEUE)
    ).to.throw('Jobs is not an array');
  });

  it('adds jobs to the queue with the correct type', (done) => {
    expect(QUEUE.testMode.jobs.length).to.equal(0);
    const jobInfos = [
      {
        phoneNumber: '44556677889',
        message: 'Use the code 1982 to verify your account',
      },
      {
        phoneNumber: '98877665544',
        message: 'Use the code 1738 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobInfos, QUEUE);
    expect(QUEUE.testMode.jobs.length).to.equal(2);
    expect(QUEUE.testMode.jobs[0].data).to.deep.equal(jobInfos[0]);
    expect(QUEUE.testMode.jobs[0].type).to.equal('push_notification_code_3');
    QUEUE.testMode.jobs.forEach(job => {
        BIG_BROTHER.log('Notification job created:', job.id)
    });
    done();
    })
})