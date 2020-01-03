const express = require('express')
const server = express()
server.use(express.json())

server.get('/', (req,res) => {
    // res.status(200).json({message : 'this is the node side of the django-vs-react database'})
    res.send('welcome to the node side of Django vs React-Node')
})

module.exports = server