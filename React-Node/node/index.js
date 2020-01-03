const server = require('./server')

const port = 9000

// server.get('/', (req,res) => {
//     res.send('this is the Node side of the Django vs React App')
// })

server.listen(port, () => {
    console.log('server listening on port ', port)
})

