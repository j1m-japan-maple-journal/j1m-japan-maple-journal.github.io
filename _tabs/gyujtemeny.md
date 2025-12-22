---
layout: page
title: "Gyűjtemény"
icon: fas fa-leaf
order: 3
---

Az alábbi listában találod a fák adatlapjait.  
Kattints bármelyikre a történet, mérések és napló megtekintéséhez.

<style>
.collection-intro {
  background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
  border-left: 4px solid #22c55e;
  padding: 1.5rem;
  border-radius: 12px;
  margin-bottom: 2rem;
  animation: fadeInUp 0.5s ease;
}

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

.tree-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.tree-card {
  display: flex;
  flex-direction: column;
  background: var(--card-bg, #ffffff);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  border: 1px solid var(--border-color, #e5e7eb);
  animation: fadeInUp 0.6s ease;
}

.tree-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
}

.tree-thumb {
  width: 100%;
  height: 220px;
  object-fit: cover;
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
  transition: transform 0.3s ease;
}

.tree-card:hover .tree-thumb {
  transform: scale(1.05);
}

.tree-info {
  padding: 1.5rem;
}

.tree-info h3 {
  margin: 0 0 0.75rem 0;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text-primary, #1f2937);
}

.tree-info h3 a {
  text-decoration: none;
  color: inherit;
  transition: color 0.2s ease;
}

.tree-info h3 a:hover {
  color: #22c55e;
}

.tree-species {
  font-size: 1rem;
  color: var(--text-secondary, #4b5563);
  margin-bottom: 0.75rem;
  line-height: 1.5;
}

.tree-species em {
  color: var(--text-primary, #1f2937);
  font-style: italic;
}

.tree-cultivar {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
  color: white;
  border-radius: 12px;
  font-size: 0.875rem;
  font-weight: 600;
  margin-left: 0.5rem;
  transition: transform 0.2s ease;
}

.tree-card:hover .tree-cultivar {
  transform: scale(1.1);
}

.tree-code {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: var(--bg-tertiary, #f3f4f6);
  border-radius: 8px;
  font-family: 'Courier New', monospace;
  font-size: 0.875rem;
  color: var(--text-secondary, #6b7280);
  margin-top: 0.75rem;
  transition: all 0.2s ease;
}

.tree-card:hover .tree-code {
  background: #22c55e;
  color: white;
}

.no-trees-message {
  text-align: center;
  padding: 3rem 1rem;
  background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
  border-radius: 12px;
  border: 2px dashed #22c55e;
  animation: fadeInUp 0.7s ease;
}

.no-trees-message p {
  font-size: 1.25rem;
  color: var(--text-secondary, #4b5563);
  margin: 0;
}

@media (max-width: 768px) {
  .tree-grid {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  .tree-info h3 {
    font-size: 1.25rem;
  }

  .tree-thumb {
    height: 180px;
  }
}

/* Staggered animation */
.tree-card:nth-child(1) { animation-delay: 0.1s; }
.tree-card:nth-child(2) { animation-delay: 0.2s; }
.tree-card:nth-child(3) { animation-delay: 0.3s; }
.tree-card:nth-child(4) { animation-delay: 0.4s; }
.tree-card:nth-child(5) { animation-delay: 0.5s; }
.tree-card:nth-child(6) { animation-delay: 0.6s; }
</style>

{% assign all_tree_pages = site.pages | where: "layout", "tree" %}
{% assign trees = all_tree_pages | where_exp: "t", "t.url contains '/trees/'" | sort: "title" %}

{% if trees.size > 0 %}
<div class="tree-grid">
  {% for tree in trees %}
  <article class="tree-card">
    <img
      class="tree-thumb"
      src="{{ tree.thumb_image | default: tree.hero_image | relative_url }}"
      alt="{{ tree.title }}"
    >
    <div class="tree-info">
      <h3>
        <a href="{{ tree.url | relative_url }}">
          {{ tree.title }}
        </a>
      </h3>

      {% if tree.species %}
      <div class="tree-species">
        <em>{{ tree.species.latin }}</em>
        {% if tree.species.cultivar %}<span class="tree-cultivar">{{ tree.species.cultivar }}</span>{% endif %}
      </div>
      {% endif %}

      {% if tree.code %}
      <div class="tree-code">
        📋 {{ tree.code }}
      </div>
      {% endif %}
    </div>
  </article>
  {% endfor %}
</div>
{% else %}
<div class="no-trees-message">
  <p>🌱 Még nincs fa a gyűjteményben – kezd az első adatlap létrehozásával!</p>
</div>
{% endif %}


