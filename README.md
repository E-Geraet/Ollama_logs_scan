KI-gestützter Log-Analyst mit Ollama & Python

Die Analyse von Log-Dateien ist eine tägliche Aufgabe in der IT. Oft ist sie zeitaufwendig und erfordert tiefes Wissen über die jeweilige Log-Struktur. Dieses Tool vereinfacht den Prozess drastisch:

    Datenschutz zuerst: Alle Daten werden zu 100% lokal verarbeitet. Ihre sensiblen Log-Dateien verlassen niemals Ihre Maschine.
    Flexibel: Funktioniert mit jedem Text-basierten Log und jedem von Ollama unterstützten Sprachmodell.

✨ Features

    Analyse von Logdateien über ein einfaches CLI-Interface.
    Kommunikation mit einem lokal laufenden LLM via Ollama.
    Intelligenter Prompt, der dem LLM den Kontext eines Systemadministrators gibt.
    Konfigurierbare Analyse:
        Anzahl der zu analysierenden Zeilen ist anpassbar (Standard: 200).
        Das zu verwendende Ollama-Modell kann direkt beim Aufruf gewählt werden.
    Live-Antworten: Gibt die Analyse per Stream aus, sodass Antworten direkt erscheinen.

🛠️ Installation

Stellen Sie sicher, dass Sie Python 3 und Ollama auf Ihrem System installiert haben.

    Repository klonen:
    Bash

git clone https://DEIN-REPO-LINK
cd DEIN-REPO-NAME

Virtuelle Umgebung erstellen und aktivieren:
Bash

python3 -m venv venv
source venv/bin/activate

Abhängigkeiten installieren:
Bash

pip install -r requirements.txt

Ollama-Modell herunterladen (falls noch nicht geschehen):
Dieses Tool ist für kleinere, schnelle Modelle wie phi3 oder gemma:2b optimiert.
Bash

    ollama pull gemma:2b

🚀 Anwendung

Führen Sie das Skript von der Kommandozeile aus. Die Parameter --datei und --frage sind erforderlich.
Parameter

    --datei: Der Pfad zur Log-Datei (erforderlich).
    --frage: Die Frage, die an die Log-Daten gestellt wird (erforderlich).
    --zeilen: (Optional) Anzahl der letzten Zeilen, die analysiert werden sollen. Standard: 200.
    --model: (Optional) Name des zu verwendenden Ollama-Modells. Standard: 'llama3:8b' (oder was im Skript festgelegt ist).
    --no-stream: (Optional) Deaktiviert die direkte Streaming-Ausgabe der Antwort.

Beispiele

Einfache Analyse (mit Standardwerten):
Analysiert die letzten 200 Zeilen der syslog-Datei.
Bash

python analyse.py --datei /var/log/syslog --frage "Fasse alle Authentifizierungsfehler zusammen."

Analyse mit benutzerdefinierter Zeilenanzahl:
Analysiert die letzten 1000 Zeilen der auth.log-Datei.
Bash

python analyse.py --datei /var/log/auth.log --frage "Gab es verdächtige Anmeldeversuche von externen IPs?" --zeilen 1000

Analyse mit einem anderen Modell:
Nutzt das phi3-Modell, um die letzten 50 Zeilen einer Testdatei zu analysieren.
Bash

python analyse.py --datei test.log --frage "Was ist das dringendste Problem?" --zeilen 50 --model phi3

Beispiel-Output

🤖 Analysiere die letzten 50 Log-Zeilen mit dem Modell 'phi3'... bitte warten.

✅ Analyse-Ergebnis:

Das dringendste Problem ist der Ausfall des Dienstes 'payment_gateway', der als "CRITICAL" markiert wurde und sofortige Maßnahmen erfordert.

Zusätzlich sind zwei IP-Adressen auffällig:
1.  **192.168.1.10**: Ein 'admin' hat sich erfolgreich angemeldet.
2.  **192.168.1.25**: Es gab einen fehlgeschlagenen Authentifizierungsversuch für den Benutzer 'guest'.
