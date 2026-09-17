# Contributing

## Adding a module

1. Create a new Markdown file in `modules/`.
2. Add YAML frontmatter using the required fields.
3. Put the current test result in `status`.
4. Preserve useful test notes in `warning` or `notes`.
5. Submit a pull request.

The README and `data/modules.json` are generated automatically from the module files. Do not edit generated output manually.

### Frontmatter

```yaml
---
id: example-module
name: "Example Module"
category: "Other"
status: working
source: "https://example.com/project"
origin: "Community submission"
source_post: null
last_verified_by_repo: "username"
last_verified_date: "2026-09-17"
warning: "Optional compatibility note"
---
```

For a new test, include device, ROM, Android version, Temporal Root version, module version, and relevant configuration in the Markdown body.
