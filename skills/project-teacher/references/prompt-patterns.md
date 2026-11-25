# Prompt patterns for building step by step

A good build prompt is small, specific, and ends with a check. Copy a template, fill in the blanks, and run one prompt at a time.

## Template 1: Build one step

```
Build only this step: [one feature in one sentence].
Change only [file name].
Do not add [things to avoid, e.g. login, styling, extra options].
When done, tell me in 3 lines what you changed and how I can test it.
```

## Template 2: Explain before changing

```
Read [file name] and explain in plain words what [function or section] does.
Do not change any code yet.
```

## Template 3: Simplify

```
Here is [file name]. Rewrite [function] with less code and no new libraries.
Keep the same behaviour and tell me what you removed.
```

## Template 4: Add a test

```
Write one small test for [rule]. It should pass now and fail if I change [rule] to something wrong.
Tell me the command to run it.
```

## Template 5: Fix an error

```
I got this error when I ran [command]:
[paste the full error]
Find the cause, fix it with the smallest change, and explain the cause in two sentences.
```

## Template 6: Plan before building

```
I want to build: [idea in one sentence]. I am a [experience level].
Give me the smallest version that works, the 8 steps for it, and one check per step.
Do not write any code yet.
```

## Why these work

- They name one file, so the change stays small.
- They say what to leave out, so the tool does not add extras.
- They end with a check, so you know when the step is done.
- Template 2 and 6 ask for explanation with no code changes, which is a safe way to learn.
