{% extends 'full.tpl'%}

{% block body %}
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">
    <h1 id="main-title">{{ nb.metadata.course_title }}</h1>
{{ super.super() }}
    </div>
  </div>
</body>
{%- endblock body %}

{% block markdowncell %}
<div class="cell border-box-sizing text_cell rendered{% if cell.custom_class %} {{ cell.custom_class }}{% endif %}">
{%- if resources.global_content_filter.include_input_prompt-%}
    {{ self.empty_in_prompt() }}
{%- endif -%}
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
{{ cell.source  | markdown2html | strip_files_prefix }}
</div>
</div>
</div>
{% endblock markdowncell %}

{% block in_prompt -%}
<div class="prompt input_prompt">
    {%- if cell.metadata.writefile is defined -%}
        {{ cell.metadata.writefile }}
    {%- elif cell.execution_count is defined -%}
        In&nbsp;[{{ cell.execution_count|replace(None, "&nbsp;") }}]:
    {%- else -%}
        In&nbsp;[&nbsp;]:
    {%- endif -%}
</div>
{%- endblock in_prompt %}
