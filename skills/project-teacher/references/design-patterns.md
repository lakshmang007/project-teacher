# Design pattern: how to build any project step by step

Use this order for every project, new or existing. Each step must be finished and checked before the next one starts. Skipping a step is how beginners get stuck.

## The 8 steps

1. **Problem and user.** Write one sentence: "This helps [who] do [what]."
   - Done when: a non-technical friend could repeat the sentence back.
2. **Inputs and outputs.** List what goes in (typed text, a file, a click) and what comes out (a screen, a file, a number).
   - Done when: you can draw an arrow from each input to each output.
3. **Data shape.** Write down the pieces of information the project stores, one line each (for example: a task has a title, a done flag, a date).
   - Done when: every output can be built from these pieces.
4. **Smallest working version.** Build only the path from input to output for one example. No login, no styling, no extras.
   - Done when: the example works from start to finish, even if it looks plain.
5. **Interface.** Add the way a person uses it (screen, command, button). Keep the layout simple. Make it usable by everyone from the start: every input and checkbox has a label, every button says what it does, and everything works with the keyboard alone.
   - Done when: the person can complete the example without help, using only the keyboard.
6. **Logic and rules.** Add the rules for edge cases: empty input, wrong input, the first and last item.
   - Done when: each rule has one test that fails if the rule breaks.
7. **Test with real examples.** Run it with three real inputs, including one that should fail.
   - Done when: the outputs match what you expected, and the failure shows a clear message.
8. **Polish and share.** Improve the look, write a short README, then share it.
   - Done when: someone else can run it using only the README.

## Rules that apply to every step

- **One change at a time.** If a change breaks something, you know which change did it.
- **Reuse before you write.** Check whether the project, the language, or the platform already does the job.
- **Simplest first.** Add a feature only when a real example needs it.
- **Test the important parts.** Money, security, saving data, and anything with branches need a check that fails when the logic breaks.
- **Never cut accessibility.** Labels, clear button names and keyboard use are part of "working", not polish.

## Applying the pattern to an existing project

1. Map the project to the 8 steps: which step does it already have, which is missing?
2. Name the first missing step. That step becomes the next checklist item.
3. Do not rewrite finished steps unless they fail their "done when" test.
