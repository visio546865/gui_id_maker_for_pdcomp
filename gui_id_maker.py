import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageTk
import math
import os
import random
import tempfile

# ==========================================
# TRANSLATIONS & LOCALIZATION DICTIONARY
# ==========================================
TRANSLATIONS = {
    "FR": {
        "title_app": "Gouvernement Central - Système d'ID v98.5",
        "sys_info": " 🏛️ SYSTÈME CENTRAL DE GESTION DES IDENTITÉS\nConfigurez le territoire, le type de badge, la langue et la mise en page.",
        "territory": "Territoire / Pays :",
        "flag_choice": "Drapeau (Auto ou Manuel) :",
        "card_name_custom": "Nom de Carte (optionnel) :",
        "card_type": "Thème / Type de Carte :",
        "layout_style": "Style / Mise en Page (Zone Sûre) :",
        "security_profile": "Profil Sécurité Graphique :",
        "security_name": "Nom Technique Sécurité :",
        "language": "Langue du Document :",
        "custom_colors": "Personnaliser les couleurs (En-tête et Bande)",
        "header_col": "Couleur En-tête",
        "stripe_col": "Couleur Bande",
        "seal_logo": "Sceau / Logo (PNG) :",
        "browse": "Parcourir...",
        "clear_seal": "Supprimer",
        "preview_btn": " [ APERCU DE LA CARTE ] ",
        "preview_title": "Apercu avant generation",
        "print_btn": " [ IMPRIMER LA CARTE OFFICIELLEMENT ] ",
        "ready": "Prêt - Gouvernement Central (Service de l'État Civil)",
        "success_title": "Gouvernement - Succès",
        "success_msg": "Document généré et certifié conforme !\nFichier enregistré sur le bureau :\n",
        "error_title": "Erreur Système 98",
        "error_msg": "Une exception est survenue lors de l'impression :\n",
        
        # Card texts translations
        "civil_title": "CARTE D'IDENTITÉ OFFICIELLE",
        "police_title": "FORCES DE L'ORDRE",
        "police_sub": "IDENTIFIANT DE POLICE OFFICIEL / BADGE",
        "fib_title": "BUREAU FÉDÉRAL D'INVESTIGATION",
        "fib_sub": "IDENTIFIANT AGENT SPÉCIAL - ",
        "ems_title": "SERVICES D'URGENCE",
        "ems_sub": "IDENTIFIANT PERSONNEL MÉDICAL",
        "mil_title": "FORCES ARMÉES",
        "mil_sub": "IDENTIFIANT PERSONNEL MILITAIRE - "
    },
    "EN": {
        "title_app": "Central Government - OS v98.5 [System ID Generator]",
        "sys_info": " 🏛️ CENTRAL IDENTITY MANAGEMENT SYSTEM\nConfigure the territory, badge type, language, and layout (Safe Zone).",
        "territory": "Territory / Country:",
        "flag_choice": "Flag (Auto or Manual):",
        "card_name_custom": "Card Name (optional):",
        "card_type": "Theme / Card Type:",
        "layout_style": "Style / Layout (Safe Zone):",
        "security_profile": "Graphic Security Profile:",
        "security_name": "Security Technical Name:",
        "language": "Document Language:",
        "custom_colors": "Customize colors (Header & Stripe)",
        "header_col": "Header Color",
        "stripe_col": "Stripe Color",
        "seal_logo": "Seal / Logo (PNG):",
        "browse": "Browse...",
        "clear_seal": "Clear",
        "preview_btn": " [ PREVIEW CARD ] ",
        "preview_title": "Preview Before Generation",
        "print_btn": " [ PRINT CARD OFFICIALLY ] ",
        "ready": "Ready - Central Government (Civil Status Service)",
        "success_title": "Government - Success",
        "success_msg": "Document generated and certified compliant!\nFile saved on desktop:\n",
        "error_title": "System Error 98",
        "error_msg": "An exception occurred during printing:\n",
        
        "civil_title": "OFFICIAL IDENTIFICATION CARD",
        "police_title": "LAW ENFORCEMENT",
        "police_sub": "OFFICIAL POLICE CREDENTIAL / BADGE ID",
        "fib_title": "FEDERAL INVESTIGATION BUREAU",
        "fib_sub": "SPECIAL AGENT CREDENTIAL - ",
        "ems_title": "EMERGENCY SERVICES",
        "ems_sub": "MEDICAL PERSONNEL CREDENTIAL",
        "mil_title": "U.S. ARMED FORCES",
        "mil_sub": "MILITARY PERSONNEL ID - "
    },
    "DE": {
        "title_app": "Zentralregierung - OS v98.5 [System-ID-Generator]",
        "sys_info": " 🏛️ ZENTRALES IDENTITÄTSVERWALTUNGSSYSTEM\nKonfigurieren Sie Gebiet, Ausweistyp, Sprache und Layout.",
        "territory": "Gebiet / Land:",
        "flag_choice": "Flagge (Auto oder Manuell):",
        "card_name_custom": "Kartenname (optional):",
        "card_type": "Thema / Kartentyp:",
        "layout_style": "Stil / Layout (Sicherer Bereich):",
        "security_profile": "Grafisches Sicherheitsprofil:",
        "security_name": "Technischer Sicherheitsname:",
        "language": "Dokumentensprache:",
        "custom_colors": "Farben anpassen (Kopfzeile & Streifen)",
        "header_col": "Kopfzeilenfarbe",
        "stripe_col": "Streifenfarbe",
        "seal_logo": "Siegel / Logo (PNG):",
        "browse": "Durchsuchen...",
        "clear_seal": "Loschen",
        "preview_btn": " [ KARTENVORSCHAU ] ",
        "preview_title": "Vorschau vor dem Erstellen",
        "print_btn": " [ KARTE OFFIZIELL DRUCKEN ] ",
        "ready": "Bereit - Zentralregierung (Standesamt)",
        "success_title": "Regierung - Erfolg",
        "success_msg": "Dokument generiert und konform zertifiziert!\nDatei gespeichert auf dem Desktop:\n",
        "error_title": "Systemfehler 98",
        "error_msg": "Beim Drucken ist ein Fehler aufgetreten:\n",
        
        "civil_title": "OFFIZIELLER AUSWEIS",
        "police_title": "STRAFVERFOLGUNGSBEHÖRDE",
        "police_sub": "OFFIZIELLER POLIZEiausweis / DIENSTMARKE",
        "fib_title": "BUNDESERMITTLUNGSBÜRO",
        "fib_sub": "SONDERAGENTEN-AUSWEIS - ",
        "ems_title": "NOTDIENSTE",
        "ems_sub": "MEDIZINISCHES PERSONAL AUSWEIS",
        "mil_title": "STREITKRÄFTE",
        "mil_sub": "MILITÄRISCHER AUSWEIS - "
    },
    "ES": {
        "title_app": "Gobierno Central - OS v98.5 [Generador de ID]",
        "sys_info": " 🏛️ SISTEMA CENTRAL DE GESTIÓN DE IDENTIDAD\nConfigure el territorio, tipo de credencial, idioma y diseño.",
        "territory": "Territorio / País:",
        "flag_choice": "Bandera (Auto o Manual):",
        "card_name_custom": "Nombre de Tarjeta (opcional):",
        "card_type": "Tema / Tipo de Tarjeta:",
        "layout_style": "Estilo / Diseño (Zona Segura):",
        "security_profile": "Perfil de Seguridad Gráfica:",
        "security_name": "Nombre Técnico de Seguridad:",
        "language": "Idioma del Documento:",
        "custom_colors": "Personalizar colores (Encabezado y Banda)",
        "header_col": "Color Encabezado",
        "stripe_col": "Color Banda",
        "seal_logo": "Sello / Logo (PNG):",
        "browse": "Examinar...",
        "clear_seal": "Quitar",
        "preview_btn": " [ VISTA PREVIA DE TARJETA ] ",
        "preview_title": "Vista previa antes de generar",
        "print_btn": " [ IMPRIMIR TARJETA OFICIALMENTE ] ",
        "ready": "Listo - Gobierno Central (Servicio de Estado Civil)",
        "success_title": "Gobierno - Éxito",
        "success_msg": "¡Documento generado y certificado conforme!\nArchivo guardado en el escritorio:\n",
        "error_title": "Error de Sistema 98",
        "error_msg": "Ocurrió una excepción durante la impresión:\n",
        
        "civil_title": "TARJETA DE IDENTIFICACIÓN OFICIAL",
        "police_title": "FUERZAS DEL ORDEN",
        "police_sub": "CREDENCIAL OFICIAL DE POLICÍA / PLACA",
        "fib_title": "BUREAU FEDERAL DE INVESTIGACIÓN",
        "fib_sub": "CREDENCIAL DE AGENTE ESPECIAL - ",
        "ems_title": "SERVICIOS DE EMERGENCIA",
        "ems_sub": "CREDENCIAL DE PERSONAL MÉDICO",
        "mil_title": "FUERZAS ARMADAS",
        "mil_sub": "CREDENCIAL DE PERSONAL MILITAR - "
    }
}

