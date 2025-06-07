import ollama
import argparse
import os

# 2. Funktionssignatur anpassen, um 'num_lines' zu akzeptieren
def analyze_log(file_path: str, query: str, num_lines: int):
    """
    Liest eine Log-Datei und nutzt Ollama, um eine Frage dazu zu beantworten.
    """
    if not os.path.exists(file_path):
        print(f"Fehler: Die Datei '{file_path}' wurde nicht gefunden.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # 3. Den festen Wert durch die Variable ersetzen
            log_content = "".join(lines[-num_lines:])

        prompt = f"""
        Du bist ein erfahrener Systemadministrator. Analysiere den folgenden Ausschnitt aus einer Log-Datei.
        Beantworte die Frage des Benutzers präzise und kurz. Gib wenn möglich konkrete Beispiele aus dem Log an.

        Log-Daten ({num_lines} Zeilen):
        ---
        {log_content}
        ---

        Frage des Benutzers: {query}
        """

        print(f"🤖 Analysiere die letzten {num_lines} Log-Zeilen mit dem lokalen LLM... bitte warten.")

        response = ollama.chat(
            model='gemma3:4b', 
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )

        print("\n✅ Analyse-Ergebnis:\n")
        print(response['message']['content'])

    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analysiere Log-Dateien mit einem lokalen LLM via Ollama.",
        epilog="Beispiel: python analyse.py --datei /var/log/syslog --frage 'Gab es Authentifizierungsfehler?' --zeilen 500"
    )
    parser.add_argument("--datei", required=True, help="Der Pfad zur Log-Datei.")
    parser.add_argument("--frage", required=True, help="Die Frage, die du an die Logs hast.")
    
    # 1. Neues Argument für die Anzahl der Zeilen hinzufügen
    parser.add_argument(
        "--zeilen", 
        type=int, 
        default=200, 
        help="Die Anzahl der letzten Zeilen, die analysiert werden sollen. Standard: 200"
    )

    args = parser.parse_args()
    # Den neuen Parameter an die Funktion übergeben
    analyze_log(args.datei, args.frage, args.zeilen)
