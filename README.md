# README

## Overview
This project is part of my submission for the Summer 2022 [Shopify Backend Developer Intern Challenge](https://www.shopify.ca/careers/backend-developer-intern-summer-2022-remote-us-canada_f29b717b-42d7-4d32-851b-e5b2c69a16c7)(See `Shopify Backend Developer Intern Challenge - Summer 2022.pdf`). 

The task was to build an inventory tracking web application for a logistics company. The challenge's requirements for the app were two-fold: Supporting basic Create, Read, Update and Delete (CRUD) functionality, and adding one additional feature; the additional feature I focused on is **allow\[ing\] image uploads AND store image with generated thumbnails**. More details are included in the **The Web App** section. 

## Demo!
![Demo GIF](https://raw.githubusercontent.com/srcoulombe/sf_karting_django/main/demo.gif)

## Quickstart
You can download and run the project yourself by following these steps:

0. Install [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads).
1. Create a `git` repo on your computer: navigate to the folder in which you want to save the code, open a terminal, and run the command `git init`.
2. Run the following command in the same terminal (same location) to clone this repository: `git clone ...`.
3. Create a virtual environment (to download the project's dependencies without affecting your other projects) by running the command `python3 -m venv django_venv`.
4. Activate your virtual environment with the CLI command `source django_venv/bin/activate` (if you use MacOS/Linux) or `.\django_venv\Scripts\activate` (for Windows users).
5. Download the external dependencies by running the command `python3 -m pip install -r requirements.txt`.
6. Run the following commands in the same terminal at the same location: 
```...```
7. Open your browser at `http://127.0.0.1:8000/admin/`
8. Log in with user: `samy` and password: `samy`
9. You can use the admin dashboard at `http://127.0.0.1:8000/admin/` to execute copy-read-update-delete operations on inventory items, or experience the full web app by navigating to `http://127.0.0.1:8000`.

## The Story
This inventory tracking app was built for specific company (which we'll call **SF Karting** for now). This company's logistics activities includes the provisioning, movement, and storage of karting parts, as well as track-side services (rent-a-mechanic, kart tuning, race analytics, and coaching services). 

### Adding Complexity
What makes **SF Karting** special is that **they must travel to each race in the [Coupe de Montreal](https://coupedemontreal.com/en/my-front-page-en/)** in order to provide their track-side services. They must therefore load the karts, spare and repair parts, tools, and other inventory items that they believe they will need/sell during a race weekend **before** heading to the racetrack. The travel is quite involved since their trailers are very large and loading/unloading them takes a lot of time. As such, **they cannot quickly restock items if they run out** during the course of a race weekend. **Knowing the number of items they have in stock is therefore not enough**; they **also need to estimate how many of each item they will need/sell** during the course of a weekend, and **quickly find which items need pre-emptive restocking**.

## The Web App
This inventory tracking web app allows **SF Karting employees to log in, create, read, update, delete, and list inventory items** (thereby fulfilling the requirement for basic CRUD operations). **Employees can also upload/replace an image of the item** - these **images are stored**, and **thumbnails are generated on-the-fly** using **Base64 encoding**. This feature fulfills the requirement of **"Allow\[ing\] image uploads AND store image with generated thumbnails"**. 

As emphasized in the **Adding Complexity** section, **SF Karting need to know which items are likely to run out of stock during a race weekend**. This is why the inventory items have the `in_stock`, `on_hold`, and `min_quantity_in_stock` attributes. Items that run out of stock (`in_stock = 0`) or are all on hold (`on_hold >= in_stock`) get listed in the **"Out-of-Stock"** section. Items that are not out-of-stock but are likely to become so during the next race weekend (`in_stock - on_hold < min_quantity_in_stock`) are listed in the **"In Need of Restock"** section. 

## Extra and Future Features
### Extra Features that are Already Implemented
The following have been implemented in anticipation of the addition of extra features in the near future: 

* Searching the inventory by item name (via a `django QuerySet`), 
* Enforcing unique item names,
* Recording who last updated an item (and when),
* Resetting the inventory database, and 
* Logging create-update-delete operations

### Future Features
* Trying out [django-reversion](https://github.com/etianen/django-reversion) to handle **database rollbacks and logging CRUD operations**; this will require migrating the database from `sqlite3` to `postgreSQL`, which will itself improve the web app's scalability.

* Enabling employees to **export data to a `.csv` file** (e.g. tabulating sold items, reporting the most frequently out-of-stock items). This could be done by writing functions to execute `SQL` queries and [adding the formatting and downloading functionality](https://docs.djangoproject.com/en/4.0/howto/outputting-csv/) to the project.

* Allowing **customers** to **make purchase orders**. This would require adding an e-commerce app and connecting it to the inventory management system. This would actually be a pretty fun and educational side project!

* Adding pagination functionality to the "In Stock", "Out-of-Stock", and "In Need of Restock" lists. 

## Technology
This `Python` web app was built using `django`, `Pillow`, and `sqlite3`.

You can download the external dependencies using `pip install -r requirements.txt`

# And Finally,
## What I Learned
Developing this web app was fun and I learned a lot! I didn't know anything about how to use `Base64` to represent images in a browser, and implementing the image handling code from scratch was a lot more fun than relying on an existing solution like [django-imagekit](https://github.com/matthewwithanm/django-imagekit/)!

Building the web app was also a good opportunity to refresh myself on the model-view-controller (MVC) pattern; I don't use it at work on a day-to-day basis, and it felt good to review it!

Being able to see the web app progress as I coded was super satisfying (especially when I was able to fix my mistakes and make those ugly django error pages go away)! I was developing a similar [Shopify website](https://mdkarting.myshopify.com) (use the password: `blaske`) in parallel, and the contrast between `django` and `Shopify` was striking! I really enjoyed developing with `django`, but `Shopify`'s building tools made everything so much easier and effortless! Seeing the two projects evolve side-by-side made me really understand and appreciate how much complexity `Shopify` had handled for its clients and customers. 