STATES_CONFIG = {
    "SAN ANDREAS": {
        "flag": "USA",
        "primary_header": (20, 35, 60, 255),
        "accent_stripe": (200, 160, 40, 255),
        "gradient_c1": (220, 235, 250, 255),
        "gradient_c2": (180, 205, 235, 255),
        "guilloche_color": (70, 90, 130, 90),
        "rosette_color": (40, 80, 150, 50),
        "symbols": ["🛡️", "★", "⚖️"]
    },
    "LIBERTY CITY": {
        "flag": "USA",
        "primary_header": (50, 50, 50, 255),
        "accent_stripe": (210, 80, 30, 255),
        "gradient_c1": (240, 240, 240, 255),
        "gradient_c2": (205, 210, 215, 255),
        "guilloche_color": (100, 100, 110, 90),
        "rosette_color": (120, 120, 130, 50),
        "symbols": ["🗽", "⚙️", "🏢"]
    },
    "NORTH YANKTON": {
        "flag": "USA",
        "primary_header": (40, 70, 90, 255),
        "accent_stripe": (220, 220, 220, 255),
        "gradient_c1": (225, 238, 245, 255),
        "gradient_c2": (195, 215, 230, 255),
        "guilloche_color": (90, 120, 150, 90),
        "rosette_color": (70, 110, 140, 50),
        "symbols": ["❄️", "🌲", "⛄"]
    },
    "VICE CITY": {
        "flag": "USA",
        "primary_header": (120, 30, 90, 255),
        "accent_stripe": (240, 180, 40, 255),
        "gradient_c1": (255, 230, 245, 255),
        "gradient_c2": (245, 200, 225, 255),
        "guilloche_color": (150, 80, 130, 90),
        "rosette_color": (200, 70, 150, 50),
        "symbols": ["🌴", "☀️", "🌊"]
    },
    "ALDERNEY": {
        "flag": "USA",
        "primary_header": (60, 70, 60, 255),
        "accent_stripe": (180, 140, 50, 255),
        "gradient_c1": (230, 235, 225, 255),
        "gradient_c2": (200, 210, 195, 255),
        "guilloche_color": (90, 110, 90, 90),
        "rosette_color": (80, 110, 80, 50),
        "symbols": ["🌾", "🚜", "🏡"]
    },
    "GLORIANA": {
        "flag": "USA",
        "primary_header": (80, 40, 100, 255),
        "accent_stripe": (210, 180, 90, 255),
        "gradient_c1": (245, 235, 250, 255),
        "gradient_c2": (225, 210, 235, 255),
        "guilloche_color": (110, 80, 130, 90),
        "rosette_color": (120, 70, 140, 50),
        "symbols": ["⚜️", "💠", "⚡"]
    },
    "LEONIDA": {
        "flag": "USA",
        "primary_header": (150, 70, 30, 255),
        "accent_stripe": (40, 140, 180, 255),
        "gradient_c1": (255, 240, 225, 255),
        "gradient_c2": (245, 215, 190, 255),
        "guilloche_color": (140, 90, 60, 90),
        "rosette_color": (160, 90, 60, 50),
        "symbols": ["🐊", "🍊", "⛵"]
    },
    "FORT ZANCUNDO": {
        "flag": "USA",
        "primary_header": (45, 55, 35, 255),
        "accent_stripe": (210, 175, 40, 255),
        "gradient_c1": (225, 230, 215, 255),
        "gradient_c2": (200, 210, 190, 255),
        "guilloche_color": (80, 95, 65, 90),
        "rosette_color": (70, 90, 60, 50),
        "symbols": ["⭐", "🎖️", "✈️"]
    },
    "CANADA": {
        "flag": "Canada",
        "primary_header": (160, 25, 25, 255),
        "accent_stripe": (255, 255, 255, 255),
        "gradient_c1": (245, 230, 230, 255),
        "gradient_c2": (220, 195, 195, 255),
        "guilloche_color": (150, 50, 50, 90),
        "rosette_color": (160, 40, 40, 50),
        "symbols": ["🍁", "❄️", "🏔️"]
    },
    "MEXICO": {
        "flag": "Mexico",
        "primary_header": (0, 104, 71, 255),
        "accent_stripe": (206, 17, 38, 255),
        "gradient_c1": (230, 245, 235, 255),
        "gradient_c2": (200, 225, 210, 255),
        "guilloche_color": (30, 110, 70, 90),
        "rosette_color": (20, 90, 50, 50),
        "symbols": ["🌵", "☀️", "🦅"]
    },
    "CUBA": {
        "flag": "Cuba",
        "primary_header": (0, 45, 98, 255),
        "accent_stripe": (206, 17, 38, 255),
        "gradient_c1": (220, 235, 250, 255),
        "gradient_c2": (185, 210, 235, 255),
        "guilloche_color": (20, 70, 130, 90),
        "rosette_color": (10, 50, 110, 50),
        "symbols": ["⭐", "🌴", "🎺"]
    },
    "FRANCE": {
        "flag": "France",
        "primary_header": (0, 85, 164, 255),
        "accent_stripe": (239, 65, 53, 255),
        "gradient_c1": (230, 240, 250, 255),
        "gradient_c2": (205, 220, 240, 255),
        "guilloche_color": (50, 100, 160, 90),
        "rosette_color": (30, 80, 140, 50),
        "symbols": ["⚜️", "🍷", "🗼"]
    },
    "UNITED KINGDOM": {
        "flag": "United Kingdom",
        "primary_header": (1, 33, 105, 255),
        "accent_stripe": (200, 16, 46, 255),
        "gradient_c1": (220, 228, 245, 255),
        "gradient_c2": (190, 205, 230, 255),
        "guilloche_color": (40, 70, 130, 90),
        "rosette_color": (20, 50, 110, 50),
        "symbols": ["👑", "🦁", "☕"]
    }
}

DEFAULT_STATE = STATES_CONFIG["SAN ANDREAS"]

SECURITY_PROFILES = {
    "Basic": {"density": 0.75, "alpha": 0.70, "rosette_centers": 1, "picto": 0.70, "tech_name": "BASIC-LINE V1", "art_style": "clean_lines"},
    "Standard": {"density": 1.0, "alpha": 1.0, "rosette_centers": 2, "picto": 1.0, "tech_name": "GUILLOCHE MATRIX V1", "art_style": "abstract_rosette"},
    "Advanced": {"density": 1.25, "alpha": 1.20, "rosette_centers": 3, "picto": 1.20, "tech_name": "ADV-ROSETTE GRID V2", "art_style": "terrain_contours"},
    "Ultra": {"density": 1.45, "alpha": 1.35, "rosette_centers": 4, "picto": 1.35, "tech_name": "ULTRA-MICROTEXT V3", "art_style": "abstract_rosette"},
    "Banknote": {"density": 1.35, "alpha": 1.25, "rosette_centers": 4, "picto": 1.10, "tech_name": "BANKNOTE GUILLOCHE X9", "art_style": "abstract_rosette"},
    "Government High": {"density": 1.15, "alpha": 1.05, "rosette_centers": 3, "picto": 1.10, "tech_name": "GOV-SEAL LAYER PRIME", "art_style": "maritime_grid"},
    "Minimal Clean": {"density": 0.85, "alpha": 0.80, "rosette_centers": 1, "picto": 0.60, "tech_name": "MIN-CLEAN SECURE 02", "art_style": "clean_lines"},
    "Tactical": {"density": 1.10, "alpha": 1.15, "rosette_centers": 2, "picto": 0.95, "tech_name": "TACTICAL BADGE NET V4", "art_style": "terrain_contours"},
    "Continental": {"density": 1.0, "alpha": 0.85, "rosette_centers": 2, "picto": 0.75, "tech_name": "CONTINENT SILHOUETTE L2", "art_style": "europe_silhouette"},
    "Coastal": {"density": 0.95, "alpha": 0.82, "rosette_centers": 2, "picto": 0.72, "tech_name": "COASTLINE WAVEMAP K5", "art_style": "coastal_lines"},
    "Agricultural": {"density": 0.92, "alpha": 0.80, "rosette_centers": 2, "picto": 0.70, "tech_name": "AGRO PARCEL GRID F3", "art_style": "agri_field_real"},
    "Rosace Abstract": {"density": 1.05, "alpha": 0.90, "rosette_centers": 3, "picto": 0.78, "tech_name": "ROSACE FRACTAL R8", "art_style": "abstract_rosette"},
    "Terrain Relief": {"density": 1.0, "alpha": 0.86, "rosette_centers": 2, "picto": 0.75, "tech_name": "RELIEF CONTOUR T4", "art_style": "terrain_contours"},
    "Maritime": {"density": 0.95, "alpha": 0.84, "rosette_centers": 2, "picto": 0.74, "tech_name": "HARBOR GRID M6", "art_style": "boats_water"},
    "Europe Silhouette": {"density": 0.95, "alpha": 0.82, "rosette_centers": 2, "picto": 0.70, "tech_name": "EUROPE WATERMARK E1", "art_style": "europe_silhouette"},
    "USA Silhouette": {"density": 0.95, "alpha": 0.82, "rosette_centers": 2, "picto": 0.70, "tech_name": "USA WATERMARK U1", "art_style": "usa_silhouette"},
    "Boats On Water": {"density": 0.95, "alpha": 0.82, "rosette_centers": 2, "picto": 0.72, "tech_name": "MARINE BOATLINE B2", "art_style": "boats_water"},
    "Field Parcels": {"density": 0.92, "alpha": 0.80, "rosette_centers": 2, "picto": 0.70, "tech_name": "FARMLAND PARCEL P1", "art_style": "agri_field_real"}
}

def scale_alpha(color, factor):
    r, g, b, a = color
    scaled = max(0, min(255, int(a * factor)))
    return (r, g, b, scaled)

