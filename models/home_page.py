from playwright.async_api import Page
from models.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.repos = page.get_by_role('link', name="Repositories")

    async def navigate(self, home_url):
        await self.page.goto(home_url, timeout=5000)

    async def repos_login(self):
        await self.repos.click()

    async def click_button(self, action):
        if action == "repos":
            await self.repos_login()
        else:
            assert False

