# Topic 2: Building Web Apps with Node and Express

> CM2040 · Weeks 2-4, Topic 2 · 9 lectures
> Source transcripts: `notes/transcripts/02-building-web-apps-with-node-and-express/` (local, gitignored)

## TL;DR
**Node.js** is an asynchronous, event-driven JavaScript runtime that lets you write server-side code in JavaScript. A **web server** is software that listens for HTTP requests and returns resources. **Express** is a lightweight framework on top of Node for building HTTP servers with **routes**. The big design principle running through the topic is **separation of concerns (SoC)**: split the app into independent, loosely-coupled pieces (router files, view folders, etc.).

## Web server fundamentals ([[web-server]])

A **web server** is a program (or the box it runs on) that:
- Uses **HTTP** to respond to client requests for resources.
- Runs continuously, listening on a network port.
- Returns the requested resource, or invokes a program (e.g. a database query) that produces one.

HTTP was invented by Tim Berners-Lee and Robert Cailliau (1990), as part of the World Wide Web project.

### Architecture of a web server
Minimum elements:
1. **Hardware**, anything from a Raspberry Pi to a rack of dedicated servers. You can rent it (web hosting: virtual private servers, cloud, dedicated).
2. **Operating system**, allocates resources, mediates between hardware and software. Linux, Windows, macOS-based variants.
3. **HTTP server**, compiles output from scripts/database into HTML and serves it. Configuration files control what's exposed.

Optional but typical:
4. **Database**, persistent storage.
5. **Scripting language**, the server-side code that generates dynamic content.

## Node.js ([[node-js]])

**Definition**: an open-source, cross-platform **JavaScript runtime environment**, executes JavaScript code outside the browser. Created by Ryan Dahl in 2009. Not a language, not a framework.

### Key properties

| Property | What it means | Consequence |
|---|---|---|
| Asynchronous | Doesn't wait for slow operations to finish before handling the next request | High concurrency |
| Event-driven | Flow controlled by events (mouse, message, I/O complete), not strict sequence | Reactive programming model |
| Single-threaded | One thread serves multiple requests | Low memory overhead |
| Non-blocking I/O | Slow I/O (DB, network, disk) doesn't block the thread | Highly scalable |

### Async vs synchronous, why it matters
**Synchronous** (e.g. classic PHP): each request gets its own thread; that thread blocks while the DB does its work; new requests need new threads.

**Asynchronous** (Node.js): the thread fires the DB query and **moves on** to the next request. When the DB returns, the server sends the response. One thread serves many in-flight requests.

```
PHP / synchronous            Node / asynchronous
  req1 -> wait -> reply         req1 -> (waiting on DB)
  req2 -> wait -> reply           req2 -> (waiting on DB)
  req3 -> wait -> reply             req3 -> (waiting on DB)
                                  reply when DB returns, any order
```

### When to use (and not use) Node.js
| Use Node for... | Avoid Node for... |
|---|---|
| I/O-intensive apps (lots of disk, DB, network reads/writes) | CPU-intensive workloads (video encoding, image manipulation) |
| E-commerce, real-time apps | Use multi-threaded runtimes for those |

Bonus: same language (JavaScript) on client and server, so code can be shared.

## Express ([[express]])

A lightweight web framework **on top of Node.js**. The whole module's web apps will be built on it. Adds routing, middleware, request/response helpers.

### Minimal app skeleton (the lab pattern)

```javascript
const express = require('express')   // import the module
const app = express()                // create the app object
const port = 8081                    // pick a port

app.get('/', (req, res) => {         // route handler for "/"
  res.send('hello world')
})

app.get('/about', (req, res) => {    // route handler for "/about"
  res.send('<h1>About</h1>')
})

app.listen(port, () => {
  console.log(`Listening on ${port}`)
})
```

Flow when a request arrives:
1. Express receives the HTTP request.
2. Walks through the registered route handlers in order.
3. Runs the first one whose path matches.
4. The handler's function returns a response to the client.

### Response anatomy
Even a one-line `res.send('hello world')` actually sets:
- **Status code** (e.g. 200 OK)
- **Content-Type** (e.g. `text/plain`)
- **Body** (the actual text/HTML/JSON)

You can see all three in the browser's DevTools → Network tab. The browser only renders the body, but the metadata is just as much "the response".

## Routes ([[express-routing]])

A **route** = path + HTTP method + handler function. Express matches incoming requests against the registered routes in order; first match wins.

Once you have more than a handful of routes, cramming them all into `index.js` gets messy. Move them to a separate file (e.g. `routes/main.js`):

```javascript
// routes/main.js
const express = require('express')
const router = express.Router()

router.get('/', (req, res) => res.send('home'))
router.get('/about', (req, res) => res.send('about'))

module.exports = router
```

```javascript
// index.js
const mainRoutes = require('./routes/main')
app.use('/', mainRoutes)             // mount at root

const userRoutes = require('./routes/user')
app.use('/user', userRoutes)         // mount at /user
```

Mount paths are **concatenated** with the router's own paths: a `router.get('/login')` mounted at `/user` responds to `GET /user/login`.

## Separation of concerns (SoC) ([[separation-of-concerns]])

> Each module or layer should be responsible for **one thing** and should not contain code that deals with other things.

### Achieving SoC
- **Modularity**, build the app from small modules with one job each.
- **Encapsulation**, hide internal details, expose well-defined interfaces.
- **Layering**, e.g. three-tier architecture, or MVC (model/view/controller).
- **Loose coupling**, modules talk via interfaces, dependencies minimised (not eliminated, you can't remove all dependencies; just reduce them).

### Benefits

| Benefit | Why it matters |
|---|---|
| Reduced complexity | Big problem broken into small, encapsulated pieces |
| Supports DRY | Easier to find and reuse logic instead of duplicating |
| Portability | Concerns are independent; swap a piece (e.g. DB) without rewriting others |
| Maintainability + testability | Smaller units are easier to test and bug-fix |

### SoC in this course's app structure
- `index.js`, app entry, wires everything together.
- `routes/`, route handlers grouped per concern (`main.js`, `user.js`, ...).
- `views/`, HTML / EJS templates (see Topic 3).
- (Later in the course: `models/` or DB-access code as its own layer.)

## Common pitfalls / exam fodder
- Calling Node.js a "language" or a "framework". It's a **runtime environment**.
- Conflating asynchronous with multi-threaded. Node is async but **single-threaded**.
- Using Node for CPU-bound work, you get no scalability benefit.
- Adding routes inline in `index.js` forever. Split into router files early.
- Confusing **SoC** with completely independent modules. Loose coupling, not zero coupling.

## Related concepts (KB stubs)
- [[node-js]], [[express]], [[express-routing]]
- [[asynchronous-vs-synchronous]]
- [[event-driven-programming]]
- [[separation-of-concerns]]
- [[web-server]], [[http]]
- [[mvc-pattern]] (TODO)
