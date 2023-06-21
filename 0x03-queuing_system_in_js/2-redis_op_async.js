import { createClient } from "redis";
var redis = require('redis')
const { promisify } = require('util')
const client = createClient()

const getAsync = promisify(client.get).bind(client)

client.on('error', (err) =>
    console.log('Redis client not connected to the server:', err)
)

client.on('connect', () =>
    console.log('Redis client connected to server')
)

const setNewSchool = async (schoolName, value) => {
    await client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
    try {
        const value = await getAsync(schoolName)
        console.log(value);
    } catch (error) {
        console.error('Error:', error)
    } finally {
        client.quit()
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
