import os
import subprocess
from pathlib import Path

def convert_mp4_to_mp3(input_folder, output_folder=None, quality="320k", ffmpeg_cmd='ffmpeg'):
    """Konwertuje MP4 na MP3 używając FFmpeg"""
    
    # Ustaw folder wyjściowy
    if output_folder is None:
        output_folder = input_folder
    else:
        Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    # Znajdź pliki MKV i MP4
    video_files = []
    for f in os.listdir(input_folder):
        if f.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.wmv')):
            video_files.append(f)
    
    if not video_files:
        print(f"❌ Nie znaleziono plików wideo w folderze {input_folder}")
        return
    
    print(f"🎬 Znaleziono {len(video_files)} plików wideo")
    print(f"📂 Folder: {input_folder}")
    print(f"🎵 Jakość: {quality}")
    print("-" * 50)
    
    for i, filename in enumerate(video_files, 1):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.mp3'
        output_path = os.path.join(output_folder, output_filename)
        
        print(f"[{i}/{len(video_files)}] {filename} → {output_filename}")
        
        # Sprawdź czy plik już istnieje
        if os.path.exists(output_path):
            choice = input(f"   Plik {output_filename} istnieje. Nadpisać? (t/n): ")
            if choice.lower() not in ['t', 'tak', 'y', 'yes']:
                print(f"   ⏭️ Pominięto")
                continue
        
        try:
            # Komenda FFmpeg
            command = [
                ffmpeg_cmd, '-i', input_path,
                '-vn', '-acodec', 'mp3', '-ab', quality,
                '-y', output_path
            ]
            
            # Uruchom konwersję (bez wyświetlania szczegółów)
            subprocess.run(command, capture_output=True, check=True)
            
            # Sprawdź rozmiar
            size_mb = os.path.getsize(output_path) / (1024 * 1024)
            print(f"   ✅ Gotowe! ({size_mb:.1f} MB)")
            
        except subprocess.CalledProcessError:
            print(f"   ❌ Błąd konwersji")
        except Exception as e:
            print(f"   ❌ Błąd: {e}")

def main():
    print("🎵 Konwerter WIDEO → MP3")
    print("=" * 35)
    
    # Sprawdź FFmpeg
    ffmpeg_paths = [
        'ffmpeg',
        'C:\\ffmpeg\\bin\\ffmpeg.exe',
        'C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe',
        'C:\\Users\\jakub\\AppData\\Local\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\\ffmpeg-8.0-full_build\\bin\\ffmpeg.exe',
        'C:\\Users\\jakub\\AppData\\Local\\CapCut\\Apps\\6.6.0.2616\\ffmpeg.exe'
    ]
    
    ffmpeg_cmd = None
    for path in ffmpeg_paths:
        try:
            subprocess.run([path, '-version'], capture_output=True, check=True)
            ffmpeg_cmd = path
            print(f"✅ FFmpeg znalezione: {path}")
            break
        except:
            continue
    
    if ffmpeg_cmd is None:
        print("❌ FFmpeg niedostępne!")
        print("💡 Spróbuj zrestartować terminal lub sprawdź PATH")
        return
    
    # Pobierz folder
    folder = input("\n📂 Podaj ścieżkę do folderu z plikami wideo (MP4/MKV/AVI): ").strip().strip('"\'')
    
    if not os.path.exists(folder):
        print("❌ Folder nie istnieje!")
        return
    
    # Wybierz jakość
    print("\n🎵 Jakość:")
    print("1. 320k (najlepsza)")
    print("2. 192k (dobra)")  
    print("3. 128k (standardowa)")
    
    choice = input("Wybór (1-3): ").strip()
    quality = {'1': '320k', '2': '192k', '3': '128k'}.get(choice, '320k')
    
    # Konwertuj
    convert_mp4_to_mp3(folder, quality=quality, ffmpeg_cmd=ffmpeg_cmd)
    print("\n🎉 Gotowe!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏹️ Przerwano")
    input("\nEnter aby zakończyć...")