from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("😀 [link=https://data-sandbox.github.io/]data-sandbox (website & blog)",
            guide_style="bold bright_black")

ds_tree = tree.add("📊 Data Science Projects", guide_style="bright_black")
ds_tree.add(
    "[bold link=https://github.com/data-sandbox/nlp-brewer-finder]brewyou[/]       - [bright_black]find better breweries (NLP)")
ds_tree.add(
    "[bold link=https://github.com/data-sandbox/ml-bluebikes-forecasting]bluebikes[/]     - [bright_black]time series forecasting (ML)")
ds_tree.add(
    "[bold link=https://github.com/data-sandbox/llms/blob/main/GPT-3_chatbot.ipynb]barbot[/]        - [bright_black]custom chatbot for bar orders (LLM)")
ds_tree.add(
    "[bold link=https://github.com/data-sandbox/ml-sandbox/tree/main/sentiment_amazon]sentiment[/]     - [bright_black]sentiment analysis of reviews (NLP)")
ds_tree.add(
    "[bold link=https://github.com/data-sandbox/bash/tree/main/rsync]rsync[/]         - [bright_black]backup workflow without the cloud (bash)")
ds_tree.add(
    "[bold link=https://data-sandbox.github.io/energy-dashboard/]energy dash[/]   - [bright_black]dashboard of energy statistics (API)")

dev_tree = tree.add("⚛️ Software Development Projects",
                    guide_style="bright_black")
dev_tree.add(
    "[bold link=https://data-sandbox.github.io/restaurant/]single-page[/]   - [bright_black]dynamic page rewrites (JS, HTML, CSS)")
dev_tree.add(
    "[bold link=https://data-sandbox.github.io/etch-a-sketch/]etch-a-sketch[/] - [bright_black]drawing sketch pad (JS, HTML, CSS)")
dev_tree.add(
    "[bold link=https://data-sandbox.github.io/library/]library[/]       - [bright_black]store your reading list (JS, HTML, CSS)")
dev_tree.add(
    "[bold link=https://data-sandbox.github.io/tic-tac-toe/]tic-tac-toe[/]   - [bright_black]tic tac toe game (JS, HTML, CSS)")
dev_tree.add(
    "[bold link=https://data-sandbox.github.io/admin-dashboard/]dashboard[/]     - [bright_black]responsive admin dashboard (HTML, CSS)")
dev_tree.add(
    "[bold link=https://data-sandbox.github.io/calculator/]calculator[/]    - [bright_black]JavaScript calculator (JS, HTML, CSS)")
dev_tree.add(
    "[bold link=https://github.com/data-sandbox/data-sandbox.github.io]website[/]       - [bright_black]personal website and blog (JS, HTML, CSS")

console.print(tree)


CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("parts/02_tree.md", inline_styles=True,
                  code_format=CONSOLE_HTML_FORMAT)
