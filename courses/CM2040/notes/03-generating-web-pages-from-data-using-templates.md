# Topic 3: Generating Web Pages from Data Using Templates

> CM2040 · Week 5, Topic 3 · 3 lectures
> Source transcripts: `notes/transcripts/03-generating-web-pages-from-data-using-templates/` (local, gitignored)

## TL;DR
Once your routes get past "Hello World", embedding HTML strings inside route handlers stops scaling. Move HTML into `views/`, render it from a route, and (most importantly) use a **templating engine** so you can inject server-side data into the page at render time. In this course the engine is **EJS** (Embedded JavaScript). The whole point: bridge the gap between data in the middleware and presentation in the browser, giving you genuine **data-driven web applications**.

## Why move HTML out of route handlers

Up to topic 2, route handlers looked like:

```javascript
app.get('/about', (req, res) => {
  res.send('<h1>About</h1><p>...</p>')   // embedded HTML string
})
```

That breaks down as HTML grows. The [[separation-of-concerns]] fix:
- Put HTML in `views/`.
- Route handlers just **render** a view.
- Express finds the view file and (with a template engine) injects data.

```javascript
// routes/main.js
router.get('/', (req, res) => {
  res.render('index', { title: 'Home' })
})
```

Wire EJS in once during app setup:
```javascript
npm install ejs
app.set('view engine', 'ejs')
```

## Templating engines ([[templating-engine]])

A **template engine** does two things:

1. **Variable interpolation**, replaces placeholders in a template with runtime values (e.g. data fetched from a DB).
2. **Embedded logic**, lets you run small bits of programming logic (loops, conditionals) before the final HTML is sent.

The flow: static template file (with placeholders) + JS data → engine combines them at render time → final HTML → sent to client.

### Why this matters for dynamic apps
Without a template engine, the only way to vary content per request is to manually concatenate strings. With one, you keep HTML clean and let data drive what users see, the foundation of every data-driven app you'll build later in this module.

### Popular engines for Express/Node

| Engine | Style | Notes |
|---|---|---|
| **EJS** (Embedded JavaScript) | HTML-with-tags | What this module uses. Simple, looks like HTML. |
| **Pug** (formerly Jade) | Whitespace/indent-sensitive (Python-like) | Clean, no closing tags. Polarising: love it or hate it. |
| **Mustache** | Logic-less templates | Minimal embedded logic by design. |

> Keep logic in templates to an **absolute minimum**. The view's job is presentation. Heavy logic belongs in middleware. This is SoC again.

## EJS in practice ([[ejs]])

Rename your `.html` files to `.ejs` and store them in `views/`. Two tag forms to remember:

| Tag | Behaviour | Use when... |
|---|---|---|
| `<%= expression %>` | Evaluates and **outputs** the value into the document | Inserting a variable: `<title><%= title %></title>` |
| `<% statement %>` | Evaluates but does **not** output | Declaring vars, loops, conditionals |

### Example: rendering a list

```javascript
// routes/main.js
router.get('/books', (req, res) => {
  const books = [
    { title: 'Hyperion',     author: 'Dan Simmons' },
    { title: 'The Dispossessed', author: 'Ursula K. Le Guin' },
  ]
  res.render('books', { books })
})
```

```html
<!-- views/books.ejs -->
<ul>
  <% books.forEach(b => { %>
    <li><strong><%= b.title %></strong> by <%= b.author %></li>
  <% }) %>
</ul>
```

The route hands `books` to the template; the template loops with `<% %>` (no output) and emits per-item HTML with `<%= %>` (output).

## How dynamic rendering works end-to-end

```
client request --> Express route handler
                    |
                    | builds JS data object (e.g. { title, books })
                    v
                  res.render('view', data)
                    |
                    | EJS template engine
                    | reads views/view.ejs
                    | substitutes <%= %> with data values
                    | runs <% %> control flow
                    v
                  final HTML
                    |
                    v
                  HTTP response to client
```

Change the JS data, the rendered page changes. That's data-driven web.

## Common pitfalls / exam fodder
- Mixing up `<%= %>` (outputs) and `<% %>` (doesn't output). Forgetting the `=` is the classic bug: code runs but the page is blank where the value should be.
- Putting heavy business logic in `.ejs` files, that's the [[separation-of-concerns]] violation, move it to middleware.
- Forgetting `app.set('view engine', 'ejs')`, or putting templates outside `views/`, Express won't find them.
- Choosing an engine arbitrarily, each has a different syntax philosophy (Pug strips closing tags; Mustache is logic-less by design). Pick what matches the team's preference.

## Lab artefacts
Programming activities for this topic are PDFs under `courses/CM2040/practice/programming-activities/03-generating-web-pages-from-data-using-templates/` (local, gitignored):
- `01-adding-html-to-your-express-server.pdf`
- `02-adding-dynamic-html-to-your-express-server.pdf`

## Related concepts (KB stubs)
- [[templating-engine]], [[ejs]]
- [[separation-of-concerns]]
- [[express]], [[express-routing]]
- [[data-driven-web-application]] (TODO)
- [[mvc-pattern]] (TODO)
