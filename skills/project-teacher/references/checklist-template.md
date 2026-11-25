# Build checklist template

Copy this structure into the checklist file. Replace the bracketed text. Keep one item per step, and do not tick an item until its "Done when" check passes.

```markdown
# Build checklist: [project name]

**Goal:** [one sentence]
**Experience level:** [never coded / some code / experienced]
**Language or platform:** [chosen language, or "to decide in step 1"]
**Time per session:** [e.g. 30 minutes]

## Step 1: [name]
- [ ] **Goal:** [what this step produces]
- **Prompt to use:** "[paste a prompt from prompt-patterns.md, filled in]"
- **Done when:** [one observable check, e.g. "running the program prints the list of three tasks"]
- **Concept:** [one term this step teaches, e.g. "function"]

## Step 2: [name]
- [ ] **Goal:** ...
- **Prompt to use:** "..."
- **Done when:** ...
- **Concept:** ...

(repeat for 5 to 12 steps)

## After the build
- [ ] Run the project with three real examples, including one that should fail.
- [ ] If it has a user interface: use it with the keyboard alone, and check every input and button has a clear name.
- [ ] Write a README a friend could follow.
- [ ] Note one thing you would change next time.
```

## Rules for filling it in

- Each step should take one sitting. If it takes longer, split it.
- The "Done when" line must be something the user can observe without reading the code.
- Write the "Concept" line only for terms the step actually uses.
