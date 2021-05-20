## BUILDING DJANGO ECOMMERCE - FINESAUCE
https://github.com/gurnitha/django-ecom-finesauce

#### 1. Initial setup

	PASS

#### 2. Starting the ecommerce project

	(venv3921) ing| tree -L 2
	.
	├── config
	│   ├── __init__.py
	│   ├── __pycache__
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	├── manage.py
	└── readme.md

#### 3. Creating listings app

	- create app
	- install the app to project
	- setup timezone
	- check the codes
	- commit
	(venv3921) ing| tree -L 2
	.
	├── config
	│   ├── __init__.py
	│   ├── __pycache__
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	├── listings
	│   ├── __init__.py
	│   ├── __pycache__
	│   ├── admin.py
	│   ├── apps.py
	│   ├── migrations
	│   ├── models.py
	│   ├── tests.py
	│   └── views.py
	├── manage.py
	└── readme.md

#### 4. Designing listings models: Category and Products models

	>> https://github.com/gurnitha/django-ecom-finesauce/commit/83836dcbf5a7ff532f8a0d2cc59a283879976e12

	BEGIN;
	--
	-- Create model Category
	--
	CREATE TABLE "listings_category" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"name" varchar(100) NOT NULL UNIQUE, 
		"slug" varchar(100) NOT NULL UNIQUE);
	--
	-- Create model Product
	--
	CREATE TABLE "listings_product" (
		"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
		"name" varchar(100) NOT NULL UNIQUE, 
		"slug" varchar(100) NOT NULL UNIQUE, 
		"image" varchar(100) NOT NULL, 
		"description" text NOT NULL, 
		"shu" varchar(10) NOT NULL, 
		"price" decimal NOT NULL, 
		"available" bool NOT NULL, 
		"category_id" integer NOT NULL REFERENCES "listings_category" ("id") DEFERRABLE INITIALLY DEFERRED);

	CREATE INDEX "listings_product_category_id_5d2fa1ec" ON "listings_product" ("category_id");
	COMMIT;

#### 5. Registering models and customizing how models are displayed in admin dashboar

	>> https://github.com/gurnitha/django-ecom-finesauce/commit/2d0ddc8d1fb3aefceb2741de770742a572028f75
	modified:   listings/admin.py
	modified:   readme.md

#### 6. Setting for Media files

	>> https://github.com/gurnitha/django-ecom-finesauce/commit/ce0d39ba065a6cfca3762216db24b913db62706f
	modified:   config/settings.py
	modified:   config/urls.py
	modified:   readme.md


### 7. Displaying our categories and products

#### 7.1 Building our product list view

	modified:   listings/views.py
	modified:   readme.md


#### 7.2 Creating template for our product list

	modified:   config/settings.py
	modified:   readme.md
	new file:   templates/base.html
	new file:   templates/product/detail.html
	new file:   templates/product/list.html

#### 7.3 Adding Static files, products, and URL pattern for our view

	modified:   config/urls.py
	modified:   db.sqlite3
	new file:   listings/static/css/admin.css
	new file:   listings/static/css/pdf.css
	new file:   listings/static/css/style.css
	new file:   listings/static/js/scripts.js
	new file:   listings/urls.py
	new file:   media/products/komodo_dragon.jpeg
	new file:   media/products/orange_habanero.jpeg
	modified:   readme.md
	modified:   templates/base.html

#### 7.4 Filtering by category

	modified:   listings/models.py
	modified:   listings/urls.py
	modified:   listings/views.py
	modified:   readme.md
	modified:   templates/product/list.html

#### 7.5 Product detail page

	modified:   listings/models.py
	modified:   listings/urls.py
	modified:   listings/views.py
	modified:   readme.md
	modified:   templates/base.html
	modified:   templates/product/detail.html
	modified:   templates/product/list.html










