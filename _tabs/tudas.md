---
layout: page
title: Tudástár
icon: fas fa-book
order: 5
permalink: /tudastar/
---

Hasznos információk, útmutatók és szakmai tudás a bonsai gondozásról.
(Javaslom, ha teheted ezeket a cikkeket nagy monitoron olvasd, mert a nagymennyiségű, rendszerezett információt mobil méretben nehéz olvashatóan megjeleníteni.)

<style>
.knowledge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.knowledge-card {
  background: var(--card-bg, #ffffff);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
  border: 1px solid var(--border-color, #e5e7eb);
  animation: fadeInUp 0.5s ease;
}

.knowledge-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

.knowledge-header {
  width: 100%;
  height: 20px;
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
}

.knowledge-content {
  padding: 1.5rem;
}

.knowledge-card h3 {
  margin: 0 0 1rem 0;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--heading-color, #1f2937);
}

.knowledge-card h3 a {
  text-decoration: none;
  color: inherit;
  transition: color 0.2s ease;
}

.knowledge-card h3 a:hover {
  color: #22c55e;
}

.knowledge-description {
  font-size: 1rem;
  line-height: 1.6;
  color: var(--text-secondary, #4b5563);
  margin-bottom: 1rem;
}

.knowledge-read-more {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #22c55e;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.knowledge-read-more:hover {
  gap: 0.75rem;
  color: #16a34a;
}

.knowledge-read-more svg {
  width: 16px;
  height: 16px;
  transition: transform 0.2s ease;
}

.knowledge-read-more:hover svg {
  transform: translateX(4px);
}

.no-knowledge-message {
  text-align: center;
  padding: 3rem 1rem;
  background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
  border-radius: 12px;
  border: 2px dashed #22c55e;
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

.knowledge-card:nth-child(1) { animation-delay: 0.1s; }
.knowledge-card:nth-child(2) { animation-delay: 0.2s; }
.knowledge-card:nth-child(3) { animation-delay: 0.3s; }
.knowledge-card:nth-child(4) { animation-delay: 0.4s; }
.knowledge-card:nth-child(5) { animation-delay: 0.5s; }

@media (max-width: 768px) {
  .knowledge-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .knowledge-header {
    height: 8px;
  }
}
</style>

{% assign knowledge_articles = site.tudas | sort: "title" %}

{% if knowledge_articles.size > 0 %}
<div class="knowledge-grid">
  {% for article in knowledge_articles %}
  <article class="knowledge-card">
    <div class="knowledge-header"></div>

    <div class="knowledge-content">
      <h3>
        <a href="{{ article.url | relative_url }}">{{ article.title }}</a>
      </h3>

      <div class="knowledge-description">
        {% if article.description %}
          {{ article.description }}
        {% else %}
          Description here
        {% endif %}
      </div>

      <a href="{{ article.url | relative_url }}" class="knowledge-read-more">
        Tovább olvasom
        <svg fill="currentColor" viewBox="0 0 16 16">
          <path fill-rule="evenodd" d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
        </svg>
      </a>
    </div>
  </article>
  {% endfor %}
</div>
{% else %}
<div class="no-knowledge-message">
  <p>📚 Hamarosan érkeznek a tudásanyagok!</p>
</div>
{% endif %}
