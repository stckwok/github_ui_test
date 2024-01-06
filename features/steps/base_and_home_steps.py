from behave import given, when, then
from behave.api.async_step import async_run_until_complete

from models.base_page import BasePage
from models.home_page import HomePage
import time

@given('the home page is open')
@async_run_until_complete
async def open_home_page(context):
    home_page = HomePage(context.page)
    await home_page.navigate()

@when('i click "{action}" tab on the home page')
@async_run_until_complete
async def click_repo_tab(context, action: str):
    """
    :param action:
    :type context: behave.runner.Context
    """
    home_page = HomePage(context.page)
    await home_page.click_button(action)

@when('the next page is "{title}" page')
@async_run_until_complete
async def is_next_page(context, title: str):
    """
    :param title:
    :type context: behave.runner.Context
    """
    base_page = BasePage(context.page)
    time.sleep(1)
    await base_page.is_title_contains(title)

@when('the page url contain "{title}"')
@async_run_until_complete
async def is_url_page(context, title: str):
    """
    :param title:
    :type context: behave.runner.Context
    """
    base_page = BasePage(context.page)
    time.sleep(1)
    assert base_page.is_url_contains(title)==True

@when('i click "{project}" project link')
@async_run_until_complete
async def click_proj_link(context, project: str):
    """
    :param project:
    :type context: behave.runner.Context
    """
    api_test_link = context.page.get_by_role('link', name=project)
    await api_test_link.click()

@then('the project "{project}" is open')
@async_run_until_complete
async def proj_opens(context, project: str):
    """
    :param project:
    :type context: behave.runner.Context
    """
    base_page = BasePage(context.page)
    time.sleep(1)
    assert base_page.is_url_contains(project)==True