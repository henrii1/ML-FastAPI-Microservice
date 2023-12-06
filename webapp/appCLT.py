#!/usr/bin/env python

import click
from app_greedy import greedy_coin
from app_openai import submit_question, create_code
from app_wiki import get_wiki_keyword, get_wiki_page, get_wiki_summary, search_wiki_pages


@click.group()
def cli():
    """OpenAI command line"""


@cli.command()
@click.argument("text")
def sub_question(text):
    """Cli tool to ask the openai api questions"""
    print(submit_question(text))


@cli.command()
@click.argument("text")
@click.argument("language")
def cr_code(text, language):
    """CLI tool for code generation"""
    print(create_code(text, language))


@cli.command()
@click.argument("change", type=float)
def coin_cli(change):
    """returns the min number of coins for a change"""
    greedy_coin(change)


@cli.command()
@click.argument("page")
def wiki_keyword(page):
    """get a keyword from wikipedia"""
    get_wiki_keyword(page)


@cli.command()
@click.argument("page")
def wiki_page(page):
    """check for a page on wikipedia"""
    search_wiki_pages(page)


@cli.command()
@click.argument("page")
def wiki_summary(page):
    """returns the summary of a wikipedia page"""
    get_wiki_summary(page)


@cli.command()
@click.argument("page")
def get_page(page):
    """returns a wikipedia page """
    get_wiki_page(page)


if __name__ == "__main__":
    cli()


    




