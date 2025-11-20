# Drug-Information-Web-Application

Drug Information Web Application

A full-stack healthcare web application built using Python Flask, OpenFDA Drug Label API, and Bootstrap UI.
Users can search any drug (generic or Indian brand names), and the app displays:

✔ Generic name
✔ Brand names
✔ Drug class
✔ Mechanism of action
✔ Indications / Uses
✔ Contraindications
✔ Side effects
✔ Warnings
✔ Black box warnings
✔ Dosage
✔ Pharmacology
✔ Interactions
✔ Pregnancy & lactation info
✔ Manufacturer

Indian brands like Dolo, Glycomet, Calpol, Zifi, Augmentin, Telma, Neurobion are automatically converted to generic names for accurate drug lookups.

🚀 Features
🔍 Search Any Drug

Enter any generic or brand name — the app fetches real FDA-approved drug label data.

🇮🇳 Indian Brand → Generic Name Conversion

Supports popular Indian medicines through a custom mapping system.

Example:

Glycomet → Metformin
Dolo 650 → Acetaminophen
Zifi → Cefixime
Augmentin → Amoxicillin + Clavulanic Acid

🔗 Real-Time Data from OpenFDA
Data fetched directly from:
https://api.fda.gov
📦 Well-Structured Information Sections
All drug information is displayed in clean vertical cards:

Generic Name

Drug Class

MOA

Indications

Side Effects

Contraindications

Dosage

Warnings

Pregnancy / Lactation

Overdose

Interactions

🎨 Responsive UI

Built with:

Bootstrap 5

Custom CSS

Mobile-friendly layout

🧩 Modular, Clean Flask Backend

API requests (requests library)

Error handling

Structured data extraction

Jinja2 templating

📂 Project Structure
drug_info_app/
│
├── app.py
├── requirements.txt
├── static/
│   └── styles.css
└── templates/
    ├── index.html
    └── result.html

🛠️ Installation & Setup
1. Clone the repo
git clone https://github.com/yourusername/drug-info-app.git
cd drug-info-app

2. Install dependencies
pip install -r requirements.txt

3. Run the Flask server
python app.py

4. Open in browser
http://127.0.0.1:5000/

🧬 Technologies Used
Backend

Python

Flask

Requests (REST API calls)

Frontend

HTML5

CSS3

Bootstrap 5

Jinja2 Templates

APIs

OpenFDA Drug Label API

Manual Indian drug brand mapper

🔥 Example Searches
Search Term	Converts To	Works?
glycomet	metformin	✔
dolo 650	acetaminophen	✔
augmentin	amoxicillin clavulanate	✔
zifi	cefixime	✔
metformin	metformin	✔
omeprazole	omeprazole	✔
ibuprofen	ibuprofen	✔
⭐ Future Improvements (Optional)

You can add these features later:

🌐 Deploy on Render / Railway

📄 PDF export of drug info

🔍 Autocomplete suggestions

🔗 Drug interaction checker (RxNorm API)

🌓 Dark mode

💾 Search history

(Ask me if you want code for any of these!)

🤝 Contributing

Pull requests are welcome!
If you want to improve UI, add Indian brand mappings, or add new features, feel free to submit a PR.

🐦 Author

K.R V V Sri Karthikeya

🎓 B.Pharmacy Student

💻 Python & Unity Game Developer

🧪 Healthcare Tech Enthusiast

🇮🇳 India

⭐ License

This project is open-source under the MIT License.
