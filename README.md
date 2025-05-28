# Instagram Clone Landing Page

A visually accurate recreation of Instagram's landing page using NiceGUI.

## Features

- Instagram-like UI with header, feed, and navigation
- Stories section with user avatars
- Post feed with images, likes, and comments
- Login and signup pages
- Responsive design for different screen sizes

## Setup and Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python main.py
   ```
4. Open your browser and navigate to `http://localhost:8000`

## Project Structure

- `main.py`: Entry point for the application
- `app/main.py`: Main application code with page definitions
- `app/static/`: Static assets (images, etc.)

## Image Placeholders

For a complete experience, you'll need to add the following images:

1. Instagram logo: `app/static/instagram-logo.png`
2. App store buttons: 
   - `app/static/app-store.png`
   - `app/static/google-play.png`
3. User avatars:
   - `app/static/avatars/user1.jpg` through `user5.jpg`
4. Post images:
   - `app/static/posts/post1.jpg` through `post5.jpg`

You can use any images you like, or download sample images from a stock photo site.

## Pages

- `/`: Main Instagram feed
- `/login`: Login page
- `/signup`: Signup page

## Technologies Used

- [NiceGUI](https://nicegui.io/): Python UI framework
- [Uvicorn](https://www.uvicorn.org/): ASGI server