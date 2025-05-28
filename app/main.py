"""
Instagram Clone Landing Page
A visually accurate recreation of Instagram's landing page using NiceGUI.
"""
import os
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime, timedelta
import random
from nicegui import ui, app

# Configure static files directory
static_dir = Path(__file__).parent / 'static'
app.add_static_files('/static', static_dir)

# Sample user data
USERS = {
    'jane_doe': {
        'name': 'Jane Doe',
        'avatar': '/static/avatars/user1.jpg',
        'verified': True
    },
    'travel_enthusiast': {
        'name': 'Travel Enthusiast',
        'avatar': '/static/avatars/user2.jpg',
        'verified': True
    },
    'food_lover': {
        'name': 'Food Lover',
        'avatar': '/static/avatars/user3.jpg',
        'verified': False
    },
    'photo_pro': {
        'name': 'Photography Pro',
        'avatar': '/static/avatars/user4.jpg',
        'verified': True
    },
    'nature_explorer': {
        'name': 'Nature Explorer',
        'avatar': '/static/avatars/user5.jpg',
        'verified': False
    }
}

# Sample posts data
POSTS: List[Dict[str, Any]] = [
    {
        'id': 1,
        'user': 'jane_doe',
        'image': '/static/posts/post1.jpg',
        'caption': 'Enjoying the beautiful sunset at the beach! 🌅 #sunset #beach #vacation',
        'likes': 1243,
        'comments': 42,
        'timestamp': datetime.now() - timedelta(hours=2)
    },
    {
        'id': 2,
        'user': 'travel_enthusiast',
        'image': '/static/posts/post2.jpg',
        'caption': 'Exploring the mountains today! The view is breathtaking. #mountains #hiking #nature',
        'likes': 892,
        'comments': 31,
        'timestamp': datetime.now() - timedelta(hours=5)
    },
    {
        'id': 3,
        'user': 'food_lover',
        'image': '/static/posts/post3.jpg',
        'caption': 'Homemade pasta for dinner tonight! 🍝 #food #homemade #pasta #foodie',
        'likes': 756,
        'comments': 25,
        'timestamp': datetime.now() - timedelta(hours=8)
    },
    {
        'id': 4,
        'user': 'photo_pro',
        'image': '/static/posts/post4.jpg',
        'caption': 'City lights at night. #photography #cityscape #nightphotography',
        'likes': 1567,
        'comments': 53,
        'timestamp': datetime.now() - timedelta(days=1)
    },
    {
        'id': 5,
        'user': 'nature_explorer',
        'image': '/static/posts/post5.jpg',
        'caption': 'Found this beautiful flower during my hike today. #nature #flowers #hiking',
        'likes': 643,
        'comments': 19,
        'timestamp': datetime.now() - timedelta(days=2)
    }
]

# Stories data
STORIES = list(USERS.keys())

