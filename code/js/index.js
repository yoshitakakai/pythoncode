const http = require('http')
const ctype = {'Content-Type': 'text/html;charset=utf-8'}

const svr = http.createServer(handler)
svr.listen(8081)

function handler(req, res) {
    const url = req.url
    if(url === '/' || url === '/index.html') {
        showIndexPage(req, res)
        return
    }

    if (url.substr(0, 6) === '/dice/') {
        showDicePage(req, res)
        return;
    }

    res.writeHead(404, ctype)
    res.end('404 not found')
}

function showIndexPage(req, res) {
    res.wtiteHead(200, ctype)
    const html = '<h1>サイコロページ</h1>\n' +
        '<p><a href="/dice/6">6面体サイコロ</p>' +
        '<p><a href="/dice/12">12面体サイコロ</p>'
    res.end(html)
}

function showDicePage(req,res) {
    res.writeHead(200, ctype)
    const a =req.url.split('/')
    const num = parseInt(a[2])
    const rnd = Math.floor(Math.random() * num) + 1
    res.end('<p style="front-siza:72px;">' + rnd + '</p>')
}