from behave import then
from behave.api.async_step import async_run_until_complete
from models.repos_page import ReposPage

@then('the repos page description is "{repos}"')
@async_run_until_complete
async def page_description(context, repos: str):
    """
    :param repos:
    :type context: behave.runner.Context
    """
    repos_page = ReposPage(context.page)
    assert await repos_page.is_project_text_contains(repos)

