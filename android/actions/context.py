class Driver():
    def __init__(self):
        pass


class Native():
    def change_to_native(self):
        contexts = self.driver.contexts
        current_context = self.driver.current_context
        if 'NATIVE' in current_context:
            Logger.info(r'Current Context is Native')
            pass
        else:
            for cont in contexts:
                if 'NATIVE' in cont:
                    self.driver.switch_to.context(cont)
                    Logger.info(r'Current Context is Native')
                    break


class Webview:
    def __init__(self, driver):
        self.driver = driver

    def change_to_webview(self):
        contexts = self.driver.contexts
        current_context = self.driver.current_context
        if 'WEBVIEW' in current_context:
            Logger.info(r'Current Context is Web View')
            pass
        else:
            for cont in contexts:
                if 'WEBVIEW' in cont:
                    self.driver.switch_to.context(cont)
                    page_source = self.driver.page_source
                    if '<html><head></head><body></body></html>' not in page_source:
                        Logger.info(r'Current Context is Web View')
                        break
