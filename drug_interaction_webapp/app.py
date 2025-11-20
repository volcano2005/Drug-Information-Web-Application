# app.py
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# -------------------------------
# OpenFDA URL
# -------------------------------
OPENFDA_LABEL_URL = "https://api.fda.gov/drug/label.json"


# -------------------------------
# INDIAN BRAND → GENERIC NAME MAPPING
# -------------------------------
BRAND_TO_GENERIC = {

    # Diabetes
    "glycomet": "metformin",
    "glycomet gp": "metformin glimepiride",
    "glucophage": "metformin",
    "janumet": "sitagliptin metformin",
    "galvus": "vildagliptin",
    "galvus met": "vildagliptin metformin",
    "januvia": "sitagliptin",
    "trajenta": "linagliptin",
    "istamet": "sitagliptin metformin",

    # Pain / Fever
    "dolo": "acetaminophen",
    "dolo 650": "acetaminophen",
    "calpol": "acetaminophen",
    "crocin": "acetaminophen",
    "combiflam": "ibuprofen acetaminophen",

    # Antibiotics
    "augmentin": "amoxicillin clavulanic acid",
    "zifi": "cefixime",
    "taxim o": "cefixime",
    "ciplox": "ciprofloxacin",
    "azee": "azithromycin",
    "meftal": "mefenamic acid",

    # Allergy
    "allegra": "fexofenadine",
    "cetcip": "cetirizine",
    "okacet": "cetirizine",
    "telekast": "montelukast",

    # Acidity / GERD
    "rantac": "ranitidine",
    "pan d": "pantoprazole domperidone",
    "pan": "pantoprazole",
    "omez": "omeprazole",

    # BP/Heart
    "atorva": "atorvastatin",
    "rosuvas": "rosuvastatin",
    "telma": "telmisartan",
    "amlong": "amlodipine",
    "metolar": "metoprolol",

    # Vitamins
    "neurobion": "vitamin b complex",
    "revital": "multivitamin",
    "becosules": "b complex",
    "limcee": "vitamin c",

    # Respiratory
    "asthalin": "salbutamol",
    "foracort": "budesonide formoterol",

    # Thyroid
    "eltroxin": "levothyroxine",

    # Anxiety
    "zapiz": "clonazepam",
    "nexito": "escitalopram",

    # Gastric motility
    "domstal": "domperidone"
}



# -------------------------------
# FETCH DATA FROM OPENFDA
# -------------------------------
def fetch_from_openfda(drug):

    query = f'(openfda.generic_name:"{drug}" OR openfda.substance_name:"{drug}" OR openfda.brand_name:"{drug}")'

    params = {"search": query, "limit": 1}

    try:
        response = requests.get(OPENFDA_LABEL_URL, params=params, timeout=10)

        if response.status_code == 404:
            return None

        response.raise_for_status()
        data = response.json()

        results = data.get("results")
        if results:
            return results[0]

        return None

    except:
        return None



# -------------------------------
# SAFE FIELD FETCHING
# -------------------------------
def safe_get(data, keys, default="No information available"):
    for key in keys:
        if key in data:
            val = data[key]
            if isinstance(val, list):
                return "\n\n".join(val)
            return str(val)
    return default



# -------------------------------
# EXTRACT ALL DRUG INFORMATION
# -------------------------------
def extract_info(result, drug):

    NO = "No information available"

    if not result:
        return {
            "query": drug,
            "generic": drug.title(),
            "brand": NO,
            "class": NO,
            "moa": NO,
            "indications": NO,
            "warnings": NO,
            "blackbox": NO,
            "dosage": NO,
            "description": NO,
            "contra": NO,
            "sideeffects": NO,
            "interactions": NO,
            "pregnancy": NO,
            "overdose": NO,
            "manufacturer": NO,
            "source": "No OpenFDA data found"
        }

    fda = result
    of = result.get("openfda", {})

    info = {
        "query": drug,
        "generic": ", ".join(of.get("generic_name", [NO])),
        "brand": ", ".join(of.get("brand_name", [NO])),
        "class": ", ".join(of.get("pharm_class_epc", of.get("pharm_class", [NO]))),
        "moa": safe_get(fda, ["mechanism_of_action"]),
        "indications": safe_get(fda, ["indications_and_usage"]),
        "warnings": safe_get(fda, ["warnings"]),
        "blackbox": safe_get(fda, ["boxed_warning"]),
        "dosage": safe_get(fda, ["dosage_and_administration"]),
        "description": safe_get(fda, ["description", "clinical_pharmacology"]),
        "contra": safe_get(fda, ["contraindications"]),
        "sideeffects": safe_get(fda, ["adverse_reactions"]),
        "interactions": safe_get(fda, ["drug_interactions"]),
        "pregnancy": safe_get(fda, ["pregnancy"]),
        "overdose": safe_get(fda, ["overdosage"]),
        "manufacturer": ", ".join(of.get("manufacturer_name", [NO])),
        "source": "OpenFDA"
    }

    return info



# -------------------------------
# ROUTES
# -------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():

    drug = request.form.get("drug", "").strip().lower()

    # Apply brand → generic conversion
    if drug in BRAND_TO_GENERIC:
        drug = BRAND_TO_GENERIC[drug]

    # API request
    fetched = fetch_from_openfda(drug)
    info = extract_info(fetched, drug)

    return render_template("result.html", info=info)



# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
