// 6-job_creator

const kue = require('kue');
const cq = kue.createQueue();

const obj = cq.create('push_notification_code', {
    phoneNumber: '1234567890',
    message: 'This is a message',
})
.save();

obj.on('enqueue', () => {
    console.log(`Notification job created: ${obj.id}`);
})
obj.on('complete', () => {
    console.log('Notification job completed');
  })
obj.on('failed', () => {
    console.log('Notification job failed');
  });
