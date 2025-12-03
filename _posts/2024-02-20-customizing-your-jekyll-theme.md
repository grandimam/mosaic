---
layout: post
title: "Customizing Your Jekyll Theme"
date: 2024-02-20
reading_time: 5
tags: [jekyll, customization, web-development]
slug: customizing-your-jekyll-theme
excerpt: "Learn how to personalize your Jekyll theme with custom colors, layouts, and components to make your website truly unique."
---

One of the great things about Jekyll is how easy it is to customize your theme. This post will walk you through some common customizations you can make to personalize your site.

## Changing Colors and Styles

The Mosaic theme uses inline CSS for simplicity. You can find all the styles in the `_layouts/default.html` file. Here are some key areas you might want to customize:

### Color Scheme

Look for these CSS variables to change your site's colors:

```css
:root {
  --primary-color: #000;
  --secondary-color: #666;
  --background-color: #fff;
  --accent-color: #0070f3;
}
```

### Typography

Change fonts by updating the `font-family` property:

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
}
```

## Adding Custom Components

You can create reusable components in the `_includes/` directory. For example, create a custom callout box:

```html
<!-- _includes/callout.html -->
<div class="callout callout-{{ include.type }}">
  <h4>{{ include.title }}</h4>
  <p>{{ include.content }}</p>
</div>
```

Then use it in your posts:

```liquid
<!-- {% include callout.html type="info" title="Pro Tip" content="Always backup your site before making major changes!" %} -->
```

## Modifying Navigation

Update your site navigation in the `_config.yml` file:

```yaml
navigation:
  - title: Home
    url: /
  - title: Blog
    url: /blog
  - title: Projects
    url: /projects
  - title: About
    url: /about
```

## Adding New Page Layouts

Create custom layouts for different types of content:

1. Create a new file in `_layouts/` (e.g., `portfolio.html`)
2. Base it on the default layout
3. Add your custom HTML and CSS
4. Use it in your pages with `layout: portfolio`

## Tips for Customization

- Always test changes locally before deploying
- Keep backups of working configurations
- Use browser developer tools to experiment with styles
- Check that your changes work on mobile devices

Remember, the goal is to make your site reflect your personality and needs. Don't be afraid to experiment!