# Build checklist: To-do list website

**Goal:** A web page where I can add tasks, tick them done, delete them, and they stay after a refresh.
**Experience level:** never coded
**Language or platform:** HTML, CSS and JavaScript in one file, opened in a browser (no install, no server code)
**Time per session:** 30 minutes

## Step 1: Empty page
- [x] **Goal:** a page with a title and an empty list.
- **Prompt to use:** "Build only this step: an index.html page with the heading 'My To-Do List' and an empty list. Change only index.html. Do not add styling or buttons yet. When done, tell me in 3 lines how to open it."
- **Done when:** opening the page shows the heading "My To-Do List".
- **Concept:** HTML

## Step 2: Add a task
- [x] **Goal:** a text box and an Add button that put the task in the list.
- **Prompt to use:** "Build only this step: add a text box and an Add button to index.html. Clicking Add puts the typed text in the list and clears the box. Change only index.html. Do not add saving yet."
- **Done when:** typing "Buy milk" and clicking Add shows "Buy milk" in the list.
- **Concept:** event

## Step 3: Tick a task done
- [x] **Goal:** a checkbox beside each task that crosses it out.
- **Prompt to use:** "Build only this step: put a checkbox beside each task in index.html. Ticking it crosses the task out; unticking restores it. Change only index.html."
- **Done when:** ticking "Buy milk" draws a line through it.
- **Concept:** DOM

## Step 4: Delete a task
- [x] **Goal:** a Delete button beside each task.
- **Prompt to use:** "Build only this step: add a Delete button beside each task in index.html that removes that task only. Change only index.html."
- **Done when:** with two tasks, deleting one leaves the other.
- **Concept:** array of objects (the data shape)

## Step 5: Remember tasks after refresh
- [x] **Goal:** tasks and their ticks survive a page refresh.
- **Prompt to use:** "Build only this step: save the task list in the browser's localStorage whenever it changes, and load it when the page opens. Change only index.html. No server or database."
- **Done when:** add two tasks, tick one, refresh: both are still there and the tick is kept.
- **Concept:** localStorage and JSON

## Step 6: Handle mistakes
- [x] **Goal:** blank tasks are ignored and Enter also adds a task.
- **Prompt to use:** "Build only this step: in index.html, ignore empty or spaces-only tasks, and let the Enter key add a task like the Add button. Change only index.html."
- **Done when:** clicking Add with an empty box adds nothing, and pressing Enter adds a typed task.
- **Concept:** validation

## Step 7: Make it tidy
- [x] **Goal:** simple, readable layout that also fits a phone screen.
- **Prompt to use:** "Build only this step: add simple CSS to index.html so the list is centred, readable and fits a phone-width screen. No libraries."
- **Done when:** the page looks tidy at full width and at phone width.
- **Concept:** CSS

## After the build
- [ ] Try three real tasks, including a blank one that should be refused.
- [ ] Write a short README a friend could follow.
- [ ] Note one thing you would change next time.
