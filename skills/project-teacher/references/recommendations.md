# Recommendations: skills and free tools

Use this list to recommend things before the user asks. Recommend only what fits the current project and step: at most 3 skills and 4 free tools at a time, each with one line on why it helps now.

Every entry below was checked to exist (November 2026). Install commands are copied from each project's own README. Do not recommend a skill or tool that is not on this list unless you verified it in this session (for example with a web search), and say that you verified it.

## How to recommend safely

- Name the official source (the GitHub repository) and install only from there. Copies under other names exist.
- Tell the user a skill is a set of instructions Claude follows, and suggest they read its `SKILL.md` before installing.
- Free tiers change. Say "free tier as of late 2026, check the pricing page" and name the main limit you know of.
- A recommendation is a suggestion. Never install anything without the user's yes.

## Claude skills on GitHub

| Skill | Source | Recommend when | Install (Claude Code) |
|---|---|---|---|
| **Ponytail** | `DietrichGebert/ponytail` | Any coding project, to keep code small and avoid over-building. Its `/ponytail-review` checks each finished step. | `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail` |
| **Superpowers** | `obra/superpowers` | Bigger projects. Its `brainstorming` skill shapes ideas before building, `systematic-debugging` finds the cause of bugs, `test-driven-development` adds tests first. | `/plugin install superpowers@claude-plugins-official`, or `/plugin marketplace add obra/superpowers-marketplace` then `/plugin install superpowers@superpowers-marketplace` |
| **Anthropic example skills** | `anthropics/skills` | `frontend-design` for a page that looks intentional; `webapp-testing` to test a local web app in a real browser; `mcp-builder` to connect Claude to a tool or API. | `/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills` |
| **Graphify** | `Graphify-Labs/graphify` | Explaining a large or unfamiliar existing codebase: builds a map of how files connect. | `pip install graphifyy` then `graphify install` (the package name has two y's) |

## Free tools by need

| Need | Free option | Main limit to mention |
|---|---|---|
| Code storage and history | GitHub (public and private repositories) | Large files need Git LFS |
| Host a static website | GitHub Pages, Netlify, Vercel (Hobby), Cloudflare Pages | Static files only on GitHub Pages; Vercel Hobby is for non-commercial use |
| Database and sign-in | Supabase (free tier), Firebase (Spark plan) | Supabase pauses inactive free projects; both cap storage and usage |
| Local database | SQLite | One machine; not for many simultaneous writers |
| Notebooks and GPU for ML | Google Colab, Kaggle Notebooks | Session time limits; GPU not always available |
| Models and demo hosting | Hugging Face Hub and Spaces (free CPU) | Free Spaces sleep when idle; GPU costs money |
| Mobile app toolkit | Expo (React Native), Flutter | App-store publishing has its own fees |
| Game engine | Godot | None for learning; it is open source |
| Hardware simulator | Wokwi (Arduino, ESP32 in the browser) | Some advanced features are paid |
| Code editor | Visual Studio Code | None |

## What to recommend at each stage

- **Shaping the idea:** Superpowers `brainstorming`, if the idea is still vague.
- **Before the first line of code:** GitHub for the code's history; Ponytail to keep the first version small.
- **When the interface goes in:** Anthropic `frontend-design` for looks; `webapp-testing` to check it in a browser.
- **When saved data or sign-in comes up:** Supabase or Firebase, with their access rules on from the start.
- **When something breaks:** Superpowers `systematic-debugging`.
- **When it is ready to share:** a free host from the table, matched to the project type.
- **Learning an existing codebase:** Graphify for the map, then this skill to explain the concepts.
