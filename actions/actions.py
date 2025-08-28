from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Any, List, Dict
from .prof_col import prof
from .podaci_prof import prof_kontakt
from .course import course_links

# Klasa za slanje linka na kolegij
class ActionProvideCourseLink(Action):

    def name(self) -> str:
        return "action_provide_course_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[str, Any]]:


        # Dobij vrijednost iz slota
        course_name = tracker.get_slot("kolegij")

        if course_name:
            # Ukloni nepotrebne razmake i pretvori u mala slova
            course_name_processed = course_name.strip().lower()
            print(f"Traženi kolegij (procesuirano): '{course_name_processed}'")
            # Provjera ključeva u listi
            print(f"Dostupni ključevi u 'course_links': {list(course_links.keys())}")

            url = course_links.get(course_name_processed)

            if url:
                # Kreiraj Markdown link
                link_text = "Više informacija"  # Ili samo "Link", "Ovdje", itd.
                message = f"Više informacija o kolegiju *{course_name}* možete pronaći ovdje: [{link_text}]({url})"
            else:
                message = f"Nažalost, ne mogu pronaći informacije o kolegiju *{course_name}*. Provjerite je li je naziv točan."
        else:
            message = "Molim vas da navedete naziv kolegija."

        dispatcher.utter_message(text=message)
        return []
# Klasa za dohvat nositelja i asistenata kolegija
class ActionShowKolegijNositelji(Action):

    def name(self) -> str:
        return "action_show_kolegij_nositelji"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[str, Any]]:

        kolegij = tracker.get_slot("kolegij")

        if not kolegij:
            dispatcher.utter_message(text="Molim vas da navedete naziv kolegija.")
            return []

        kolegij = kolegij.lower()
        info = prof.get(kolegij)

        if info:
            nositelji = info.get('nositelj kolegija', [])
            asistenti = info.get('asistent kolegija', [])

            nositelji_str = ", ".join(nositelji) if isinstance(nositelji, list) else nositelji
            asistenti_str = ", ".join(asistenti) if isinstance(asistenti, list) else asistenti

            poruka = f"Nositelji kolegija su: {nositelji_str}."
            if asistenti_str:
                poruka += f" Asistenti su: {asistenti_str}."
        else:
            poruka = f"Ne mogu pronaći informacije o kolegiju *{kolegij}*."

        dispatcher.utter_message(text=poruka)
        return []


# Klasa za dohvat nositelja i asistenata kolegija
class ActionDohvatiPodatke(Action):

    def name(self) -> str:
        return "action_dohvati_podatke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> List[Dict[str, Any]]:

        nastavnik = tracker.get_slot("nastavnik")

        if not nastavnik:
            dispatcher.utter_message(text="Molim vas da navedete ime nastavnika.")
            return []

        url = prof_kontakt.get(nastavnik)

        if url:
            # Kreiraj Markdown link
            link_text = f"Informacije o {nastavnik}" # Ili samo "Link", "Ovdje", itd.
            message = f"Možete pronaći informacije o nastavniku *{nastavnik}* ovdje: [{link_text}]({url})"
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text=f"Nažalost, nemam podatke za nastavnika *{nastavnik}*.")

        return []