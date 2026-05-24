const express = require('express')
const router = express.Router()

router.get('/', (req, res) => {
    res.render('index.ejs')
})

router.get('/about', (req, res) => {
    const title = { name: 'About this site' }
    res.render('about.ejs', title)
})

router.get('/list-users', (req, res) => {
    const users = [
        { name: 'Ada Lovelace', role: 'mathematician' },
        { name: 'Alan Turing', role: 'computer scientist' },
        { name: 'Grace Hopper', role: 'rear admiral' }
    ]
    res.render('list-users.ejs', { users: users })
})

module.exports = router
