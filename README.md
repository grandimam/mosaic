# Mosaic - Minimalist Jekyll Theme

A clean, minimalist Jekyll theme with a modern design perfect for blogs, portfolios, and personal websites. Features a responsive layout, clean typography, and easy customization.

## Features

- **Clean & Modern Design**: Minimalist layout with excellent typography
- **Fully Responsive**: Mobile-first design that looks great on all devices
- **SEO Optimized**: Built-in SEO tags and meta data support
- **Fast Loading**: Optimized CSS and minimal dependencies
- **Blog Ready**: Post pagination, tags, and reading time
- **Easy Customization**: Simple configuration and styling options
- **Social Media Ready**: Open Graph and Twitter Card support

## Demo

See the theme in action at: [Live Demo](https://grandimam.github.io/mosaic)

## Quick Start

### 1. Use This Template

Click "Use this template" on GitHub or clone the repository:

```bash
git clone https://github.com/grandimam/mosaic.git my-website
cd my-website
```

### 2. Install Dependencies

```bash
gem install bundler jekyll
bundle install
```

### 3. Configure Your Site

Edit `_config.yml` with your information:

```yaml
# Site settings
title: Your Site Name
description: A brief description of your site
url: "https://yourdomain.com"

# Author
author:
  name: Your Name
  twitter: yourtwitterhandle

# SEO and meta tags
tagline: Your Site Tagline
keywords:
  - your
  - relevant
  - keywords
```

### 4. Run Locally

```bash
bundle exec jekyll serve
```

Visit `http://localhost:4000` to see your site.

## Customization

### Site Configuration

All main settings are in `_config.yml`:

- **Basic Info**: title, description, URL, author details
- **Navigation**: Add/remove menu items in the `navigation` section
- **SEO**: Keywords, social media handles, meta descriptions
- **Pagination**: Number of posts per page

### Navigation Menu

Update the navigation menu in `_config.yml`:

```yaml
navigation:
  - title: posts
    url: /
  - title: about
    url: /about
  - title: contact
    url: /contact
```

### Creating Content

#### Blog Posts

Create new posts in the `_posts/` directory with the naming format:
```
YYYY-MM-DD-post-title.md
```

Use this front matter template:

```yaml
---
layout: post
title: "Your Post Title"
date: 2024-01-01
reading_time: 5
tags: [tag1, tag2, tag3]
slug: your-post-slug
excerpt: "A brief description of your post content"
---

Your post content goes here...
```

#### Pages

Create new pages as `.md` files in the root directory:

```yaml
---
layout: default
title: "Page Title"
---

Your page content...
```

### Styling

The theme uses inline CSS in `_layouts/default.html` for simplicity. Main style sections:

- **Typography**: Font families, sizes, and spacing
- **Layout**: Grid system and responsive design
- **Components**: Navigation, cards, buttons
- **Colors**: Update color variables at the top of the CSS

### Custom Colors

Update these CSS variables in `_layouts/default.html`:

```css
:root {
  --primary-color: #000;
  --secondary-color: #666;
  --background-color: #fff;
  --accent-color: #0070f3;
}
```

## File Structure

```
├── _config.yml          # Site configuration
├── _layouts/            # Page layouts
│   ├── default.html     # Base layout with CSS
│   └── post.html        # Blog post layout
├── _includes/           # Reusable components
│   ├── header.html      # Site header with navigation
│   ├── sidebar.html     # Desktop sidebar navigation  
│   ├── footer.html      # Site footer
│   └── blog-card.html   # Blog post card component
├── _posts/              # Blog posts
├── _data/               # Data files (optional)
├── assets/              # Static assets
│   ├── css/
│   └── js/
├── index.html           # Homepage
├── about.md             # About page
└── Gemfile              # Ruby dependencies
```

## Deployment

### GitHub Pages

1. Push your code to a GitHub repository
2. Go to Settings > Pages
3. Select source: "Deploy from a branch"
4. Choose "main" branch
5. Your site will be available at `https://username.github.io/repository-name`

### Netlify

1. Connect your GitHub repository to Netlify
2. Build command: `bundle exec jekyll build`
3. Publish directory: `_site`
4. Deploy!

### Vercel

1. Connect your GitHub repository to Vercel
2. Framework preset: "Other"
3. Build command: `bundle exec jekyll build`
4. Output directory: `_site`
5. Deploy!

## Advanced Customization

### Adding New Layouts

1. Create a new file in `_layouts/`
2. Use the default layout as a base:

```html
---
layout: default
---
<div class="custom-layout">
  {{ content }}
</div>
```

### Custom Includes

Create reusable components in `_includes/`:

```html
<!-- _includes/custom-component.html -->
<div class="custom-component">
  <h3>{{ include.title }}</h3>
  <p>{{ include.content }}</p>
</div>
```

Use in pages:

```html
{% include custom-component.html title="My Title" content="My content" %}
```

### Adding JavaScript

Add JavaScript to `assets/js/main.js` and include in the layout:

```html
<script src="{{ '/assets/js/main.js' | relative_url }}"></script>
```

### Custom CSS

For extensive styling, create `assets/css/custom.css`:

```css
/* Custom styles */
.my-custom-class {
  color: #333;
}
```

Include in the layout:

```html
<link rel="stylesheet" href="{{ '/assets/css/custom.css' | relative_url }}">
```

## Troubleshooting

### Common Issues

**Bundle install fails**
```bash
gem install bundler
bundle install --retry=3
```

**Ruby version issues**
```bash
rbenv install 3.1.0
rbenv global 3.1.0
```

**Port already in use**
```bash
bundle exec jekyll serve --port 4001
```

**Build fails on GitHub Pages**
- Ensure all gems in `Gemfile` are GitHub Pages compatible
- Check the [GitHub Pages gem list](https://pages.github.com/versions/)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## Support

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Issues](https://github.com/grandimam/mosaic/issues)
- [Discussions](https://github.com/grandimam/mosaic/discussions)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Credits

Built with ❤️ using [Jekyll](https://jekyllrb.com/)

---

**Happy blogging!** 🚀