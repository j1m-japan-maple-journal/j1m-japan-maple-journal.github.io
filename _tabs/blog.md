---
layout: page
title: "Blog & Hírek"
icon: fas fa-newspaper
order: 2
---

Kövess nyomon minden újdonságot, tapasztalatot és történetet a japán juharok világából!

<style>
.blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.blog-post-card {
  background: var(--card-bg, #ffffff);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  border: 1px solid var(--border-color, #e5e7eb);
}

.blog-post-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

.blog-post-image {
  width: 100%;
  height: 20px;
  object-fit: cover;
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
}

.blog-post-content {
  padding: 1.5rem;
}

.blog-post-date {
  display: inline-block;
  font-size: 0.875rem;
  color: var(--text-muted, #6b7280);
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.blog-post-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0.5rem 0;
  color: var(--text-primary, #1f2937);
}

.blog-post-title a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s ease;
}

.blog-post-title a:hover {
  color: #22c55e;
}

.blog-post-excerpt {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-secondary, #4b5563);
  margin: 1rem 0;
}

.blog-post-categories {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.blog-category-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
  color: white;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  transition: all 0.2s ease;
}

.blog-category-badge:hover {
  transform: scale(1.05);
  box-shadow: 0 2px 8px rgba(34, 197, 94, 0.3);
}

.blog-read-more {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #22c55e;
  font-weight: 600;
  text-decoration: none;
  margin-top: 1rem;
  transition: all 0.2s ease;
}

.blog-read-more:hover {
  gap: 0.75rem;
  color: #16a34a;
}

.blog-read-more svg {
  width: 16px;
  height: 16px;
  transition: transform 0.2s ease;
}

.blog-read-more:hover svg {
  transform: translateX(4px);
}

.no-posts-message {
  text-align: center;
  padding: 3rem 1rem;
  color: var(--text-muted, #6b7280);
  font-size: 1.125rem;
}

/* Fade in animation */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.blog-post-card {
  animation: fadeInUp 0.5s ease;
}

.blog-post-card:nth-child(1) { animation-delay: 0.1s; }
.blog-post-card:nth-child(2) { animation-delay: 0.2s; }
.blog-post-card:nth-child(3) { animation-delay: 0.3s; }
.blog-post-card:nth-child(4) { animation-delay: 0.4s; }
.blog-post-card:nth-child(5) { animation-delay: 0.5s; }
.blog-post-card:nth-child(6) { animation-delay: 0.6s; }

@media (max-width: 768px) {
  .blog-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .blog-post-image {
    height: 50px;
  }

  .blog-post-title {
    font-size: 1.25rem;
  }
}

/* Dark mode adjustments */
[data-mode="dark"] .blog-post-title {
  color: #ffffff !important;
}

/* ── Language filter bar ── */
.lang-filter-bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

.lang-filter-label {
  font-size: 0.85rem;
  color: var(--text-muted, #6b7280);
  margin-right: 0.25rem;
}

.lang-filter-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.3rem 0.9rem;
  border: 1px solid #d1d5db;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
  background: transparent;
  color: var(--text-secondary, #4b5563);
  transition: all 0.2s ease;
}

.lang-filter-btn:hover {
  border-color: #22c55e;
  color: #16a34a;
}

.lang-filter-btn.active {
  background: #22c55e;
  border-color: #22c55e;
  color: #fff;
}

[data-mode="dark"] .lang-filter-btn {
  border-color: #404040;
  color: #a0a0a0;
}

[data-mode="dark"] .lang-filter-btn:hover {
  border-color: #22c55e;
  color: #22c55e;
}

[data-mode="dark"] .lang-filter-btn.active {
  background: #22c55e;
  border-color: #22c55e;
  color: #fff;
}

.no-posts-filtered {
  display: none;
  text-align: center;
  padding: 3rem 1rem;
  color: var(--text-muted, #6b7280);
  font-size: 1.125rem;
}

</style>

{% if jekyll.environment == "production" %}
  {% assign posts = site.posts | where_exp: "item", "item.hidden != true" | sort: 'date' | reverse %}
{% else %}
  {% assign posts = site.posts | sort: 'date' | reverse %}
{% endif %}

{% if posts.size > 0 %}

<div class="lang-filter-bar">
  <span class="lang-filter-label">Nyelv / Language:</span>
  <button class="lang-filter-btn" data-filter="all">🌍 Mind / All</button>
  <!-- default to magyar on every page -->
  <button class="lang-filter-btn active" data-filter="hu">🇭🇺 Magyar</button>
  <button class="lang-filter-btn" data-filter="en">🇬🇧 English</button>
</div>

<div class="no-posts-filtered" id="no-posts-filtered">
  <p>Nincs találat / No posts found.</p>
</div>

<div class="blog-grid" id="blog-grid">
  {% for post in posts %}
  {% assign _post_url_tail = post.url | slice: -4, 4 %}
  {% if _post_url_tail == '-en/' %}
    {% assign _post_lang = 'en' %}
  {% else %}
    {% assign _post_lang = 'hu' %}
  {% endif %}
  <article class="blog-post-card" data-lang="{{ _post_lang }}">
    {% if post.image %}
    <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="blog-post-image">
    {% else %}
    <div class="blog-post-image"></div>
    {% endif %}

    <div class="blog-post-content">
      <time class="blog-post-date" datetime="{{ post.date | date_to_xmlschema }}">
        📅 {{ post.date | date: "%Y. %B %d." }}
      </time>

      <h2 class="blog-post-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>

      {% if post.excerpt %}
      <div class="blog-post-excerpt">
        {{ post.excerpt | strip_html | truncatewords: 30 }}
      </div>
      {% endif %}

      {% if post.categories %}
      <div class="blog-post-categories">
        {% for category in post.categories %}
        <span class="blog-category-badge">{{ category }}</span>
        {% endfor %}
      </div>
      {% endif %}

      <a href="{{ post.url | relative_url }}" class="blog-read-more">
        {% if _post_lang == 'en' %}Read more{% else %}Tovább olvasom{% endif %}
        <svg fill="currentColor" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
        </svg>
      </a>
    </div>
  </article>
  {% endfor %}
</div>
{% else %}
<div class="no-posts-message">
  <p>📝 Még nincs blogbejegyzés – hamarosan érkeznek az első történetek! 🌱</p>
</div>
{% endif %}

<script>
(function () {
  var buttons = document.querySelectorAll('.lang-filter-btn');
  var cards   = document.querySelectorAll('#blog-grid .blog-post-card');
  var noPostsMsg = document.getElementById('no-posts-filtered');

  function applyFilter(filter) {
    var visible = 0;
    cards.forEach(function (card) {
      var lang = card.getAttribute('data-lang');
      var show = filter === 'all' || lang === filter;
      card.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    noPostsMsg.style.display = visible === 0 ? 'block' : 'none';
  }

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      buttons.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      applyFilter(btn.getAttribute('data-filter'));
    });
  });

  // ensure default filter applies on load (Magyar)
  applyFilter('hu');
})();
</script>