def create_guilloche_pattern(width, height, color_primary, color_secondary=(150, 180, 220, 40), pattern_type="standard", density=1.0, alpha_factor=1.0):
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    step = max(6, int(16 / density))
    color_primary = scale_alpha(color_primary, alpha_factor)
    color_secondary = scale_alpha(color_secondary, alpha_factor)
    if pattern_type == "civil":
        for x in range(0, width + height, step):
            points = []
            for y in range(0, height, 4):
                offset_x = x + int(20 * math.sin(y / 20.0))
                points.append((offset_x, y))
            if len(points) > 1:
                draw.line(points, fill=color_primary, width=1)
    elif pattern_type in ["police", "military", "fib", "ems"]:
        for x in range(0, width + height, step - 2):
            points = []
            for y in range(0, height, 6):
                offset_x = x + int(12 * math.cos(y / 15.0) * math.sin(y / 10.0))
                points.append((offset_x, y))
            if len(points) > 1:
                draw.line(points, fill=color_primary, width=1)
    spacing = max(12, int(30 / density))
    for i in range(-height, width + height, spacing):
        draw.line([(i, 0), (i + height, height)], fill=color_secondary, width=1)
        draw.line([(i + height, 0), (i, height)], fill=color_secondary, width=1)
    return overlay

def create_security_background_gradient(width, height, state_data):
    gradient = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(gradient)
    c1 = state_data["gradient_c1"]
    c2 = state_data["gradient_c2"]
    for y in range(height):
        r = int(c1[0] + (c2[0] - c1[0]) * (y / height))
        g = int(c1[1] + (c2[1] - c1[1]) * (y / height))
        b = int(c1[2] + (c2[2] - c1[2]) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))
    return gradient

