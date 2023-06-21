import { createClient } from "redis";
var redis = require('redis')

const client = createClient()

client.on('error', (err) =>
    console.log('Redis client not connected to the server:', err)
)

client.on('connect', () =>
    console.log('Redis client connected to server')
)

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (error, value) => {
        if (error) {
          console.error('Error:', error);
        }else {
            console.log(value);
        }
    });
    client.quit()
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
