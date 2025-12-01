---
layout: page
title: "Gyűjtemény"
icon: fas fa-leaf
order: 2
---

# Gyűjtemény

Az alábbi listában találod a fák adatlapjait.  
Kattints bármelyikre a történet, mérések és napló megtekintéséhez.

<style>
.tree-card {
  display: flex;
  align-items: center;
  padding: 0.75rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  background: var(--card-bg);
  box-shadow: var(--shadow-sm);
  transition: 0.2s ease;
}

.tree-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.tree-thumb {
  width: 90px;
  height: 90px;
  border-radius: 8px;
  object-fit: cover;
  margin-right: 1rem;
  background: #333;
}

.tree-info h3 {
  margin: 0;
  font-size: 1.1rem;
}

.tree-info p {
  margin: 0;
  font-size: 0.9rem;
  color: var(--text-muted);
}
</style>

{% assign all_tree_pages = site.pages | where: "layout", "tree" %}
{% assign trees = all_tree_pages | where_exp: "t", "t.url contains '/trees/'" | sort: "title" %}

{% if trees.size > 0 %}
{% for tree in trees %}
<div class="tree-card">
  <img
    class="tree-thumb"
    src="{{ tree.thumb_image | default: tree.hero_image | relative_url }}"
    alt="{{ tree.title }}"
  >
  <div class="tree-info">
    <h3>
      <a href="{{ tree.url | relative_url }}" style="text-decoration:none; color:inherit;">
        {{ tree.title }}
      </a>
    </h3>

    {% if tree.species %}
    <p>
      <em>{{ tree.species.latin }}</em>
      {% if tree.species.cultivar %} ‘{{ tree.species.cultivar }}’{% endif %}
    </p>
    {% endif %}

    {% if tree.code %}
    <p>Kód: <code>{{ tree.code }}</code></p>
    {% endif %}
  </div>
</div>
{% endfor %}
{% else %}
<p>Még nincs fa a gyűjteményben – kezd az első adatlap létrehozásával! 🌱</p>
{% endif %}


