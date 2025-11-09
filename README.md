## 💖 Support & Donation

If this project helps you, consider supporting the developer 🙏  

<p align="center">
  <a href="https://saweria.co/HilmiAlawi" target="_blank">
    <img src="https://img.shields.io/badge/Donate%20via-Saweria-orange?style=for-the-badge&logo=buymeacoffee&logoColor=white" alt="Donate via Saweria">
  </a>
</p>

<p align="center">
  <b>☕ Every donation keeps this project alive and improving!</b>
</p>

# 📥 IG Comment Extractor & Merger

IG Comment Extractor is a simple Python-based tool to **extract comments from Instagram posts (Reels, Feed)** and **merge them into a single file**. Perfect for social media research, sentiment analysis, and other data needs.

---

## 🚀 Key Features

- 🔗 Extract comments from multiple Instagram URLs
- 🗂️ Automatically save comments into `feeds/` and `reels/` folders
- 📄 Merge all comments into a single text file
- 🎨 Interactive terminal interface using `colorama` and `tqdm`

---

## 📁 Project Structure

```
.
├── 2file.py            # Main script to extract Instagram comments
├── cookie.py           # Contains session/cookie data from Instagram
├── gabung.py           # Script to merge all extracted comments
├── requirements.txt    # Python dependencies
├── output_comments/
│   ├── feeds/          # Comments from feed posts
│   └── reels/          # Comments from reels
└── output_file/        # Final merged comment files
```

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/HilmiAlawi/IG-Comment-Extractor.git
cd IG-Comment-Extractor
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Prepare the `cookie.py` file**

Fill in your Instagram session cookie data:

```python
sessionid = "YOUR_SESSION_ID"
ds_user_id = "YOUR_USER_ID"
csrftoken = "YOUR_CSRF_TOKEN"
mid = "YOUR_MID"
```

---

## ▶️ How to Use

### 1. Extract Instagram Comments

```bash
python 2file.py
```

- Paste one or more Instagram post URLs (feed/reel)
- Press `Enter` after each URL
- Type `done` when finished

Comments will be saved automatically in `output_comments/feeds` or `output_comments/reels`.

---

### 2. Merge All Comments

```bash
python gabung.py
```

- Enter the desired output file name
- The merged file will be saved in `output_file/`

---

## ❗ Important Notes

- You must be logged in to Instagram in a browser to get your cookie.
- Make sure the cookie is still valid and active.
- This tool is **not officially affiliated with Instagram**. Use responsibly.

---

## 🧠 Use Cases

- 📊 Social media sentiment analysis  
- 🧪 Academic research or thesis  
- 💼 Digital marketing and brand monitoring

---

## 📜 License

This project is licensed under the MIT License.  
© 2025 [Hilmi Alawi](https://github.com/HilmiAlawi)

---

📍 Tasikmalaya  
🎥 Photo & Video • 📢 Event Organizer • 📲 Digital Marketing • 📱 Social Media Handling

```
███╗   ███╗██╗██████╗  ██████╗ ███████╗████████╗██╗███████╗██╗   ██╗
████╗ ████║██║██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
██╔████╔██║██║██████╔╝██║   ██║███████╗   ██║   ██║█████╗   ╚████╔╝ 
██║╚██╔╝██║██║██╔═══╝ ██║   ██║╚════██║   ██║   ██║██╔══╝    ╚██╔╝  
██║ ╚═╝ ██║██║██║     ╚██████╔╝███████║   ██║   ██║██║        ██║   
╚═╝     ╚═╝╚═╝╚═╝      ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝        ╚═╝   
```

---

> If you find this tool useful, don't forget to ⭐ star the repo on GitHub!
