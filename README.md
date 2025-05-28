# Instagram Clone Landing Page

A responsive Instagram UI clone built with NiceGUI that closely resembles the real Instagram application.

## Features

- Responsive design that adapts to different screen sizes (mobile and desktop)
- Instagram-like UI components including:
  - Navigation bar with Instagram logo and icons
  - Stories section with profile circles
  - Post feed with sample images
  - Like, comment, and share functionality (UI only)
  - Mobile bottom navigation bar

## Setup Instructions

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Add your sample images to the `app/static/images/` directory:
   - Avatar images: avatar1.jpg, avatar2.jpg, avatar3.jpg, avatar4.jpg, avatar5.jpg, avatar6.jpg, avatar7.jpg, avatar_self.jpg
   - Post images: post1.jpg, post2.jpg, post3.jpg, post4.jpg
   - Instagram logo: instagram-logo.png
   - The SVG icons are already included in the repository

4. Run the application:
   ```
   python main.py
   ```
5. Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
instagram-clone/
├── app/
│   ├── __init__.py
│   ├── main.py             # Main application logic
│   └── static/
│       └── images/         # Sample images and icons
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

## Responsive Design

The application is fully responsive:
- Desktop view: Shows the full Instagram interface with search bar and navigation icons
- Mobile view: Adapts to smaller screens with bottom navigation bar and optimized layout

## Technologies Used

- NiceGUI: Python UI framework
- HTML/CSS: For styling and layout
- SVG: For Instagram icons