# CSS for Instagram styling
INSTAGRAM_CSS = """
<style>
    /* Instagram-like styling */
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        background-color: #fafafa;
        color: #262626;
        margin: 0;
        padding: 0;
    }
    
    .instagram-container {
        max-width: 935px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .header {
        height: 60px;
        background-color: white;
        border-bottom: 1px solid #dbdbdb;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 20px;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 100;
    }
    
    .logo {
        font-family: 'Billabong', cursive;
        font-size: 28px;
        font-weight: 500;
    }
    
    .post {
        background-color: white;
        border: 1px solid #dbdbdb;
        border-radius: 3px;
        margin-bottom: 24px;
    }
    
    .post-header {
        display: flex;
        align-items: center;
        padding: 14px 16px;
    }
    
    .post-avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        margin-right: 10px;
    }
    
    .post-username {
        font-weight: 600;
        font-size: 14px;
    }
    
    .post-image {
        width: 100%;
        max-height: 600px;
        object-fit: cover;
    }
    
    .post-actions {
        padding: 8px 16px;
    }
    
    .post-likes {
        font-weight: 600;
        font-size: 14px;
        margin: 8px 0;
    }
    
    .post-caption {
        font-size: 14px;
        margin: 8px 0;
    }
    
    .post-timestamp {
        color: #8e8e8e;
        font-size: 10px;
        text-transform: uppercase;
        margin: 8px 0;
    }
    
    .stories {
        display: flex;
        overflow-x: auto;
        padding: 16px 0;
        background-color: white;
        border: 1px solid #dbdbdb;
        border-radius: 3px;
        margin-bottom: 24px;
    }
    
    .story {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0 12px;
    }
    
    .story-avatar {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        border: 2px solid #e1306c;
        padding: 2px;
    }
    
    .story-username {
        font-size: 12px;
        margin-top: 4px;
        max-width: 64px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    
    .bottom-nav {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        height: 50px;
        background-color: white;
        border-top: 1px solid #dbdbdb;
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 100;
    }
    
    .nav-icon {
        font-size: 24px;
    }
    
    .verified-badge {
        color: #3897f0;
        font-size: 12px;
        margin-left: 4px;
    }
    
    .login-container {
        background-color: white;
        border: 1px solid #dbdbdb;
        border-radius: 3px;
        padding: 20px;
        margin-bottom: 10px;
        text-align: center;
    }
    
    .login-form input {
        width: 100%;
        padding: 9px 8px;
        background-color: #fafafa;
        border: 1px solid #dbdbdb;
        border-radius: 3px;
        margin-bottom: 6px;
    }
    
    .login-button {
        background-color: #0095f6;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 5px 9px;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        margin-top: 8px;
    }
    
    .or-divider {
        display: flex;
        align-items: center;
        margin: 10px 0;
    }
    
    .or-line {
        flex-grow: 1;
        height: 1px;
        background-color: #dbdbdb;
    }
    
    .or-text {
        margin: 0 10px;
        color: #8e8e8e;
        font-size: 13px;
        font-weight: 600;
    }
    
    .facebook-login {
        color: #385185;
        font-weight: 600;
        font-size: 14px;
        margin: 8px 0;
    }
    
    .forgot-password {
        color: #00376b;
        font-size: 12px;
        margin: 12px 0;
    }
    
    .signup-container {
        background-color: white;
        border: 1px solid #dbdbdb;
        border-radius: 3px;
        padding: 20px;
        text-align: center;
    }
    
    .app-download {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    
    .app-download img {
        height: 40px;
        margin: 0 4px;
    }
    
    @media (max-width: 735px) {
        .instagram-container {
            padding: 0;
        }
        
        .post {
            border-left: none;
            border-right: none;
            border-radius: 0;
        }
        
        .stories {
            border-left: none;
            border-right: none;
            border-radius: 0;
        }
    }
</style>
"""

# Helper functions
def format_timestamp(timestamp: datetime) -> str:
    """Format timestamp in Instagram style."""
    now = datetime.now()
    diff = now - timestamp
    
    if diff.days > 0:
        return f"{diff.days}d ago"
    elif diff.seconds // 3600 > 0:
        return f"{diff.seconds // 3600}h ago"
    else:
        return f"{diff.seconds // 60}m ago"

def format_number(num: int) -> str:
    """Format numbers in Instagram style."""
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    else:
        return str(num)

@ui.page('/')
def instagram_landing_page():
    """Instagram clone landing page."""
    # Add Instagram CSS
    ui.html(INSTAGRAM_CSS)
    
    with ui.header().classes('header'):
        ui.label('Instagram').classes('logo')
        with ui.row().classes('gap-4'):
            ui.button(icon='search').props('flat round')
            ui.button(icon='notifications').props('flat round')
            ui.button(icon='send').props('flat round')
    
    # Main content container
    with ui.column().classes('instagram-container mt-16 mb-16'):
        # Stories section
        with ui.row().classes('stories w-full'):
            for username in STORIES:
                user = USERS[username]
                with ui.column().classes('story'):
                    ui.image(user['avatar']).classes('story-avatar')
                    ui.label(username).classes('story-username')
        
        # Posts feed
        for post in POSTS:
            user = USERS[post['user']]
            with ui.card().classes('post w-full'):
                # Post header
                with ui.row().classes('post-header w-full items-center'):
                    ui.image(user['avatar']).classes('post-avatar')
                    ui.label(post['user']).classes('post-username')
                    if user['verified']:
                        ui.icon('verified', color='#3897f0').classes('verified-badge')
                    ui.space()
                    ui.button(icon='more_horiz').props('flat round')
                
                # Post image
                ui.image(post['image']).classes('post-image')
                
                # Post actions
                with ui.row().classes('post-actions w-full'):
                    with ui.row().classes('gap-4'):
                        ui.button(icon='favorite_border').props('flat round')
                        ui.button(icon='chat_bubble_outline').props('flat round')
                        ui.button(icon='send').props('flat round')
                    ui.space()
                    ui.button(icon='bookmark_border').props('flat round')
                
                # Post details
                with ui.column().classes('px-4 pb-4'):
                    ui.label(f"{format_number(post['likes'])} likes").classes('post-likes')
                    with ui.row().classes('post-caption'):
                        ui.label(post['user']).classes('font-bold mr-2')
                        ui.label(post['caption'])
                    ui.label(f"View all {post['comments']} comments").classes('text-gray-500 text-sm')
                    ui.label(format_timestamp(post['timestamp'])).classes('post-timestamp')
        
        # Login section (for non-logged in users)
        with ui.card().classes('login-container'):
            ui.image('/static/instagram-logo.png').style('width: 175px; margin: 0 auto 20px;')
            
            with ui.column().classes('login-form w-full'):
                ui.input('Phone number, username, or email').props('outlined dense')
                ui.input('Password', password=True).props('outlined dense')
                ui.button('Log In').classes('login-button')
            
            with ui.row().classes('or-divider'):
                ui.element('div').classes('or-line')
                ui.label('OR').classes('or-text')
                ui.element('div').classes('or-line')
            
            with ui.row().classes('facebook-login items-center justify-center'):
                ui.icon('facebook', color='#385185')
                ui.label('Log in with Facebook')
            
            ui.label('Forgot password?').classes('forgot-password')
        
        with ui.card().classes('signup-container'):
            ui.label("Don't have an account? ").classes('inline')
            ui.label('Sign up').classes('text-blue-500 font-semibold inline')
        
        ui.label('Get the app.').classes('text-center mt-4')
        with ui.row().classes('app-download'):
            ui.image('/static/app-store.png')
            ui.image('/static/google-play.png')
    
    # Bottom navigation
    with ui.footer().classes('bottom-nav'):
        ui.button(icon='home').props('flat round')
        ui.button(icon='search').props('flat round')
        ui.button(icon='add_box').props('flat round')
        ui.button(icon='favorite_border').props('flat round')
        ui.button(icon='person').props('flat round')

