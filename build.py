import json
import glob
import os

with open('template.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Sucht jetzt nach ALLEN .json-Dateien im Ordner
json_files = sorted(glob.glob('*.json'))

if not json_files:
    print("Keine .json Dateien gefunden.")
else:
    for jf in json_files:
        basename = os.path.splitext(jf)[0] # z. B. 'chemie_test' oder 'mathe_klasse5'
        with open(jf, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Erzeugt einen sauberen Titel aus dem Dateinamen (ersetzt _ und - durch Leerzeichen)
        nice_name = basename.replace('_', ' ').replace('-', ' ').title()
        title = f"Quiz - {nice_name}"
        
        data_js = f"const quizData = {json.dumps(data, ensure_ascii=False, indent=2)};"
        
        page = template_content.replace('/* QUIZ_TITLE */', title)
        page = page.replace('/* QUIZ_DATA_PLACEHOLDER */', data_js)
        
        out_filename = f"{basename}.html"
        with open(out_filename, 'w', encoding='utf-8') as f:
            f.write(page)
        
        print(f"Erfolgreich generiert: {out_filename} ({len(data)} Fragen)")