def add_security_rosettes(width, height, state_data, density=1.0, alpha_factor=1.0, center_count=2):
    rosette_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(rosette_layer)
    rosette_color = scale_alpha(state_data["rosette_color"], alpha_factor)
    centers_base = [
        (width - 180, height - 150),
        (200, height - 120),
        (width // 2, height - 110),
        (width - 320, height // 2 + 70)
    ]
    centers = centers_base[:max(1, min(len(centers_base), center_count))]
    for cx, cy in centers:
        radius = int(120 * density)
        for r in range(10, radius, max(4, int(8 / density))):
            draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=rosette_color, width=1)
    return rosette_layer

def add_security_pictograms(width, height, state_data, density=1.0, alpha_factor=1.0):
    picto_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(picto_layer)
    try:
        font_picto = ImageFont.truetype("seguiym.ttf", 20)
    except IOError:
        font_picto = ImageFont.load_default()
    symbols = state_data.get("symbols", ["🏛️", "★", "👣"])
    rows = max(5, int(8 * density))
    cols = max(10, int(16 * density))
    step_x = width // cols
    step_y = height // rows
    picto_alpha = max(10, min(100, int(35 * alpha_factor)))
    for r in range(rows):
        for c in range(cols):
            x = c * step_x + (step_x // 2)
            y = r * step_y + (step_y // 2)
            symbol = symbols[(r + c) % len(symbols)]
            draw.text((x, y), symbol, fill=(50, 50, 100, picto_alpha), font=font_picto, anchor="mm")
    return picto_layer

def add_center_safe_zone_overlay(width, height, max_alpha=92, radius_factor=0.86):
    # Build a soft radial mask then upscale for a smooth "safe zone" fade.
    small_w, small_h = 220, 150
    mask_small = Image.new("L", (small_w, small_h), 0)
    pix = mask_small.load()
    cx, cy = small_w / 2.0, small_h / 2.0
    max_dist = min(cx, cy) * max(0.4, min(1.0, radius_factor))

    for y in range(small_h):
        for x in range(small_w):
            dx = (x - cx) / max_dist
            dy = (y - cy) / max_dist
            d2 = dx * dx + dy * dy
            if d2 < 1.0:
                # Smoother curve near edges to avoid visible ring boundaries.
                alpha = int(max_alpha * ((1.0 - d2) ** 1.8))
                pix[x, y] = max(0, min(255, alpha))

    resample = Image.Resampling.BICUBIC if hasattr(Image, "Resampling") else Image.BICUBIC
    mask = mask_small.resize((width, height), resample)

    overlay = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    overlay.putalpha(mask)
    return overlay

def add_security_thematic_layer(width, height, state_data, art_style="abstract_rosette", density=1.0, alpha_factor=1.0):
    theme_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(theme_layer)
    line_alpha = max(12, min(44, int(22 * alpha_factor)))
    accent_alpha = max(16, min(56, int(30 * alpha_factor)))
    base_primary = state_data["guilloche_color"]
    base_secondary = state_data["rosette_color"]
    primary = (base_primary[0], base_primary[1], base_primary[2], line_alpha)
    secondary = (base_secondary[0], base_secondary[1], base_secondary[2], accent_alpha)

    if art_style == "continent_silhouette":
        # Soft map-like silhouette watermark in the left-center area.
        main_land = [
            (width * 0.20, height * 0.54), (width * 0.30, height * 0.44), (width * 0.43, height * 0.43),
            (width * 0.51, height * 0.49), (width * 0.49, height * 0.61), (width * 0.36, height * 0.66),
            (width * 0.25, height * 0.62)
        ]
        draw.polygon(main_land, fill=(primary[0], primary[1], primary[2], int(primary[3] * 0.45)), outline=secondary)
    elif art_style == "europe_silhouette":
        europe_poly = [
            (width * 0.18, height * 0.48), (width * 0.24, height * 0.42), (width * 0.31, height * 0.40),
            (width * 0.39, height * 0.42), (width * 0.43, height * 0.47), (width * 0.41, height * 0.53),
            (width * 0.36, height * 0.57), (width * 0.30, height * 0.56), (width * 0.25, height * 0.60),
            (width * 0.20, height * 0.57), (width * 0.18, height * 0.52)
        ]
        draw.polygon(europe_poly, fill=(primary[0], primary[1], primary[2], int(primary[3] * 0.45)), outline=secondary)
        draw.ellipse([(width * 0.33, height * 0.35), (width * 0.37, height * 0.39)], fill=(primary[0], primary[1], primary[2], int(primary[3] * 0.35)))
    elif art_style == "usa_silhouette":
        usa_poly = [
            (width * 0.16, height * 0.56), (width * 0.22, height * 0.50), (width * 0.31, height * 0.49),
            (width * 0.42, height * 0.50), (width * 0.50, height * 0.55), (width * 0.54, height * 0.60),
            (width * 0.47, height * 0.64), (width * 0.36, height * 0.65), (width * 0.27, height * 0.62),
            (width * 0.19, height * 0.61)
        ]
        draw.polygon(usa_poly, fill=(primary[0], primary[1], primary[2], int(primary[3] * 0.45)), outline=secondary)
        draw.ellipse([(width * 0.56, height * 0.60), (width * 0.60, height * 0.64)], fill=(primary[0], primary[1], primary[2], int(primary[3] * 0.35)))
    elif art_style == "coastal_lines":
        coast_step = max(14, int(30 / density))
        for base_y in range(int(height * 0.34), int(height * 0.78), coast_step):
            points = []
            for x in range(0, width, 8):
                y = base_y + int(8 * math.sin(x / 88.0) + 4 * math.cos(x / 37.0))
                points.append((x, y))
            if len(points) > 1:
                draw.line(points, fill=primary, width=1)
        boat = [(width * 0.64, height * 0.58), (width * 0.72, height * 0.58), (width * 0.69, height * 0.62), (width * 0.61, height * 0.62)]
        draw.polygon(boat, outline=secondary, fill=(secondary[0], secondary[1], secondary[2], int(secondary[3] * 0.35)))
    elif art_style == "agri_parcels":
        grid_x = max(58, int(120 / density))
        grid_y = max(46, int(96 / density))
        for x in range(int(width * 0.12), int(width * 0.88), grid_x):
            for y in range(int(height * 0.30), int(height * 0.82), grid_y):
                draw.rectangle([(x, y), (x + grid_x - 10, y + grid_y - 10)], outline=primary, width=1)
    elif art_style == "agri_field_real":
        horizon = int(height * 0.47)
        center_x = int(width * 0.52)
        for i in range(1, 12):
            x_off = int((width * 0.43) * (i / 12.0))
            draw.line([(center_x, horizon), (center_x - x_off, height)], fill=primary, width=1)
            draw.line([(center_x, horizon), (center_x + x_off, height)], fill=primary, width=1)
        for y in range(horizon + 24, height, 22):
            draw.line([(center_x - int((y - horizon) * 1.15), y), (center_x + int((y - horizon) * 1.15), y)], fill=secondary, width=1)
        barn = [(width * 0.73, height * 0.52), (width * 0.77, height * 0.49), (width * 0.81, height * 0.52), (width * 0.81, height * 0.57), (width * 0.73, height * 0.57)]
        draw.polygon(barn, outline=secondary, fill=(secondary[0], secondary[1], secondary[2], int(secondary[3] * 0.30)))
    elif art_style == "terrain_contours":
        ring_count = max(5, int(10 * density))
        for i in range(ring_count):
            offset = i * 14
            contour = []
            for x in range(int(width * 0.05), int(width * 0.95), 9):
                y = int(height * 0.56 + 28 * math.sin((x + offset) / 120.0) + 10 * math.cos((x - offset) / 63.0) + (i - ring_count / 2) * 9)
                contour.append((x, y))
            draw.line(contour, fill=primary if i % 2 == 0 else secondary, width=1)
    elif art_style == "maritime_grid":
        cx, cy = int(width * 0.80), int(height * 0.70)
        for r in range(45, int(185 * density), max(18, int(34 / density))):
            draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=primary, width=1)
        for a in range(0, 180, 18):
            rad = math.radians(a)
            x2 = cx + int(190 * math.cos(rad))
            y2 = cy - int(190 * math.sin(rad))
            draw.line([(cx, cy), (x2, y2)], fill=secondary, width=1)
    elif art_style == "boats_water":
        for base_y in range(int(height * 0.52), int(height * 0.84), 20):
            wave = []
            for x in range(int(width * 0.45), width, 8):
                y = base_y + int(5 * math.sin(x / 55.0))
                wave.append((x, y))
            draw.line(wave, fill=primary, width=1)
        boats = [
            [(width * 0.67, height * 0.58), (width * 0.76, height * 0.58), (width * 0.73, height * 0.62), (width * 0.64, height * 0.62)],
            [(width * 0.79, height * 0.66), (width * 0.86, height * 0.66), (width * 0.84, height * 0.69), (width * 0.77, height * 0.69)]
        ]
        for hull in boats:
            draw.polygon(hull, outline=secondary, fill=(secondary[0], secondary[1], secondary[2], int(secondary[3] * 0.35)))
        draw.line([(width * 0.72, height * 0.58), (width * 0.72, height * 0.52)], fill=secondary, width=1)
        draw.polygon([(width * 0.72, height * 0.52), (width * 0.75, height * 0.55), (width * 0.72, height * 0.55)], fill=(secondary[0], secondary[1], secondary[2], int(secondary[3] * 0.40)))
    elif art_style == "abstract_rosette":
        centers = [(int(width * 0.80), int(height * 0.70))]
        for cx, cy in centers:
            for r in range(28, int(135 * density), max(12, int(22 / density))):
                draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=primary, width=1)
            for a in range(0, 360, 24):
                rad = math.radians(a)
                x2 = cx + int(132 * math.cos(rad))
                y2 = cy + int(132 * math.sin(rad))
                draw.line([(cx, cy), (x2, y2)], fill=secondary, width=1)
    else:
        for i in range(-height, width, 36):
            draw.line([(i, 0), (i + height, height)], fill=primary, width=1)

    return theme_layer.filter(ImageFilter.GaussianBlur(0.9))

def add_flag_badge(card, width, height, flag_type="USA", position="top_right"):
    flag_w, flag_h = 90, 55
    if position == "top_left":
        flag_x = 40
        flag_y = 28
    elif position == "center":
        flag_x = width // 2 - 45
        flag_y = 28
    elif position == "bottom_right":
        flag_x = width - 130
        flag_y = height - 80
    else:
        flag_x = width - 130
        flag_y = 28
        
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle([(flag_x, flag_y), (flag_x + flag_w, flag_y + flag_h)], radius=6, fill=(255, 255, 255, 220), outline=(200, 200, 200, 255), width=1)

    x1, y1 = flag_x + 2, flag_y + 2
    x2, y2 = flag_x + flag_w - 2, flag_y + flag_h - 2
    w, h = x2 - x1, y2 - y1

    def draw_vertical_tricolor(c1, c2, c3):
        draw.rectangle([(x1, y1), (x1 + int(w / 3), y2)], fill=c1)
        draw.rectangle([(x1 + int(w / 3), y1), (x1 + int(2 * w / 3), y2)], fill=c2)
        draw.rectangle([(x1 + int(2 * w / 3), y1), (x2, y2)], fill=c3)

    def draw_horizontal_tricolor(c1, c2, c3):
        draw.rectangle([(x1, y1), (x2, y1 + int(h / 3))], fill=c1)
        draw.rectangle([(x1, y1 + int(h / 3)), (x2, y1 + int(2 * h / 3))], fill=c2)
        draw.rectangle([(x1, y1 + int(2 * h / 3)), (x2, y2)], fill=c3)

    def draw_horizontal_bicolor(c1, c2):
        draw.rectangle([(x1, y1), (x2, y1 + int(h / 2))], fill=c1)
        draw.rectangle([(x1, y1 + int(h / 2)), (x2, y2)], fill=c2)

    def draw_nordic_cross(bg, cross, inner=None):
        draw.rectangle([(x1, y1), (x2, y2)], fill=bg)
        if inner:
            draw.rectangle([(x1 + int(w * 0.28), y1), (x1 + int(w * 0.42), y2)], fill=inner)
            draw.rectangle([(x1, y1 + int(h * 0.42)), (x2, y1 + int(h * 0.58))], fill=inner)
        draw.rectangle([(x1 + int(w * 0.31), y1), (x1 + int(w * 0.39), y2)], fill=cross)
        draw.rectangle([(x1, y1 + int(h * 0.45)), (x2, y1 + int(h * 0.55))], fill=cross)

    if flag_type == "USA":
        stripe_h = h / 7
        colors_flag = [(180, 30, 30, 230), (255, 255, 255, 230)]
        for i in range(7):
            color = colors_flag[i % 2]
            draw.rectangle([(x1, y1 + int(i * stripe_h)), (x2, y1 + int((i + 1) * stripe_h))], fill=color)
        draw.rectangle([(x1, y1), (x1 + int(w * 0.45), y1 + int(h * 0.55))], fill=(20, 40, 100, 240))
    elif flag_type == "Canada":
        draw_vertical_tricolor((200, 20, 30, 240), (255, 255, 255, 240), (200, 20, 30, 240))
    elif flag_type == "Mexico":
        draw_vertical_tricolor((0, 104, 71, 240), (255, 255, 255, 240), (206, 17, 38, 240))
    elif flag_type == "Cuba":
        stripe_h = h / 5
        colors = [(0, 45, 98, 240), (255, 255, 255, 240), (0, 45, 98, 240), (255, 255, 255, 240), (0, 45, 98, 240)]
        for i in range(5):
            draw.rectangle([(x1, y1 + int(i * stripe_h)), (x2, y1 + int((i + 1) * stripe_h))], fill=colors[i])
        draw.polygon([(x1, y1), (x1 + int(w * 0.45), y1 + int(h * 0.5)), (x1, y2)], fill=(206, 17, 38, 255))
    elif flag_type == "France":
        draw_vertical_tricolor((0, 85, 164, 240), (255, 255, 255, 240), (239, 65, 53, 240))
    elif flag_type == "United Kingdom":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(1, 33, 105, 240))
        draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255, 255), width=5)
        draw.line([(x1, y2), (x2, y1)], fill=(255, 255, 255, 255), width=5)
        cx, cy = x1 + int(w / 2), y1 + int(h / 2)
        draw.line([(x1, cy), (x2, cy)], fill=(255, 255, 255, 255), width=9)
        draw.line([(cx, y1), (cx, y2)], fill=(255, 255, 255, 255), width=9)
    elif flag_type == "Germany":
        draw_horizontal_tricolor((0, 0, 0, 240), (220, 0, 0, 240), (255, 206, 0, 240))
    elif flag_type == "Italy":
        draw_vertical_tricolor((0, 140, 69, 240), (255, 255, 255, 240), (205, 33, 42, 240))
    elif flag_type == "Spain":
        draw.rectangle([(x1, y1), (x2, y1 + int(h * 0.25))], fill=(198, 0, 43, 240))
        draw.rectangle([(x1, y1 + int(h * 0.25)), (x2, y1 + int(h * 0.75))], fill=(255, 204, 0, 240))
        draw.rectangle([(x1, y1 + int(h * 0.75)), (x2, y2)], fill=(198, 0, 43, 240))
    elif flag_type == "Portugal":
        draw.rectangle([(x1, y1), (x1 + int(w * 0.4), y2)], fill=(0, 102, 0, 240))
        draw.rectangle([(x1 + int(w * 0.4), y1), (x2, y2)], fill=(206, 17, 38, 240))
    elif flag_type == "Belgium":
        draw_vertical_tricolor((0, 0, 0, 240), (253, 218, 36, 240), (239, 51, 64, 240))
    elif flag_type == "Netherlands":
        draw_horizontal_tricolor((174, 28, 40, 240), (255, 255, 255, 240), (33, 70, 139, 240))
    elif flag_type == "Ireland":
        draw_vertical_tricolor((22, 155, 98, 240), (255, 255, 255, 240), (255, 130, 0, 240))
    elif flag_type == "Sweden":
        draw_nordic_cross((0, 82, 147, 240), (255, 205, 0, 240))
    elif flag_type == "Norway":
        draw_nordic_cross((186, 12, 47, 240), (0, 32, 91, 240), inner=(255, 255, 255, 240))
    elif flag_type == "Finland":
        draw_nordic_cross((255, 255, 255, 240), (0, 53, 128, 240))
    elif flag_type == "Denmark":
        draw_nordic_cross((198, 12, 48, 240), (255, 255, 255, 240))
    elif flag_type == "Switzerland":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(218, 41, 28, 240))
        draw.rectangle([(x1 + int(w * 0.42), y1 + int(h * 0.25)), (x1 + int(w * 0.58), y1 + int(h * 0.75))], fill=(255, 255, 255, 240))
        draw.rectangle([(x1 + int(w * 0.30), y1 + int(h * 0.42)), (x1 + int(w * 0.70), y1 + int(h * 0.58))], fill=(255, 255, 255, 240))
    elif flag_type == "Austria":
        draw_horizontal_tricolor((220, 20, 60, 240), (255, 255, 255, 240), (220, 20, 60, 240))
    elif flag_type == "Poland":
        draw_horizontal_bicolor((255, 255, 255, 240), (220, 20, 60, 240))
    elif flag_type == "Ukraine":
        draw_horizontal_bicolor((0, 87, 183, 240), (255, 215, 0, 240))
    elif flag_type == "Romania":
        draw_vertical_tricolor((0, 43, 127, 240), (252, 209, 22, 240), (206, 17, 38, 240))
    elif flag_type == "Greece":
        stripe_h = h / 9
        for i in range(9):
            color = (13, 94, 175, 240) if i % 2 == 0 else (255, 255, 255, 240)
            draw.rectangle([(x1, y1 + int(i * stripe_h)), (x2, y1 + int((i + 1) * stripe_h))], fill=color)
        canton_w = int(w * 0.42)
        canton_h = int(h * 0.55)
        draw.rectangle([(x1, y1), (x1 + canton_w, y1 + canton_h)], fill=(13, 94, 175, 240))
        draw.rectangle([(x1 + int(canton_w * 0.42), y1), (x1 + int(canton_w * 0.58), y1 + canton_h)], fill=(255, 255, 255, 240))
        draw.rectangle([(x1, y1 + int(canton_h * 0.42)), (x1 + canton_w, y1 + int(canton_h * 0.58))], fill=(255, 255, 255, 240))
    elif flag_type == "Turkey":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(227, 10, 23, 240))
        cx, cy = x1 + int(w * 0.40), y1 + int(h * 0.50)
        r1, r2 = int(h * 0.20), int(h * 0.16)
        draw.ellipse([(cx - r1, cy - r1), (cx + r1, cy + r1)], fill=(255, 255, 255, 240))
        draw.ellipse([(cx - r2 + int(h * 0.06), cy - r2), (cx + r2 + int(h * 0.06), cy + r2)], fill=(227, 10, 23, 240))
    elif flag_type == "Russia":
        draw_horizontal_tricolor((255, 255, 255, 240), (0, 57, 166, 240), (213, 43, 30, 240))
    elif flag_type == "Japan":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(255, 255, 255, 240))
        r = int(h * 0.28)
        cx, cy = x1 + int(w * 0.5), y1 + int(h * 0.5)
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(188, 0, 45, 240))
    elif flag_type == "China":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(222, 41, 16, 240))
        draw.ellipse([(x1 + int(w * 0.12), y1 + int(h * 0.18)), (x1 + int(w * 0.24), y1 + int(h * 0.38))], fill=(255, 222, 0, 240))
    elif flag_type == "South Korea":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(255, 255, 255, 240))
        cx, cy = x1 + int(w * 0.5), y1 + int(h * 0.5)
        r = int(h * 0.22)
        draw.pieslice([(cx - r, cy - r), (cx + r, cy + r)], start=0, end=180, fill=(205, 46, 58, 240))
        draw.pieslice([(cx - r, cy - r), (cx + r, cy + r)], start=180, end=360, fill=(0, 71, 160, 240))
    elif flag_type == "India":
        draw_horizontal_tricolor((255, 153, 51, 240), (255, 255, 255, 240), (19, 136, 8, 240))
        cx, cy = x1 + int(w * 0.5), y1 + int(h * 0.5)
        r = int(h * 0.12)
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=(0, 0, 128, 240), width=2)
    elif flag_type == "Brazil":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(0, 156, 59, 240))
        draw.polygon([(x1 + int(w * 0.5), y1 + int(h * 0.12)), (x1 + int(w * 0.88), y1 + int(h * 0.5)), (x1 + int(w * 0.5), y1 + int(h * 0.88)), (x1 + int(w * 0.12), y1 + int(h * 0.5))], fill=(255, 223, 0, 240))
        r = int(h * 0.18)
        cx, cy = x1 + int(w * 0.5), y1 + int(h * 0.5)
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(0, 39, 118, 240))
    elif flag_type == "Argentina":
        draw_horizontal_tricolor((116, 172, 223, 240), (255, 255, 255, 240), (116, 172, 223, 240))
        r = int(h * 0.10)
        cx, cy = x1 + int(w * 0.5), y1 + int(h * 0.5)
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(255, 196, 0, 240))
    elif flag_type == "Chile":
        draw.rectangle([(x1, y1), (x2, y1 + int(h * 0.5))], fill=(255, 255, 255, 240))
        draw.rectangle([(x1, y1 + int(h * 0.5)), (x2, y2)], fill=(213, 43, 30, 240))
        draw.rectangle([(x1, y1), (x1 + int(w * 0.34), y1 + int(h * 0.5))], fill=(0, 57, 166, 240))
    elif flag_type == "Colombia":
        draw.rectangle([(x1, y1), (x2, y1 + int(h * 0.5))], fill=(252, 209, 22, 240))
        draw.rectangle([(x1, y1 + int(h * 0.5)), (x2, y1 + int(h * 0.75))], fill=(0, 56, 147, 240))
        draw.rectangle([(x1, y1 + int(h * 0.75)), (x2, y2)], fill=(206, 17, 38, 240))
    elif flag_type == "Peru":
        draw_vertical_tricolor((206, 17, 38, 240), (255, 255, 255, 240), (206, 17, 38, 240))
    elif flag_type == "Australia":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(1, 33, 105, 240))
        draw.ellipse([(x1 + int(w * 0.68), y1 + int(h * 0.28)), (x1 + int(w * 0.78), y1 + int(h * 0.48))], fill=(255, 255, 255, 240))
    elif flag_type == "New Zealand":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(0, 40, 104, 240))
        draw.ellipse([(x1 + int(w * 0.70), y1 + int(h * 0.30)), (x1 + int(w * 0.80), y1 + int(h * 0.50))], fill=(255, 0, 0, 240))
    elif flag_type == "South Africa":
        draw_horizontal_bicolor((0, 122, 77, 240), (0, 0, 0, 240))
        draw.polygon([(x1, y1), (x1 + int(w * 0.45), y1 + int(h * 0.5)), (x1, y2)], fill=(255, 184, 28, 240))
    elif flag_type == "Egypt":
        draw_horizontal_tricolor((206, 17, 38, 240), (255, 255, 255, 240), (0, 0, 0, 240))
    elif flag_type == "Morocco":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(193, 39, 45, 240))
        draw.ellipse([(x1 + int(w * 0.43), y1 + int(h * 0.40)), (x1 + int(w * 0.57), y1 + int(h * 0.60))], outline=(0, 122, 61, 240), width=2)
    elif flag_type == "Algeria":
        draw.rectangle([(x1, y1), (x1 + int(w * 0.5), y2)], fill=(0, 122, 61, 240))
        draw.rectangle([(x1 + int(w * 0.5), y1), (x2, y2)], fill=(255, 255, 255, 240))
    elif flag_type == "Tunisia":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(227, 10, 23, 240))
        cx, cy = x1 + int(w * 0.5), y1 + int(h * 0.5)
        r = int(h * 0.2)
        draw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], fill=(255, 255, 255, 240))
    elif flag_type == "Saudi Arabia":
        draw.rectangle([(x1, y1), (x2, y2)], fill=(0, 108, 53, 240))
        draw.rectangle([(x1 + int(w * 0.25), y1 + int(h * 0.72)), (x1 + int(w * 0.75), y1 + int(h * 0.76))], fill=(255, 255, 255, 240))
    elif flag_type == "United Arab Emirates":
        draw.rectangle([(x1, y1), (x1 + int(w * 0.25), y2)], fill=(206, 17, 38, 240))
        draw.rectangle([(x1 + int(w * 0.25), y1), (x2, y1 + int(h / 3))], fill=(0, 122, 61, 240))
        draw.rectangle([(x1 + int(w * 0.25), y1 + int(h / 3)), (x2, y1 + int(2 * h / 3))], fill=(255, 255, 255, 240))
        draw.rectangle([(x1 + int(w * 0.25), y1 + int(2 * h / 3)), (x2, y2)], fill=(0, 0, 0, 240))
    elif flag_type == "Qatar":
        draw.rectangle([(x1, y1), (x1 + int(w * 0.36), y2)], fill=(255, 255, 255, 240))
        draw.rectangle([(x1 + int(w * 0.36), y1), (x2, y2)], fill=(138, 21, 56, 240))
    else:
        draw_horizontal_tricolor((80, 80, 80, 240), (210, 210, 210, 240), (80, 80, 80, 240))

