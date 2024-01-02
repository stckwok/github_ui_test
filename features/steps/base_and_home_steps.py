from behave import given, when, then
from behave.api.async_step import async_run_until_complete

from models.base_page import BasePage
from models.home_page import HomePage


@given('the home page is open')
@async_run_until_complete
async def open_login_url(context):
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

@then('the next page is "{title}" page')
@async_run_until_complete
async def is_next_page(context, title: str):
    """
    :param title:
    :type context: behave.runner.Context
    """
    base_page = BasePage(context.page)
    await base_page.is_title_contains(title)
    
    # repos_tab = context.page.get_by_role('link', name="Repositories")
    # await repos_tab.click()
    # api_test_link = base_page.get_by_role('link', name="github_api_test")
    # https://github.com/stckwok?tab=repositories
    # await base_page.is_title_contains(api_test_link)
