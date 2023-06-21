import { createClient } from "redis";
var redis = require('redis')

const HolbertonSchools = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
}

const client = createClient()

client.on('error', (err) =>
    console.log('Redis client not connected to the server:', err)
)

client.on('connect', () =>
    console.log('Redis client connected to server')
)

for (const element in HolbertonSchools){
    client.HSET(
        'HolbertonSchools',
        element,
        HolbertonSchools[element],
        redis.print
    )
}

client.HGETALL('HolbertonSchools', (err, value) => {
    if (err) console.error(err);
    console.log(value);
})
