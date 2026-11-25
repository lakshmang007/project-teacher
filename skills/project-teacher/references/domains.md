# Domain expert notes

Read only the section for the user's project type. Each section says how an expert in that field would guide a beginner: the stack to start with, what to do from day one, the mistakes beginners make, and what a good "done when" looks like.

Contents: [Website](#website) · [Web app with accounts or saved data](#web-app-with-accounts-or-saved-data) · [Mobile app](#mobile-app) · [API or backend](#api-or-backend) · [Data analysis or machine learning](#data-analysis-or-machine-learning) · [Automation script or bot](#automation-script-or-bot) · [Game](#game) · [Hardware or IoT](#hardware-or-iot)

If the project fits none of these, act as the expert yourself: name the field, its usual beginner stack, and its top three mistakes, and say that this part is your own judgment.

---

## Website

- **Start with:** plain HTML, CSS and JavaScript in one or a few files. No framework until the site has several pages that share parts.
- **From day one:** a `<meta name="viewport">` tag for phones, labels on every input, readable text contrast, image `alt` text.
- **Beginner mistakes:** reaching for a framework for a one-page site; layout that breaks on phones; copying code without knowing which file it belongs in.
- **Good done-when:** "Open the page on a phone-width window: nothing scrolls sideways."
- **Share it free:** GitHub Pages, Netlify, Vercel or Cloudflare Pages (see recommendations.md).

## Web app with accounts or saved data

- **Start with:** the website stack, plus a hosted database with built-in sign-in (for example Supabase or Firebase) instead of writing your own login.
- **From day one:** never put secret keys in front-end code; turn on the database's access rules (row-level security or security rules) before real users sign up; check every input on the server, not just in the browser.
- **Beginner mistakes:** storing passwords yourself; leaving the database open to anyone; keeping keys in a public GitHub repo.
- **Good done-when:** "Signed out, I cannot see or change anyone's data, even by typing the address directly."

## Mobile app

- **Start with:** a cross-platform toolkit (Expo for React Native, or Flutter) so one codebase runs on Android and iPhone. Test on your own phone with the toolkit's preview app.
- **From day one:** big enough tap targets, text that scales with the phone's font setting, working with no internet (show a clear message).
- **Beginner mistakes:** starting with app-store publishing; building for one screen size only; too many screens before one works.
- **Good done-when:** "On my own phone, I can complete the main task with one hand."

## API or backend

- **Start with:** one small server in a language the user knows (Python with FastAPI or Flask, or Node with Express). SQLite for data until it outgrows one machine.
- **From day one:** validate every input; return clear error messages; keep secrets in environment variables, not in code.
- **Beginner mistakes:** no input checks; building many endpoints before one works end to end; testing only the happy path.
- **Good done-when:** "Sending a wrong or empty request returns a clear error, not a crash."

## Data analysis or machine learning

- **Start with:** a notebook (Jupyter, or Google Colab for free compute) with pandas and a plot. Try a simple baseline before any complex model.
- **From day one:** look at the raw data first; keep a test set the model never trains on; write down where the data came from.
- **Beginner mistakes:** training before cleaning the data; judging a model on its training data; using a big model where a simple rule works.
- **Good done-when:** "The model beats a simple baseline on data it has never seen, and I can say by how much."

## Automation script or bot

- **Start with:** one Python script that does the job once, by hand-run, before any scheduling or hosting.
- **From day one:** a dry-run mode that shows what it would do without doing it; logging of each action; respecting the rate limits and terms of any site or API it uses.
- **Beginner mistakes:** running destructive actions without a dry run; hard-coding passwords; scraping sites that forbid it.
- **Good done-when:** "Dry run lists the exact actions; the real run does exactly those and nothing else."

## Game

- **Start with:** a free engine sized to the idea: plain JavaScript canvas for a tiny browser game, Godot for anything bigger. One playable level before menus or art.
- **From day one:** the core loop (the thing the player repeats) must be fun with boxes as graphics; keyboard and controller support if it is a desktop game.
- **Beginner mistakes:** making art, menus and save systems before the game is fun; too-large scope (an "MMO" as a first game).
- **Good done-when:** "A friend plays one level for two minutes without being told what to do."

## Hardware or IoT

- **Start with:** an Arduino or ESP32 board, and a free simulator (Wokwi) to test the circuit before wiring real parts.
- **From day one:** check voltage and current limits before connecting anything; one sensor or one output working at a time.
- **Beginner mistakes:** wiring everything at once; powering motors straight from the board; no plan for what happens when Wi-Fi drops.
- **Good done-when:** "The sensor reading on screen changes when I change the real thing it measures."
