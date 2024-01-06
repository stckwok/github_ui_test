from playwright.async_api import Page
from models.base_page import BasePage

class ReposPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.project_text = page.locator("p.f4.my-3")

    async def is_project_text_contains(self, value):
        content = await self.project_text.text_content()
        if content.find(value) == -1:
            return False
        else:
            return True
