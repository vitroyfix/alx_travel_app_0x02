# ALX Travel App 0x01

A fully functional Django REST API application for managing travel listings, bookings, and reviews.

## Features

- **Listings Management**: Create, read, update, and delete travel property listings
- **Bookings System**: Users can book listings for specific dates
- **Reviews**: Users can leave ratings and comments for listings
- **REST API**: Full RESTful API with Django REST Framework
- **Admin Panel**: Django admin interface for easy management
- **Database Seeding**: Custom management command to populate sample data

## Project Structure

```
alx_travel_app_0x01/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── setup.sh                  # Automated setup script
├── .gitignore               # Git ignore rules
├── README.md                # This file
└── alx_travel_app/          # Main Django project
    ├── __init__.py
    ├── settings.py          # Project settings
    ├── urls.py              # Main URL configuration
    ├── wsgi.py              # WSGI configuration
    ├── asgi.py              # ASGI configuration
    └── listings/            # Listings app
        ├── __init__.py
        ├── apps.py          # App configuration
        ├── models.py        # Database models (Listing, Booking, Review)
        ├── serializers.py   # DRF serializers
        ├── views.py         # API views
        ├── urls.py          # App URL routing
        ├── admin.py         # Admin panel configuration
        ├── tests.py         # Unit tests
        └── management/
            └── commands/
                └── seed.py  # Database seeding command
```

## Quick Start

### Option 1: Automated Setup (Recommended)

```bash
# Run the setup script
./setup.sh
```

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create superuser (optional)
python manage.py createsuperuser

# 5. Seed database with sample data
python manage.py seed

# 6. Run development server
python manage.py runserver
```

## API Endpoints

The API is available at `http://127.0.0.1:8000/api/`

### Listings
- `GET /api/listings/` - List all listings
- `POST /api/listings/` - Create a new listing
- `GET /api/listings/{id}/` - Retrieve a specific listing
- `PUT /api/listings/{id}/` - Update a listing
- `DELETE /api/listings/{id}/` - Delete a listing

### Bookings
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create a new booking
- `GET /api/bookings/{id}/` - Retrieve a specific booking
- `PUT /api/bookings/{id}/` - Update a booking
- `DELETE /api/bookings/{id}/` - Delete a booking

### Reviews
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create a new review
- `GET /api/reviews/{id}/` - Retrieve a specific review
- `PUT /api/reviews/{id}/` - Update a review
- `DELETE /api/reviews/{id}/` - Delete a review

## Management Commands

### Seed Database
```bash
python manage.py seed
```
Populates the database with sample listings.

### Create Superuser
```bash
python manage.py createsuperuser
```
Creates an admin user for the Django admin panel.

### Run Tests
```bash
python manage.py test
```
Runs the test suite.

## Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/`

Features:
- Manage listings with filters and search
- View and manage bookings with date hierarchy
- Moderate reviews and ratings
- User management

## Technologies Used

- **Django 4.2+**: Web framework
- **Django REST Framework**: API development
- **Django CORS Headers**: Cross-origin resource sharing
- **SQLite**: Default database (easily switchable to PostgreSQL/MySQL)

## Models

### Listing
- `id` (UUID): Primary key
- `title` (str): Property title
- `description` (text): Detailed description
- `price_per_night` (decimal): Nightly rate
- `location` (str): Property location
- `created_at` (datetime): Creation timestamp

### Booking
- `id` (UUID): Primary key
- `user` (ForeignKey): User who made the booking
- `listing` (ForeignKey): Booked property
- `start_date` (date): Check-in date
- `end_date` (date): Check-out date
- `created_at` (datetime): Creation timestamp

### Review
- `id` (UUID): Primary key
- `user` (ForeignKey): Reviewer
- `listing` (ForeignKey): Reviewed property
- `rating` (int): Rating (1-5)
- `comment` (text): Review text (optional)
- `created_at` (datetime): Creation timestamp

## Testing

The project includes comprehensive unit tests for all models:

```bash
# Run all tests
python manage.py test

# Run specific test class
python manage.py test listings.tests.ListingModelTest

# Run with verbose output
python manage.py test --verbosity=2
```

## Environment Variables

For production, create a `.env` file with:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
```

## Dependencies

- Django>=4.2,<5.0
- djangorestframework>=3.14.0
- django-cors-headers>=4.0.0

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is created for educational purposes as part of the ALX Software Engineering program.

## Troubleshooting

### Import errors
If you see import errors, ensure the virtual environment is activated and dependencies are installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Database errors
Reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py seed
```

### Port already in use
Run on a different port:
```bash
python manage.py runserver 8080
```

## Support

For issues or questions, please open an issue in the repository.

