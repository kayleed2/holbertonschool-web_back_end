//Connect to redis server

const redis = require('redis');
import { createClient } from 'redis';
const { promisify } = require('util');

const client = createClient();

    client.on('connect', () => {
        console.log('Redis client connected to the server');
    })
    client.on('error', (err) => {
        console.log('Redis client not connected to the server: ', err);
    });

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
    console.log(await promisify(client.get).bind(client)(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
