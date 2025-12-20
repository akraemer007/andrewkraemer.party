# How to Modernize Your Blog - Super Easy Guide

## The Simplest Option: Use Minima Theme

Minima is clean, modern, actively maintained, and works perfectly with GitHub Pages. Here's how to update:

### Step 1: Update Your Files

1. **Replace `_config.yml`** with the new config file I created
2. **Replace `Gemfile`** with the new Gemfile

### Step 2: Clean Up Your Repository

You can delete these folders/files (they're from the old Lanyon theme):
- `_includes/`
- `_layouts/` 
- `public/`
- `_site/` (this is just build output)

Keep these:
- `_posts/` (your blog posts!)
- `about.md`
- `_config.yml` (the new one)
- `Gemfile` (the new one)
- `index.html` (but you might want to change it to index.md)

### Step 3: Update Your About Page

Change `about.md` to have this front matter:
```yaml
---
layout: page
title: About
permalink: /about/
---
```

### Step 4: Update Your Posts

Your posts in `_posts/` should have this front matter format:
```yaml
---
layout: post
title: "Your Post Title"
date: 2017-10-06
categories: personal
---
```

### Step 5: Push to GitHub

```bash
git add .
git commit -m "Modernize blog with Minima theme"
git push
```

That's it! GitHub Pages will automatically rebuild your site with the new theme.

---

## Alternative: Even Simpler Themes

If you want something even more minimal, here are other great GitHub Pages supported themes you can use by just changing one line in `_config.yml`:

- **Cayman**: `theme: jekyll-theme-cayman` - Clean landing page style
- **Minimal**: `theme: jekyll-theme-minimal` - Ultra minimal sidebar
- **Architect**: `theme: jekyll-theme-architect` - Bold headers

Just change the `theme:` line in `_config.yml` and push!

---

## Quick Reference: Writing New Posts

1. Create a new file in `_posts/` folder
2. Name it: `YYYY-MM-DD-title-of-post.md`
3. Add front matter at the top:
```yaml
---
layout: post
title: "My New Post"
date: 2025-12-20
---
```
4. Write your content in Markdown below the front matter
5. Commit and push to GitHub

---

## Troubleshooting

**Blog not updating?**
- Wait 2-3 minutes after pushing
- Check GitHub Actions tab in your repository
- Make sure GitHub Pages is enabled in Settings > Pages

**Theme looks broken?**
- Make sure you deleted the old `_layouts` and `_includes` folders
- Check that `baseurl` and `url` are correct in `_config.yml`

**Want to test locally?**
```bash
bundle install
bundle exec jekyll serve
```
Visit http://localhost:4000/andrewkraemer.party/

---

## Your Current Posts

All your great travel posts from 2017 will work perfectly with the new theme! They'll just look more modern and clean.

