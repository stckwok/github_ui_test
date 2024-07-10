from playwright.async_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    # common attributes for all child pages
    async def is_title_contains(self, text) -> bool:
        title = await self.page.title()
        if title.find(text) == -1:
            return False
        else:
            expect(self.page).to_have_title(text)
            return True

    def is_url_contains(self, text) -> bool:
        if self.page.url.find(text) == -1:
            return False
        else:
            expect(self.page).to_have_url(text)
            return True