def add_realistic_plastic_effects(image, radius=35):
    width, height = image.size
    
    mask = Image.new("L", (width, height), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle([(0, 0), (width, height)], radius=radius, fill=255)
    image.putalpha(mask)

    noise_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    np_draw = ImageDraw.Draw(noise_layer)
    for _ in range(int(width * height * 0.012)):
        nx = random.randint(0, width - 1)
        ny = random.randint(0, height - 1)
        val = random.randint(180, 255)
        np_draw.point((nx, ny), fill=(val, val, val, random.randint(6, 18)))
    image = Image.alpha_composite(image, noise_layer)

    dot_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    dot_draw = ImageDraw.Draw(dot_layer)
    for x in range(0, width, 4):
        for y in range(0, height, 4):
            if (x + y) % 8 == 0:
                dot_draw.point((x, y), fill=(0, 0, 0, 12))
    image = Image.alpha_composite(image, dot_layer)

    holo_foil = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    hf_draw = ImageDraw.Draw(holo_foil)
    for i in range(-height, width, 2):
        alpha_val = int(12 * abs(math.sin(i / 80.0)))
        if alpha_val > 1:
            color_choice = (random.choice([150, 255]), random.choice([200, 100]), random.choice([255, 180]), alpha_val)
            hf_draw.line([(i, 0), (i + height, height)], fill=color_choice, width=12)
    holo_foil = holo_foil.filter(ImageFilter.GaussianBlur(10))
    image = Image.alpha_composite(image, holo_foil)

    gloss = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(gloss)
    for i in range(-height, width, 4):
        alpha_shine = int(22 * math.sin(i / 120.0))
        if alpha_shine > 0:
            g_draw.line([(i, 0), (i + height, height)], fill=(255, 255, 255, alpha_shine), width=50)
    gloss = gloss.filter(ImageFilter.GaussianBlur(18))
    image = Image.alpha_composite(image, gloss)

    border_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw_border = ImageDraw.Draw(border_overlay)
    draw_border.rounded_rectangle([(0, 0), (width - 1, height - 1)], radius=radius, outline=(30, 30, 30, 180), width=1)
    draw_border.rounded_rectangle([(1, 1), (width - 2, height - 2)], radius=radius - 1, outline=(255, 255, 255, 140), width=1)
    
    final_image = Image.alpha_composite(image, border_overlay)
    return final_image

def generate_id_card(card_type, state_name, logo_path, output_filename, custom_colors=None, layout_style="standard", lang="EN", custom_card_name=None, custom_flag_type=None, security_profile="Standard", security_label=None):
    width, height = 1067, 712
    state_data = STATES_CONFIG.get(state_name.upper(), DEFAULT_STATE).copy()
    security_cfg = SECURITY_PROFILES.get(security_profile, SECURITY_PROFILES["Standard"])
    
    if custom_colors:
        if custom_colors.get("header"):
            state_data["primary_header"] = custom_colors["header"]
        if custom_colors.get("stripe"):
            state_data["accent_stripe"] = custom_colors["stripe"]

    flag_type = custom_flag_type if custom_flag_type else state_data.get("flag", "USA")
    
    card = create_security_background_gradient(width, height, state_data)
    guilloche = create_guilloche_pattern(
        width,
        height,
        color_primary=state_data["guilloche_color"],
        pattern_type=card_type,
        density=security_cfg["density"],
        alpha_factor=security_cfg["alpha"]
    )
    card = Image.alpha_composite(card, guilloche)
    
    rosettes = add_security_rosettes(
        width,
        height,
        state_data,
        density=security_cfg["density"],
        alpha_factor=security_cfg["alpha"],
        center_count=security_cfg["rosette_centers"]
    )
    card = Image.alpha_composite(card, rosettes)
    
    picto_layer = add_security_pictograms(
        width,
        height,
        state_data,
        density=security_cfg["density"],
        alpha_factor=security_cfg["picto"]
    )
    card = Image.alpha_composite(card, picto_layer)

    theme_layer = add_security_thematic_layer(
        width,
        height,
        state_data,
        art_style=security_cfg.get("art_style", "abstract_rosette"),
        density=security_cfg["density"],
        alpha_factor=security_cfg["alpha"]
    )
    card = Image.alpha_composite(card, theme_layer)

    safe_zone = add_center_safe_zone_overlay(width, height)
    card = Image.alpha_composite(card, safe_zone)
    
    draw = ImageDraw.Draw(card)
    
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 40)
        font_sub = ImageFont.truetype("arialbd.ttf", 40)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    header_bg = state_data["primary_header"]
    stripe_bg = state_data["accent_stripe"]
    
    text_color_override = None
    if layout_style == "Top Banner / Classic":
        draw.rectangle([(0, 0), (width, 110)], fill=header_bg)
        draw.rectangle([(0, 110), (width, 122)], fill=stripe_bg)
        title_x, title_y1, title_y2 = 50, 22, 72
        flag_pos = "top_right"
    elif layout_style == "Compact / Minimalist (Max Safe Zone)":
        draw.rectangle([(0, 0), (width, 85)], fill=header_bg)
        draw.rectangle([(0, 85), (width, 93)], fill=stripe_bg)
        title_x, title_y1, title_y2 = 40, 15, 50
        flag_pos = "top_right"
    elif layout_style == "Inverted (Flag on Left)":
        draw.rectangle([(0, 0), (width, 110)], fill=header_bg)
        draw.rectangle([(0, 110), (width, 122)], fill=stripe_bg)
        title_x, title_y1, title_y2 = 145, 22, 72
        flag_pos = "top_left"
    elif layout_style == "Side Banner (Vertical Government Style)":
        draw.rectangle([(0, 0), (280, height)], fill=header_bg)
        draw.rectangle([(280, 0), (295, height)], fill=stripe_bg)
        title_x, title_y1, title_y2 = 310, 30, 80
        flag_pos = "top_right"
        text_color_override = (20, 20, 20, 255)
    elif layout_style == "Double Border & Floating Header":
        draw.rectangle([(0, 0), (width, 130)], fill=header_bg)
        draw.rectangle([(0, 130), (width, 140)], fill=stripe_bg)
        draw.rectangle([(0, 140), (width, 146)], fill=(255, 255, 255, 200))
        title_x, title_y1, title_y2 = 50, 30, 82
        flag_pos = "top_right"
    elif layout_style == "Diplomatic Style / Centered":
        draw.rectangle([(0, 0), (width, 110)], fill=header_bg)
        draw.rectangle([(0, 110), (width, 122)], fill=stripe_bg)
        title_x, title_y1, title_y2 = width // 2, 22, 72
        flag_pos = "bottom_right"
    else: 
        draw.rectangle([(0, 0), (width, 110)], fill=header_bg)
        draw.rectangle([(0, 110), (width, 122)], fill=stripe_bg)
        title_x, title_y1, title_y2 = 50, 22, 72
        flag_pos = "top_right"

    t_color = text_color_override if text_color_override else (255, 255, 255, 255)
    sub_color = (60, 60, 60, 255) if text_color_override else (230, 230, 230, 255)
    police_sub_col = (80, 50, 0, 255) if text_color_override else (255, 240, 200, 255)
    fib_sub_col = (120, 20, 20, 255) if text_color_override else (255, 200, 200, 255)
    mil_sub_col = (100, 80, 0, 255) if text_color_override else (230, 215, 130, 255)

    anchor_val = "mt" if layout_style == "Diplomatic Style / Centered" else None
    t_dict = TRANSLATIONS.get(lang, TRANSLATIONS["EN"])
    title_territory = state_name.strip().upper() if state_name else ""
    custom_subtitle = custom_card_name.strip().upper() if custom_card_name else ""

    text_outline = 1

    if card_type == "civil":
        draw.text((title_x, title_y1), title_territory, fill=t_color, font=font_title, anchor=anchor_val, stroke_width=text_outline, stroke_fill=t_color)
        sub_text = custom_subtitle if custom_subtitle else t_dict["civil_title"]
        draw.text((title_x, title_y2), sub_text, fill=sub_color, font=font_sub, anchor=anchor_val, stroke_width=text_outline, stroke_fill=sub_color)
    elif card_type == "police":
        draw.text((title_x, title_y1), f"{title_territory} - {t_dict['police_title']}", fill=t_color, font=font_title, anchor=anchor_val, stroke_width=text_outline, stroke_fill=t_color)
        sub_text = custom_subtitle if custom_subtitle else t_dict["police_sub"]
        draw.text((title_x, title_y2), sub_text, fill=police_sub_col, font=font_sub, anchor=anchor_val, stroke_width=text_outline, stroke_fill=police_sub_col)
    elif card_type == "fib":
        draw.text((title_x, title_y1), t_dict["fib_title"], fill=t_color, font=font_title, anchor=anchor_val, stroke_width=text_outline, stroke_fill=t_color)
        sub_text = custom_subtitle if custom_subtitle else f"{t_dict['fib_sub']}{title_territory}"
        draw.text((title_x, title_y2), sub_text, fill=fib_sub_col, font=font_sub, anchor=anchor_val, stroke_width=text_outline, stroke_fill=fib_sub_col)
    elif card_type == "ems":
        draw.text((title_x, title_y1), f"{title_territory} - {t_dict['ems_title']}", fill=t_color, font=font_title, anchor=anchor_val, stroke_width=text_outline, stroke_fill=t_color)
        sub_text = custom_subtitle if custom_subtitle else t_dict["ems_sub"]
        draw.text((title_x, title_y2), sub_text, fill=sub_color, font=font_sub, anchor=anchor_val, stroke_width=text_outline, stroke_fill=sub_color)
    elif card_type == "military":
        draw.text((title_x, title_y1), t_dict["mil_title"], fill=t_color, font=font_title, anchor=anchor_val, stroke_width=text_outline, stroke_fill=t_color)
        sub_text = custom_subtitle if custom_subtitle else f"{t_dict['mil_sub']}{title_territory}"
        draw.text((title_x, title_y2), sub_text, fill=mil_sub_col, font=font_sub, anchor=anchor_val, stroke_width=text_outline, stroke_fill=mil_sub_col)

    add_flag_badge(card, width, height, flag_type=flag_type, position=flag_pos)

    if security_label:
        try:
            sec_font = ImageFont.truetype("arial.ttf", 16)
        except IOError:
            sec_font = ImageFont.load_default()
        security_text = f"SECURITY: {security_label.strip()}"
        draw.text((30, height - 28), security_text, fill=(35, 35, 35, 180), font=sec_font)

    if logo_path and os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo = logo.resize((320, 320))
            alpha = logo.split()[3]
            alpha = alpha.point(lambda p: int(p * 0.28))
            logo.putalpha(alpha)
            card.paste(logo, (width // 2 - 40, height // 2 - 160), logo)
        except Exception as e:
            print(f"Error loading logo: {e}")

    final_card = add_realistic_plastic_effects(card, radius=35)
    final_card.save(output_filename, "PNG")


# --- WIN98 GUI WITH LANGUAGE SWITCHER ---

def create_win98_container(parent, title_text=""):
    outer = tk.Frame(parent, bg="#808080", bd=2, relief="raised")
    
    title_bar = tk.Frame(outer, bg="#000080", height=22)
    title_bar.pack(fill="x", padx=1, pady=1)
    title_bar.pack_propagate(False)
    
    title_lbl = tk.Label(title_bar, text=f"  {title_text}", bg="#000080", fg="white", font=("MS Sans Serif", 9, "bold"), anchor="w")
    title_lbl.pack(side="left", fill="both", expand=True)
    
    close_btn = tk.Label(title_bar, text=" X ", bg="#c0c0c0", fg="black", font=("MS Sans Serif", 8, "bold"), relief="raised", bd=1)
    close_btn.pack(side="right", padx=2, pady=2)
    
    content = tk.Frame(outer, bg="#c0c0c0", padx=8, pady=8)
    content.pack(fill="both", expand=True, padx=1, pady=1)
    
    return outer, content

def create_win98_button(parent, text, command, width=None):
    btn = tk.Button(
        parent, 
        text=text, 
        command=command,
        bg="#c0c0c0", 
        fg="black", 
        font=("MS Sans Serif", 9),
        relief="raised",
        bd=2,
        activebackground="#c0c0c0",
        activeforeground="black",
        cursor="arrow"
    )
    if width:
        btn.config(width=width)
    return btn


class IDCardAppWin98:
    def __init__(self, root):
        self.root = root
        self.root.geometry("570x760")
        self.root.resizable(False, False)
        self.root.config(bg="#a8d8ff")

        # Variables
        self.lang_var = tk.StringVar(value="FR")
        self.state_var = tk.StringVar(value=list(STATES_CONFIG.keys())[0])
        self.flag_override_var = tk.StringVar(value="AUTO")
        self.card_name_var = tk.StringVar(value="")
        self.security_profile_display_var = tk.StringVar(value="Profile 02")
        self.security_name_var = tk.StringVar(value=SECURITY_PROFILES["Standard"]["tech_name"])
        
        self.types_map = {
            "Civil Card / Civil Status": "civil",
            "Police (Law Enforcement / Badge)": "police",
            "FIB (Federal Agent)": "fib",
            "EMS (Medical Services)": "ems",
            "Military": "military"
        }
        self.type_var = tk.StringVar(value=list(self.types_map.keys())[0])

        self.layouts_list = [
            "Top Banner / Classic",
            "Compact / Minimalist (Max Safe Zone)",
            "Inverted (Flag on Left)",
            "Side Banner (Vertical Government Style)",
            "Double Border & Floating Header",
            "Diplomatic Style / Centered"
        ]
        self.layout_var = tk.StringVar(value=self.layouts_list[0])
        self.security_profile_options = [
            ("Profile 01", "Basic"),
            ("Profile 02", "Standard"),
            ("Profile 03", "Advanced"),
            ("Profile 04", "Ultra"),
            ("Profile 05", "Banknote"),
            ("Profile 06", "Government High"),
            ("Profile 07", "Minimal Clean"),
            ("Profile 08", "Tactical"),
            ("Profile 09", "Continental"),
            ("Profile 10", "Coastal"),
            ("Profile 11", "Agricultural"),
            ("Profile 12", "Rosace Abstract"),
            ("Profile 13", "Terrain Relief"),
            ("Profile 14", "Maritime"),
            ("Profile 15", "Europe Silhouette"),
            ("Profile 16", "USA Silhouette"),
            ("Profile 17", "Boats On Water"),
            ("Profile 18", "Field Parcels")
        ]
        self.security_profiles = [label for label, _ in self.security_profile_options]
        self.profile_display_to_key = {label: key for label, key in self.security_profile_options}
        self.profile_key_to_display = {key: label for label, key in self.security_profile_options}
        self.profile_default_labels = {k: v.get("tech_name", "") for k, v in SECURITY_PROFILES.items()}
        self.flag_values = [
            "AUTO", "USA", "Canada", "Mexico", "Cuba", "France", "United Kingdom",
            "Germany", "Allemagne", "Italy", "Spain", "Portugal", "Belgium", "Netherlands", "Ireland",
            "Sweden", "Norway", "Finland", "Denmark", "Switzerland", "Austria", "Poland",
            "Ukraine", "Romania", "Greece", "Turkey", "Russia", "Japan", "China",
            "South Korea", "India", "Brazil", "Argentina", "Chile", "Colombia", "Peru",
            "Australia", "New Zealand", "South Africa", "Egypt", "Morocco", "Algeria",
            "Tunisia", "Saudi Arabia", "United Arab Emirates", "Qatar"
        ]

        self.logo_path = tk.StringVar(value="")
        self.use_custom_colors = tk.BooleanVar(value=False)
        self.header_color = (20, 35, 60, 255)
        self.stripe_color = (200, 160, 40, 255)

        # UI References for dynamic translation
        self.widgets_to_update = {}
        self.preview_window = None
        self.preview_image_ref = None
        self._last_profile_applied = self.security_profile_display_var.get()

        self.create_widgets()
        self.apply_security_profile(force=True)
        self.update_ui_texts()

    def create_widgets(self):
        self.main_win, content_area = create_win98_container(self.root, title_text="")
        self.main_win.pack(fill="both", expand=True, padx=10, pady=10)

        # Top Bar for Language Selector inside Win98 style
        top_lang_frame = tk.Frame(content_area, bg="#c0c0c0")
        top_lang_frame.pack(fill="x", padx=5, pady=(0, 5))

        lbl_lang = tk.Label(top_lang_frame, text="Interface Language / Langue :", bg="#c0c0c0", fg="black", font=("MS Sans Serif", 8, "bold"))
        lbl_lang.pack(side="left")

        lang_combo = ttk.Combobox(top_lang_frame, textvariable=self.lang_var, values=["FR", "EN", "DE", "ES"], state="readonly", width=8)
        lang_combo.pack(side="right")
        lang_combo.bind("<<ComboboxSelected>>", lambda e: self.update_ui_texts())

        # Banner Info
        banner_frame = tk.Frame(content_area, bg="#c0c0c0", bd=2, relief="sunken")
        banner_frame.pack(fill="x", padx=5, pady=2)
        
        self.lbl_info = tk.Label(
            banner_frame, 
            text="", 
            bg="#c0c0c0", 
            fg="#000000", 
            font=("MS Sans Serif", 8),
            justify="left"
        )
        self.lbl_info.pack(padx=6, pady=6, anchor="w")

        # Form Inner Box
        form_outer = tk.Frame(content_area, bg="#808080", bd=1, relief="sunken")
        form_outer.pack(fill="x", padx=5, pady=5)
        form_inner = tk.Frame(form_outer, bg="#c0c0c0", padx=10, pady=10)
        form_inner.pack(fill="both", expand=True)

        def add_field(row, text_key, widget):
            lbl = tk.Label(form_inner, bg="#c0c0c0", fg="black", font=("MS Sans Serif", 9, "bold"))
            lbl.grid(row=row, column=0, sticky="w", pady=5)
            widget.grid(row=row, column=1, sticky="ew", pady=5, padx=5)
            self.widgets_to_update[text_key] = lbl

        self.state_combo = ttk.Combobox(form_inner, textvariable=self.state_var, values=list(STATES_CONFIG.keys()), state="normal", width=32)
        add_field(0, "territory", self.state_combo)

        self.flag_combo = ttk.Combobox(form_inner, textvariable=self.flag_override_var, values=self.flag_values, state="readonly", width=32)
        add_field(1, "flag_choice", self.flag_combo)

        self.card_name_entry = tk.Entry(form_inner, textvariable=self.card_name_var, bg="white", fg="black", font=("MS Sans Serif", 8), bd=2, relief="sunken")
        add_field(2, "card_name_custom", self.card_name_entry)

        self.type_combo = ttk.Combobox(form_inner, textvariable=self.type_var, values=list(self.types_map.keys()), state="readonly", width=32)
        add_field(3, "card_type", self.type_combo)

        self.layout_combo = ttk.Combobox(form_inner, textvariable=self.layout_var, values=self.layouts_list, state="readonly", width=32)
        add_field(4, "layout_style", self.layout_combo)

        self.security_profile_combo = ttk.Combobox(form_inner, textvariable=self.security_profile_display_var, values=self.security_profiles, state="readonly", width=32)
        add_field(5, "security_profile", self.security_profile_combo)
        self.security_profile_combo.bind("<<ComboboxSelected>>", lambda e: self.apply_security_profile())

        self.security_name_entry = tk.Entry(form_inner, textvariable=self.security_name_var, bg="white", fg="black", font=("MS Sans Serif", 8), bd=2, relief="sunken")
        add_field(6, "security_name", self.security_name_entry)

        self.custom_check = tk.Checkbutton(
            form_inner, 
            variable=self.use_custom_colors, 
            command=self.toggle_color_selectors,
            bg="#c0c0c0", 
            fg="black", 
            font=("MS Sans Serif", 8),
            selectcolor="#c0c0c0",
            activebackground="#c0c0c0"
        )
        self.custom_check.grid(row=7, column=0, columnspan=2, sticky="w", pady=(4, 4))
        self.widgets_to_update["custom_colors"] = self.custom_check

        self.color_frame = tk.Frame(form_inner, bg="#c0c0c0")
        self.color_frame.grid(row=8, column=0, columnspan=2, sticky="ew", pady=2)
        
        self.btn_header_col = create_win98_button(self.color_frame, "", lambda: self.pick_color('header'), width=18)
        self.btn_header_col.pack(side="left", padx=(0, 5))
        self.btn_header_col.config(bg="#14233c", fg="white")
        self.widgets_to_update["header_col"] = self.btn_header_col

        self.btn_stripe_col = create_win98_button(self.color_frame, "", lambda: self.pick_color('stripe'), width=18)
        self.btn_stripe_col.pack(side="right", padx=(5, 0))
        self.btn_stripe_col.config(bg="#c8a028", fg="black")
        self.widgets_to_update["stripe_col"] = self.btn_stripe_col

        self.toggle_color_selectors()

        logo_container = tk.Frame(form_inner, bg="#c0c0c0")
        logo_container.grid(row=9, column=0, columnspan=2, sticky="ew", pady=6)
        
        self.lbl_logo = tk.Label(logo_container, bg="#c0c0c0", fg="black", font=("MS Sans Serif", 9, "bold"))
        self.lbl_logo.pack(side="left", anchor="w")
        self.widgets_to_update["seal_logo"] = self.lbl_logo

        logo_inner_frame = tk.Frame(logo_container, bg="#c0c0c0")
        logo_inner_frame.pack(side="right", fill="x", expand=True, padx=(10, 0))

        self.logo_entry = tk.Entry(logo_inner_frame, textvariable=self.logo_path, bg="white", fg="black", font=("MS Sans Serif", 8), bd=2, relief="sunken")
        self.logo_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.logo_btn = create_win98_button(logo_inner_frame, "", command=self.browse_logo, width=10)
        self.logo_btn.pack(side="right", padx=(4, 0))
        self.widgets_to_update["browse"] = self.logo_btn

        self.clear_logo_btn = create_win98_button(logo_inner_frame, "", command=self.clear_logo, width=10)
        self.clear_logo_btn.pack(side="right")
        self.widgets_to_update["clear_seal"] = self.clear_logo_btn

        # Action Button
        action_frame = tk.Frame(content_area, bg="#c0c0c0", pady=8)
        action_frame.pack(fill="x", padx=5)

        self.preview_btn = tk.Button(
            action_frame,
            command=self.preview,
            bg="#c0c0c0",
            fg="black",
            font=("MS Sans Serif", 9, "bold"),
            relief="raised",
            bd=3,
            activebackground="#a0a0a0",
            cursor="hand2",
            padx=8,
            pady=6
        )
        self.preview_btn.pack(side="left", fill="x", expand=True, padx=(0, 4))
        self.widgets_to_update["preview_btn"] = self.preview_btn

        self.generate_btn = tk.Button(
            action_frame, 
            command=self.generate, 
            bg="#c0c0c0", 
            fg="black", 
            font=("MS Sans Serif", 9, "bold"),
            relief="raised",
            bd=3,
            activebackground="#a0a0a0",
            cursor="hand2",
            padx=10,
            pady=6
        )
        self.generate_btn.pack(side="right", fill="x", expand=True, padx=(4, 0))
        self.widgets_to_update["print_btn"] = self.generate_btn

        # Status Bar
        status_bar = tk.Frame(self.root, bg="#c0c0c0", bd=1, relief="sunken", height=22)
        status_bar.pack(side="bottom", fill="x")
        status_bar.pack_propagate(False)

        self.status_lbl = tk.Label(status_bar, bg="#c0c0c0", fg="black", font=("MS Sans Serif", 8), anchor="w")
        self.status_lbl.pack(side="left", padx=4)

        time_lbl = tk.Label(status_bar, text="[SECURE 1998]", bg="#c0c0c0", fg="black", font=("MS Sans Serif", 8), anchor="e")
        time_lbl.pack(side="right", padx=4)

    def update_ui_texts(self):
        lang = self.lang_var.get()
        t = TRANSLATIONS.get(lang, TRANSLATIONS["EN"])

        self.root.title(t["title_app"])
        self.lbl_info.config(text=t["sys_info"])
        self.status_lbl.config(text=t["ready"])

        for key, widget in self.widgets_to_update.items():
            if key in t:
                if isinstance(widget, tk.Checkbutton):
                    widget.config(text=t[key])
                else:
                    widget.config(text=t[key])

    def apply_security_profile(self, force=False):
        current_profile_display = self.security_profile_display_var.get()
        current_profile_key = self.profile_display_to_key.get(current_profile_display, "Standard")
        prev_profile_display = self._last_profile_applied
        prev_profile_key = self.profile_display_to_key.get(prev_profile_display, "Standard")
        prev_default = self.profile_default_labels.get(prev_profile_key, "")
        current_label = self.security_name_var.get().strip()
        # Auto-refresh technical label when switching profile unless user typed a custom one.
        if force or not current_label or current_label == prev_default:
            self.security_name_var.set(self.profile_default_labels.get(current_profile_key, ""))
        self._last_profile_applied = current_profile_display

    def toggle_color_selectors(self):
        state = "normal" if self.use_custom_colors.get() else "disabled"
        self.btn_header_col.config(state=state)
        self.btn_stripe_col.config(state=state)

    def pick_color(self, target):
        color_code = colorchooser.askcolor(title="Select System Color")
        if color_code[0]:
            rgb = tuple(int(c) for c in color_code[0]) + (255,)
            hex_col = color_code[1]
            if target == 'header':
                self.header_color = rgb
                self.btn_header_col.config(bg=hex_col)
            elif target == 'stripe':
                self.stripe_color = rgb
                self.btn_stripe_col.config(bg=hex_col)

    def browse_logo(self):
        file_path = filedialog.askopenfilename(
            title="Select Seal / Logo",
            filetypes=[("PNG/JPG Images", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")]
        )
        if file_path:
            self.logo_path.set(file_path)

    def clear_logo(self):
        self.logo_path.set("")

    def get_generation_params(self):
        state = self.state_var.get()
        gui_card_type_label = self.type_var.get()
        card_type = self.types_map.get(gui_card_type_label, "civil")
        layout_style = self.layout_var.get()
        logo = self.logo_path.get()

        custom_colors = None
        if self.use_custom_colors.get():
            custom_colors = {
                "header": self.header_color,
                "stripe": self.stripe_color
            }

        chosen_flag = self.flag_override_var.get().strip()
        flag_aliases = {
            "Allemagne": "Germany"
        }
        normalized_flag = flag_aliases.get(chosen_flag, chosen_flag)
        custom_flag_type = None if normalized_flag == "AUTO" else normalized_flag

        return {
            "card_type": card_type,
            "state_name": state,
            "logo_path": logo if logo else None,
            "custom_colors": custom_colors,
            "layout_style": layout_style,
            "lang": self.lang_var.get(),
            "custom_card_name": self.card_name_var.get(),
            "custom_flag_type": custom_flag_type,
            "security_profile": self.profile_display_to_key.get(self.security_profile_display_var.get(), "Standard"),
            "security_label": self.security_name_var.get()
        }

    def preview(self):
        lang = self.lang_var.get()
        t = TRANSLATIONS.get(lang, TRANSLATIONS["EN"])
        preview_file = os.path.join(tempfile.gettempdir(), "id_card_preview.png")

        params = self.get_generation_params()
        try:
            generate_id_card(output_filename=preview_file, **params)

            with Image.open(preview_file) as src_img:
                preview_img = src_img.convert("RGBA")

            resample = Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS
            preview_img.thumbnail((920, 620), resample)

            if self.preview_window and self.preview_window.winfo_exists():
                self.preview_window.destroy()

            self.preview_window = tk.Toplevel(self.root)
            self.preview_window.title(t.get("preview_title", "Preview"))
            self.preview_window.config(bg="#c0c0c0")
            self.preview_window.resizable(False, False)

            frame = tk.Frame(self.preview_window, bg="#c0c0c0", bd=2, relief="sunken")
            frame.pack(padx=8, pady=8)

            self.preview_image_ref = ImageTk.PhotoImage(preview_img)
            preview_label = tk.Label(frame, image=self.preview_image_ref, bg="#c0c0c0")
            preview_label.pack()

            close_btn = create_win98_button(self.preview_window, "Fermer", self.preview_window.destroy, width=12)
            close_btn.pack(pady=(0, 8))

            self.preview_window.transient(self.root)
            self.preview_window.grab_set()
            self.preview_window.focus_set()
        except Exception as e:
            messagebox.showerror(t["error_title"], f"{t['error_msg']}{str(e)}")

    def generate(self):
        lang = self.lang_var.get()
        t = TRANSLATIONS.get(lang, TRANSLATIONS["EN"])
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        output = filedialog.asksaveasfilename(
            title="Save official document as...",
            defaultextension=".png",
            initialfile="id_card.png",
            initialdir=desktop_path,
            filetypes=[("PNG Image", "*.png")]
        )

        if not output:
            return

        params = self.get_generation_params()

        try:
            generate_id_card(output_filename=output, **params)
            messagebox.showinfo(t["success_title"], f"{t['success_msg']}{output}")
        except Exception as e:
            messagebox.showerror(t["error_title"], f"{t['error_msg']}{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = IDCardAppWin98(root)
    root.mainloop()