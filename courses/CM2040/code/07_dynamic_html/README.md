# 07_dynamic_html

End-of-topic-3 starter for CM2040. Reconstructed because the original lab download was lost. The next lab (`08_forms`) builds on this by adding form handling.

## What's in it
- `index.js`, Express server, registers EJS as the view engine and mounts the routes.
- `routes/main.js`, three routes: `/`, `/about` (passes a single variable), `/list-users` (passes an array iterated in the template).
- `views/`, EJS templates demonstrating both EJS tag forms (`<%= %>` for output, `<% %>` for logic).
- `public/main.css`, served as a static asset.

## Run it
```
npm install
npm start
```
Then open http://localhost:8000.

## Next, add forms
Topic 4 builds on this by adding `app.use(express.urlencoded({ extended: true }))`, a `GET` route that renders a form, and a `POST` route that consumes `req.body`.