@ui.page('/login')
def login_page():
    """Login page."""
    ui.html(INSTAGRAM_CSS)
    
    with ui.column().classes('instagram-container flex justify-center items-center min-h-screen'):
        with ui.card().classes('login-container max-w-sm'):
            ui.image('/static/instagram-logo.png').style('width: 175px; margin: 0 auto 20px;')
            
            with ui.column().classes('login-form w-full'):
                ui.input('Phone number, username, or email').props('outlined dense')
                ui.input('Password', password=True).props('outlined dense')
                ui.button('Log In').classes('login-button')
            
            with ui.row().classes('or-divider'):
                ui.element('div').classes('or-line')
                ui.label('OR').classes('or-text')
                ui.element('div').classes('or-line')
            
            with ui.row().classes('facebook-login items-center justify-center'):
                ui.icon('facebook', color='#385185')
                ui.label('Log in with Facebook')
            
            ui.label('Forgot password?').classes('forgot-password')
        
        with ui.card().classes('signup-container max-w-sm mt-4'):
            ui.label("Don't have an account? ").classes('inline')
            ui.label('Sign up').classes('text-blue-500 font-semibold inline')
        
        ui.label('Get the app.').classes('text-center mt-4')
        with ui.row().classes('app-download'):
            ui.image('/static/app-store.png')
            ui.image('/static/google-play.png')

@ui.page('/signup')
def signup_page():
    """Signup page."""
    ui.html(INSTAGRAM_CSS)
    
    with ui.column().classes('instagram-container flex justify-center items-center min-h-screen'):
        with ui.card().classes('login-container max-w-sm'):
            ui.image('/static/instagram-logo.png').style('width: 175px; margin: 0 auto 20px;')
            ui.label('Sign up to see photos and videos from your friends.').classes('text-center text-gray-500 mb-4')
            
            ui.button('Log in with Facebook').classes('login-button')
            
            with ui.row().classes('or-divider'):
                ui.element('div').classes('or-line')
                ui.label('OR').classes('or-text')
                ui.element('div').classes('or-line')
            
            with ui.column().classes('login-form w-full'):
                ui.input('Mobile Number or Email').props('outlined dense')
                ui.input('Full Name').props('outlined dense')
                ui.input('Username').props('outlined dense')
                ui.input('Password', password=True).props('outlined dense')
                ui.button('Sign Up').classes('login-button')
            
            ui.label('By signing up, you agree to our Terms, Privacy Policy and Cookies Policy.').classes('text-center text-xs text-gray-500 mt-4')
        
        with ui.card().classes('signup-container max-w-sm mt-4'):
            ui.label('Have an account? ').classes('inline')
            ui.label('Log in').classes('text-blue-500 font-semibold inline')
        
        ui.label('Get the app.').classes('text-center mt-4')
        with ui.row().classes('app-download'):
            ui.image('/static/app-store.png')
            ui.image('/static/google-play.png')