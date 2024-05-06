# Vendor Management System API

## Overview

The Vendor Management System API provides endpoints for managing vendors and purchase orders. It includes functionality for retrieving vendor performance metrics and acknowledging purchase orders.

## Setup Instructions

1. **Clone the Repository:**
git clone <repository_url>

2. **Install Dependencies:**
pip install -r requirements.txt

3. **Database Setup:**
- Ensure you have a PostgreSQL database installed and running.
- Update the database settings in `settings.py`.

4. **Apply Migrations:**
python manage.py migrate

5. **Create a Superuser:**
python manage.py createsuperuser

6. **Run the Server:**
python manage.py runserver

### API Endpoints ###
** Authentication **
To access protected endpoints, obtain an access token by sending a POST request to api/token/. Use the obtained token in the Authorization header for subsequent requests.

Obtain token: POST /api/token/
Refresh token: POST /api/token/refresh/
** Vendors**
List/create vendors: GET /api/vendors/, POST /api/vendors/
Retrieve/update/destroy vendor: GET /api/vendors/<int:pk>/, PUT /api/vendors/<int:pk>/, DELETE /api/vendors/<int:pk>/
Vendor performance metrics: GET /api/vendors/<int:vendor_id>/performance/
** Purchase Orders8
List/create purchase orders: GET /api/purchase_orders/, POST /api/purchase_orders/
Retrieve/update/destroy purchase order: GET /api/purchase_orders/<int:pk>/, PUT /api/purchase_orders/<int:pk>/, DELETE /api/purchase_orders/<int:pk>/
Acknowledge purchase order: POST /api/purchase_orders/<int:po_id>/acknowledge/
