#!/usr/bin/env python3
"""
Clean up WordPress-style front matter in Jekyll posts to simplified format
"""
import os
import re
from pathlib import Path

def clean_frontmatter(filepath):
    """Clean up front matter in a post file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has front matter
    if not content.startswith('---'):
        return False

    # Split front matter and content
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    frontmatter = parts[1]
    post_content = parts[2]

    # Extract important fields
    layout = re.search(r'^layout:\s*(.+)$', frontmatter, re.MULTILINE)
    title = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
    date = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', frontmatter, re.MULTILINE)
    categories = re.search(r'^categories:\s*(.+)$', frontmatter, re.MULTILINE)
    tags = re.search(r'^tags:\s*(.+)$', frontmatter, re.MULTILINE)

    # Check if already clean (no 'type', 'published', 'status', or 'meta' fields)
    has_wordpress_fields = any([
        'type:' in frontmatter,
        'published:' in frontmatter,
        'status:' in frontmatter,
        'meta:' in frontmatter
    ])

    if not has_wordpress_fields:
        print(f"  ✓ {filepath.name} already clean")
        return False

    # Build new front matter
    new_frontmatter = "---\n"

    if layout:
        new_frontmatter += f"layout: {layout.group(1).strip()}\n"

    if title:
        title_text = title.group(1).strip()
        # Ensure title is quoted if it contains special characters
        if not (title_text.startswith('"') or title_text.startswith("'")):
            title_text = f'"{title_text}"'
        new_frontmatter += f"title: {title_text}\n"

    if date:
        new_frontmatter += f"date: {date.group(1)}\n"

    if categories:
        cats = categories.group(1).strip()
        if cats and cats != '[]':
            new_frontmatter += f"categories: {cats}\n"

    if tags:
        tag_text = tags.group(1).strip()
        if tag_text and tag_text != '[]':
            # Handle multi-line tags
            if '\n' in frontmatter[tags.start():]:
                # Extract multi-line tags
                tags_section = re.search(r'tags:\s*\n((?:-\s*.+\n?)+)', frontmatter, re.MULTILINE)
                if tags_section:
                    new_frontmatter += f"tags:\n{tags_section.group(1)}"
            else:
                new_frontmatter += f"tags: {tag_text}\n"

    new_frontmatter += "---"

    # Write back
    new_content = new_frontmatter + post_content

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ Cleaned {filepath.name}")
    return True

def main():
    posts_dir = Path('_posts')

    if not posts_dir.exists():
        print("Error: _posts directory not found")
        return

    print("Cleaning front matter in posts...\n")

    cleaned_count = 0
    for post_file in sorted(posts_dir.glob('*')):
        if post_file.is_file():
            if clean_frontmatter(post_file):
                cleaned_count += 1

    print(f"\n✓ Cleaned {cleaned_count} posts")

if __name__ == '__main__':
    main()
