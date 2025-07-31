import os

# Minta input nama file output dari user
nama_file_output = input("Masukkan nama file output (tanpa .txt): ").strip()
if not nama_file_output:
    nama_file_output = "comen"  # fallback default
output_filename = nama_file_output + '.txt'

# Folder sumber dan folder output
source_folders = ['output_comments/feeds', 'output_comments/reels']
output_folder = 'output_file'
output_path = os.path.join(output_folder, output_filename)

# Pastikan folder output ada
os.makedirs(output_folder, exist_ok=True)

# Gabungkan semua komentar
with open(output_path, 'w', encoding='utf-8') as outfile:
    for folder in source_folders:
        for filename in os.listdir(folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(folder, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # (Opsional) Tulis nama file asal sebagai separator
                    outfile.write(f'--- {folder}/{filename} ---\n')
                    outfile.write(infile.read())
                    outfile.write('\n')

print(f"✅ Komentar berhasil digabungkan dan disimpan di: {output_path}")
