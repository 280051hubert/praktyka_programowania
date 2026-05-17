from abc import ABC


class WsparcieHandler(ABC):
    def __init__(self):
        self._next: WsparcieHandler | None = None

    def set_next(self, handler: "WsparcieHandler") -> "WsparcieHandler":
        self._next = handler
        return handler

    def handle(self, request: str) -> str | None: ...

    def pass_to_next(self, request: str) -> str | None:
        if self._next:
            return self._next.handle(request)
        return None


class BotHandler(WsparcieHandler):
    FAQ = {
        "stop": "Wlacz i wylacz.",
        "godziny": "nie mamy godzin",
    }

    def handle(self, request: str) -> str | None:
        for keyword, answer in self.FAQ.items():
            if keyword in request.lower():
                return f"[Bot] {answer}"
        print(f"[I linia] nie mozna obsluzyc xd: '{request}' daje dlaej")
        return self.pass_to_next(request)


class PierwszaLiniaHandler(WsparcieHandler):
    def handle(self, request: str) -> str | None:
        if "internet" in request.lower() or "drukarka" in request.lower():
            return f"[I linia] rozwiazano: '{request}'"
        print(f"[I linia] nie mozna obsluzyc xd: '{request}' daje dlaej")
        return self.pass_to_next(request)


class DrugaLiniaHandler(WsparcieHandler):
    def handle(self, request: str) -> str | None:
        return f"[Specjalista] przejmuje: '{request}'"


if __name__ == "__main__":
    bot = BotHandler()
    pierwsza_linia = PierwszaLiniaHandler()
    specjalista = DrugaLiniaHandler()

    bot.set_next(pierwsza_linia).set_next(specjalista)

    zgloszenia = [
        "reset hasla heeelp",
        "internet kaputt",
        "serwer zdycha co 5 minut",
        "jakie godziny jestescie??? otwarci??",
    ]

    for i in zgloszenia:
        print(f"\n zgloszenie: {i}")
        wynik = bot.handle(i)
        if wynik:
            print(f"    Odpowiedź: {wynik}")
