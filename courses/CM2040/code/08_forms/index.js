const express = require('express')
const app = express()
const port = 8000

app.use(express.static(__dirname + '/public'))

app.set('views', __dirname + '/views')
app.set('view engine', 'ejs')

const mainRoutes = require('./routes/main')
app.use('/', mainRoutes)

app.get('*', (req, res) => {
    res.status(404).send('page not found')
})

app.listen(port, () => {
    console.log(`server listening on port ${port}`)
})
