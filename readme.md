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

	modified:   listings/admin.py
	modified:   readme.md

#### 6. Setting for Media files

	modified:   config/settings.py
	modified:   config/urls.py
	modified:   readme.md



































