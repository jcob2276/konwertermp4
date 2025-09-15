\# 🎵 Video to MP3 Converter



Prosty konwerter plików wideo (MP4, MKV, AVI, MOV, WMV) na pliki audio MP3 z wysoką jakością.



\## 🚀 Funkcje



\- ✅ Obsługuje wiele formatów: MP4, MKV, AVI, MOV, WMV

\- ✅ Wysoką jakość audio (320k, 256k, 192k, 128k)

\- ✅ Batch processing - wszystkie pliki z folderu naraz

\- ✅ Automatyczne wykrywanie FFmpeg

\- ✅ Prosty interfejs w terminalu

\- ✅ Obsługa polskich znaków w nazwach plików



\## 📋 Wymagania



\- Python 3.6+

\- FFmpeg



\## 🔧 Instalacja



\### 1. Zainstaluj FFmpeg



\*\*Windows:\*\*

```bash

winget install ffmpeg

```



\*\*Linux:\*\*

```bash

sudo apt install ffmpeg

```



\*\*macOS:\*\*

```bash

brew install ffmpeg

```



\### 2. Pobierz kod

```bash

git clone https://github.com/jakub/video-to-mp3-converter.git

cd video-to-mp3-converter

```



\## 🎯 Użycie



1\. Uruchom program:

```bash

python ffmpeg\_konverter.py

```



2\. Podaj ścieżkę do folderu z plikami wideo



3\. Wybierz jakość audio:

&nbsp;  - `1` - 320k (najwyższa jakość)

&nbsp;  - `2` - 192k (dobra jakość) 

&nbsp;  - `3` - 128k (standardowa jakość)



4\. Program automatycznie przetworzy wszystkie pliki!



\## 📝 Przykład użycia



```

🎵 Konwerter WIDEO → MP3

===================================

✅ FFmpeg znalezione!

📂 Podaj ścieżkę do folderu z plikami wideo: C:\\Music\\Videos

🎵 Jakość:

1\. 320k (najlepsza)

Wybór (1-3): 1



🎬 Znaleziono 5 plików wideo

\[1/5] song1.mkv → song1.mp3

&nbsp;  ✅ Gotowe! (4.2 MB)

\[2/5] song2.mp4 → song2.mp3

&nbsp;  ✅ Gotowe! (3.8 MB)

...

🎉 Gotowe!

```



\## 🛠️ Rozwiązywanie problemów



\### FFmpeg nie zostało znalezione

Program automatycznie sprawdza popularne lokalizacje FFmpeg. Jeśli nadal masz problemy:



1\. Sprawdź instalację: `ffmpeg -version`

2\. Dodaj FFmpeg do PATH

3\. Lub użyj pełnej ścieżki w kodzie



\### Pliki nie są konwertowane

\- Sprawdź czy pliki mają obsługiwane rozszerzenia

\- Upewnij się że masz uprawnienia do zapisu w folderze

\- Sprawdź czy pliki nie są uszkodzone



\## 📄 Licencja



MIT License - możesz używać i modyfikować kod jak chcesz!



\## 🤝 Współpraca



Pull requesty są mile widziane! Jeśli masz pomysły na ulepszenia:



1\. Zrób fork projektu

2\. Stwórz branch (`git checkout -b feature/AmazingFeature`)

3\. Commit changes (`git commit -m 'Add some AmazingFeature'`)

4\. Push to branch (`git push origin feature/AmazingFeature`)

5\. Otwórz Pull Request



\## 📧 Kontakt



Jeśli masz pytania lub problemy, stwórz issue w tym repozytorium.



---



⭐ Jeśli projekt Ci pomógł, zostaw gwiazdkę!

