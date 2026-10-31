---
title: 'SynthID vs C2PA: Two Ways to Label AI Content'
description: 'SynthID embeds invisible pixel watermarks while C2PA attaches signed provenance metadata. Discover how they differ, why it matters, and how to detect both.'
pubDate: 2026-10-16
---

Two technologies come up most often when people talk about labelling AI-generated media: **SynthID** and **C2PA**. They solve the same problem in very different ways.

## SynthID: inside the content

SynthID, from Google DeepMind, embeds an invisible signal directly in the pixels, audio or text a model generates. You can't see it, and it is designed to survive common edits such as cropping, resizing and compression. Checking for it requires a dedicated detector.

## C2PA: attached to the file

C2PA (also called Content Credentials) is an open standard backed by Adobe, Microsoft, Google, OpenAI and others. It attaches a signed record to a file's metadata describing how the file was made and edited. Anyone with a compatible viewer can read it, but it is easy to lose: re-saving, screenshotting or uploading to some platforms strips it.

## Side by side

| | SynthID | C2PA |
|---|---|---|
| Where it lives | In the content | In the metadata |
| Visible? | No | Readable with a viewer |
| Survives screenshots | Designed to | No |
| Who can check it | Dedicated detector | Anyone with a C2PA viewer |
| Open standard | Text version open-sourced | Yes |

## Why many tools use both

The two approaches complement each other. C2PA carries rich, human-readable history; SynthID is a fallback that stays with the content when metadata is lost. Google, for example, applies SynthID and is also a C2PA member.

To learn more, read [What is SynthID?](/what-is-synthid/).
