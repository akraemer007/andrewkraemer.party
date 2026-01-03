# Photography Page Setup Instructions

## Quick Start

Your photography page is ready to use! Just follow these steps:

### 1. Set Up GLightbox (One-Time Setup)

You need to create a custom `head.html` file to include the GLightbox library.

**Create the file:** `_includes/head.html`

**Paste this content:**

```html
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {%- seo -%}
  <link rel="stylesheet" href="{{ "/assets/main.css" | relative_url }}">
  {%- feed_meta -%}
  {%- if jekyll.environment == 'production' and site.google_analytics -%}
    {%- include google-analytics.html -%}
  {%- endif -%}

  <!-- GLightbox for photo gallery -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/glightbox/dist/css/glightbox.min.css">
  <script src="https://cdn.jsdelivr.net/gh/mcstudios/glightbox/dist/js/glightbox.min.js"></script>
</head>
```

**Create the file:** `_includes/footer.html` (add to the existing footer.html file at the very bottom, before the closing `</footer>` tag)

Add this script just before the closing `</footer>` tag:

```html
<!-- Initialize GLightbox -->
<script>
  const lightbox = GLightbox({
    touchNavigation: true,
    loop: true,
    autoplayVideos: true,
    closeButton: true,
    moreLength: 0
  });
</script>
```

Or if you prefer to create a separate script file, create `_includes/glightbox-init.html`:

```html
<script>
  const lightbox = GLightbox({
    touchNavigation: true,
    loop: true,
    autoplayVideos: true,
    closeButton: true,
    moreLength: 0
  });
</script>
```

Then add `{%- include glightbox-init.html -%}` to your footer or just before the closing `</body>` tag.

### 2. Add Your Photos

**Step 1:** Export photos from Lightroom to `/assets/photos/`

**Step 2:** Open `photography.md`

**Step 3:** Add one line per photo in this format:

```markdown
[![Photo description](/assets/photos/your-photo.jpg)](/assets/photos/your-photo.jpg){: .glightbox data-gallery="gallery1"}
```

**That's it!** The photo will automatically appear in the grid.

### Example

```markdown
<div class="photo-grid" markdown="1">

[![Sunset at the beach](/assets/photos/beach-sunset.jpg)](/assets/photos/beach-sunset.jpg){: .glightbox data-gallery="gallery1"}

[![Mountain landscape](/assets/photos/mountain.jpg)](/assets/photos/mountain.jpg){: .glightbox data-gallery="gallery1"}

[![Street photography in Tokyo](/assets/photos/tokyo-street.jpg)](/assets/photos/tokyo-street.jpg){: .glightbox data-gallery="gallery1"}

</div>
```

## How It Works

- **Responsive Grid:** 3 columns on desktop, 2 on tablet, 1 on mobile
- **Square Thumbnails:** Photos are cropped to squares in the grid using `object-fit: cover`
- **Full-Size Lightbox:** Click any photo to view full-size with arrow navigation
- **Clean Design:** Matches your site's minimal aesthetic

## Photo Requirements

- **Format:** JPEG, PNG, WebP, etc.
- **Size:** For best performance, export at 1200-2000px wide for thumbnails
- **Naming:** Use descriptive filenames (e.g., `yosemite-valley.jpg` not `IMG_1234.jpg`)

## Customization

### Change Grid Columns

Edit `assets/main.scss`, find the `.photo-grid` section and modify:

```scss
.photo-grid {
  grid-template-columns: repeat(3, 1fr) !important; /* Change 3 to desired columns */
}
```

### Change Photo Aspect Ratio

To use rectangular photos instead of squares, edit `assets/main.scss`:

```scss
.photo-grid img {
  aspect-ratio: 3 / 2 !important; /* Or remove this line for original aspect ratio */
}
```

### Add Photo Captions

You can add captions to individual photos:

```markdown
[![Mountain view](/assets/photos/mountain.jpg)](/assets/photos/mountain.jpg){: .glightbox data-gallery="gallery1" data-description="Sunrise at Mount Rainier, Washington"}
```

The caption will appear when the photo is opened in the lightbox.

## Troubleshooting

**Photos not appearing in grid:**
- Check that the image file is in `/assets/photos/`
- Verify the filename matches exactly (case-sensitive)
- Make sure the line is inside the `<div class="photo-grid" markdown="1">` section

**Lightbox not working:**
- Verify GLightbox scripts are loaded (check browser console for errors)
- Make sure the link has the `.glightbox` class
- Check that the script initialization is running (in footer or custom script)

**Grid layout looks broken:**
- Run `jekyll build` to regenerate the site
- Clear browser cache
- Check browser console for CSS errors

## File Structure

```
/assets/
  /photos/
    beach-sunset.jpg
    mountain.jpg
    tokyo-street.jpg
  main.scss (contains grid styles)
/photography.md (the page file)
/_includes/
  head.html (includes GLightbox library)
  footer.html or glightbox-init.html (initializes GLightbox)
```

## Need Help?

The photography page uses:
- **Jekyll** markdown for content
- **CSS Grid** for layout (defined in `assets/main.scss`)
- **GLightbox** for lightbox functionality (https://github.com/biati-digital/glightbox)

All the code has comments explaining what each section does.
