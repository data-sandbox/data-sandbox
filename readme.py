from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("😀 [link=https://data-sandbox.github.io/]data-sandbox",
            guide_style="bold bright_black")

main_tree = tree.add("📘 Main Projects", guide_style="bright_black")
main_tree.add(
    "[bold link=https://github.com/data-sandbox/nlp-brewer-finder]brewyou[/]      - [bright_black]find better breweries (NLP)")
main_tree.add(
    "[bold link=https://github.com/data-sandbox/ml-bluebikes-forecasting]bluebikes[/]    - [bright_black]time series forecasting (ML)")
main_tree.add(
    "[bold link=https://github.com/data-sandbox/data-sandbox.github.io]website[/]      - [bright_black]personal website and blog (web)")

mini_tree = tree.add("📚 Mini Projects", guide_style="bright_black")
mini_tree.add(
    "[bold link=https://github.com/data-sandbox/llms/blob/main/GPT-3_chatbot.ipynb]barbot[/]       - [bright_black]custom chatbot for bar orders (LLM)")
mini_tree.add(
    "[bold link=https://github.com/data-sandbox/ml-sandbox/tree/main/sentiment_amazon]sentiment[/]    - [bright_black]sentiment analysis of reviews (NLP)")
mini_tree.add(
    "[bold link=https://github.com/data-sandbox/data-pipelines/tree/main/bash_temp_reporting]etl[/]          - [bright_black]ETL pipeline with bash scripting")
mini_tree.add(
    "[bold link=https://github.com/data-sandbox/ml-sandbox/tree/main/diamond_quality]multiclass[/]   - [bright_black]multiclass classifier (ML)")
mini_tree.add(
    "[bold link=https://github.com/data-sandbox/restaurant-inspections]inspections[/]  - [bright_black]query NYC restaurant data (SQL)")
mini_tree.add(
    "[bold link=https://github.com/data-sandbox/distributed-computing]spark[/]        - [bright_black]distributing computing & clusters (Spark)")
mini_tree.add(
    "[bold link=https://github.com/data-sandbox/bash/tree/main/rsync]rsync[/]        - [bright_black]backup workflow without the cloud (bash)")

stats_tree = tree.add("📈 Explorations", guide_style="bright_black")
stats_tree.add(
    "[bold link=https://github.com/data-sandbox/stats-sandbox/blob/main/bootstrap.ipynb]bootstrap[/]    - [bright_black]powerful resampling technique (stats)")
stats_tree.add(
    "[bold link=https://github.com/data-sandbox/stats-sandbox/blob/main/permutation.ipynb]permutation[/]  - [bright_black]statistical significance test (stats)")

console.print(tree)
console.print("")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True,
                  code_format=CONSOLE_HTML_FORMAT)
