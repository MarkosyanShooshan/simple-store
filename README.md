# 🛍️ Simple Store (Django Web Application)

[ 🇬🇧 English Version ](#english) | [ 🇦🇲 Հայերեն Տարբերակ ](#armenian)

---

<span id="english"></span>
## 🇬🇧 English

> A lightweight, intuitive e-commerce web application built with Python and the Django framework. Designed as an accessible online storefront featuring product browsing, category management, and detailed item views.

### 📌 About the Project

The **Simple Store** project highlights clean, maintainable web architecture for an online shop. It focuses on presenting items clearly, allowing users to navigate through product categories, view real-time availability, inspect high-quality item photos, and review pricing.

The application showcases foundational and practical Django concepts, including relational database design (Categories and Products), modular view logic, slug-based URL routing, and a customized Django Admin interface for smooth catalog operations.

### ✨ Key Features

- **Product Showcase & Catalog:** Clean grid presentation of available store inventory categorized by item type.
- **Detailed Product Pages:** Dynamic product pages displaying descriptions, prices, stock status, and product imagery.
- **Category Navigation:** Intuitive browsing experience grouping items under dedicated store categories.
- **SEO-Friendly URLs:** Clean and descriptive URL routing using slugs for optimal readability and navigation.
- **Admin Inventory Dashboard:** Fast and centralized management of products, categories, and inventory via Django Admin.
- **Responsive Layout:** Modular HTML templates built with Django Template Language (DTL) and CSS.

### 🛠 Tech Stack

- **Backend:** Python 3.x, Django
- **Database:** SQLite3 (Django ORM)
- **Frontend:** HTML5, CSS3, Django Templates
- **Image Processing:** Pillow

### 📂 Project Structure

```text
simple_store/
│
├── store/                  # Core storefront app (Models, Views, URLs)
│   ├── models.py           # Product and Category data models
│   ├── views.py            # Store views and catalog display logic
│   ├── urls.py             # Route routing rules
│   └── admin.py            # Admin configuration
│
├── templates/              # HTML templates (base.html, catalog, product_detail)
├── static/                 # Static assets (CSS styling, fonts, icons)
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── .gitignore              # Git ignored files
```

🚀 Installation & Setup

Clone the repository:

git clone https://github.com/MarkosyanShooshan/simple-store.git
cd simple-store
Create and activate a virtual environment:
Windows:
python -m venv venv
venv\Scripts\activate

macOS / Linux:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Create an admin superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.


<span id="armenian"></span>
🇦🇲 Հայերեն

Թեթև և հարմարավետ է-կոմերց (E-commerce) վեբ-հավելված՝ ստեղծված Python-ով և Django ֆրեյմվորքով։ Նախագիծն իրենից ներկայացնում է առցանց խանութի կատալոգ՝ ապրանքների ցուցադրմամբ, կատեգորիաներով և դետալային էջերով։

📌 Նախագծի մասին

Simple Store նախագծի նպատակն է ցույց տալ Django-ով առցանց խանութի ստեղծման մաքուր և գրագետ կառուցվածքը։ Հավելվածը թույլ է տալիս հաճախորդներին հեշտությամբ զննել ապրանքները, տեսնել դրանց արժեքը, նկարագրությունն ու առկայությունը, ինչպես նաև ֆիլտրել ըստ համապատասխան կատեգորիաների։
Նախագիծն ընդգծում է Django-ի հիմնարար առավելությունները՝ ռելյացիոն մոդելներ (Categories & Products), գեղեցիկ և SEO-հարմար հասցեներ (slugs), ինչպես նաև Django Admin հզոր վահանակ՝ ապրանքների տեսականին հեշտությամբ ղեկավարելու համար։

✨ Հիմնական հնարավորությունները

Ապրանքների Կատալոգ — Խանութի տեսականու կոկիկ ցուցադրում՝ նկարներով, գներով և անվանումներով։
Ապրանքի Դետալային Էջ (Product Details) — Յուրաքանչյուր ապրանքի համար առանձին էջ՝ մանրամասն նկարագրությամբ և բարձրորակ լուսանկարով։
Կատեգորիաների Համակարգ — Ապրանքների խմբավորում ըստ համապատասխան բաժինների։
Հարմար URL-ներ (Slugs) — Կարդացվող և հասկանալի հասցեներ յուրաքանչյուր ապրանքի համար։
Django Admin Վահանակ — Խանութի ապրանքների, գների, կատեգորիաների և առկայության կառավարում։
Մոդուլային Շաբլոններ — Django Template Language-ի շաբլոնների ժառանգում և հարմարավետ դիզայն։

👤 Հեղինակ (Author)
- **Shooshan Markosyan** — [GitHub Profile](https://github.com/MarkosyanShooshan)

