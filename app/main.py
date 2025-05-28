"""
Instagram Clone Landing Page
A responsive Instagram UI clone built with NiceGUI
"""
from nicegui import ui, app
import os
from typing import List, Dict, Any

# Configure static files directory
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app.add_static_files('/static', static_dir)

# Sample data for posts and stories
def get_sample_posts() -> List[Dict[str, Any]]:
    return [
        {
            'username': 'travel_explorer',
            'avatar': '/static/images/avatar1.jpg',
            'image': '/static/images/post1.jpg',
            'likes': 1243,
            'caption': 'Exploring the beautiful mountains! #travel #adventure',
            'time': '2 hours ago',
            'comments': 42
        },
        {
            'username': 'food_lover',
            'avatar': '/static/images/avatar2.jpg',
            'image': '/static/images/post2.jpg',
            'likes': 856,
            'caption': 'Delicious homemade pasta 🍝 #foodie #homecooking',
            'time': '5 hours ago',
            'comments': 23
        },
        {
            'username': 'fitness_guru',
            'avatar': '/static/images/avatar3.jpg',
            'image': '/static/images/post3.jpg',
            'likes': 2105,
            'caption': 'Morning workout complete! 💪 #fitness #motivation',
            'time': '8 hours ago',
            'comments': 67
        },
        {
            'username': 'art_creative',
            'avatar': '/static/images/avatar4.jpg',
            'image': '/static/images/post4.jpg',
            'likes': 943,
            'caption': 'My latest creation 🎨 #art #creative',
            'time': '1 day ago',
            'comments': 31
        }
    ]

def get_sample_stories() -> List[Dict[str, Any]]:
    return [
        {'username': 'your_story', 'avatar': '/static/images/avatar_self.jpg', 'is_self': True},
        {'username': 'travel_explorer', 'avatar': '/static/images/avatar1.jpg', 'is_self': False},
        {'username': 'food_lover', 'avatar': '/static/images/avatar2.jpg', 'is_self': False},
        {'username': 'fitness_guru', 'avatar': '/static/images/avatar3.jpg', 'is_self': False},
        {'username': 'art_creative', 'avatar': '/static/images/avatar4.jpg', 'is_self': False},
        {'username': 'tech_geek', 'avatar': '/static/images/avatar5.jpg', 'is_self': False},
        {'username': 'music_fan', 'avatar': '/static/images/avatar6.jpg', 'is_self': False},
        {'username': 'nature_lover', 'avatar': '/static/images/avatar7.jpg', 'is_self': False}
    ]

# Add Instagram CSS styles
@ui.page('/')
def instagram_page():
    with ui.element('style').classes('hidden'):
        ui.html('''
        <style>
            /* Instagram-like styling */
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #fafafa;
                color: #262626;
            }
            
            .instagram-container {
                max-width: 935px;
                margin: 0 auto;
                padding: 0;
            }
            
            .navbar {
                background-color: white;
                border-bottom: 1px solid #dbdbdb;
                position: fixed;
                top: 0;
                width: 100%;
                z-index: 100;
                height: 60px;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .navbar-content {
                max-width: 975px;
                width: 100%;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 20px;
            }
            
            .logo {
                height: 29px;
            }
            
            .search-box {
                background-color: #efefef;
                border-radius: 8px;
                padding: 8px 16px;
                width: 268px;
                border: none;
                text-align: center;
                font-size: 14px;
            }
            
            .nav-icons {
                display: flex;
                gap: 22px;
            }
            
            .stories-container {
                display: flex;
                overflow-x: auto;
                padding: 16px 0;
                gap: 15px;
                background-color: white;
                border: 1px solid #dbdbdb;
                border-radius: 8px;
                margin-bottom: 24px;
                scrollbar-width: none; /* Firefox */
            }
            
            .stories-container::-webkit-scrollbar {
                display: none; /* Chrome, Safari, Opera */
            }
            
            .story {
                display: flex;
                flex-direction: column;
                align-items: center;
                min-width: 80px;
            }
            
            .story-avatar-container {
                width: 66px;
                height: 66px;
                border-radius: 50%;
                background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
                display: flex;
                justify-content: center;
                align-items: center;
                margin-bottom: 8px;
            }
            
            .story-avatar {
                width: 62px;
                height: 62px;
                border-radius: 50%;
                border: 2px solid white;
                object-fit: cover;
            }
            
            .story-username {
                font-size: 12px;
                color: #262626;
                max-width: 74px;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
                text-align: center;
            }
            
            .post {
                background-color: white;
                border: 1px solid #dbdbdb;
                border-radius: 8px;
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
                margin-right: 12px;
                object-fit: cover;
            }
            
            .post-username {
                font-weight: 600;
                font-size: 14px;
                flex-grow: 1;
            }
            
            .post-more {
                font-weight: bold;
                font-size: 14px;
            }
            
            .post-image {
                width: 100%;
                max-height: 767px;
                object-fit: cover;
            }
            
            .post-actions {
                display: flex;
                justify-content: space-between;
                padding: 8px 16px;
            }
            
            .post-action-left {
                display: flex;
                gap: 16px;
            }
            
            .post-likes {
                font-weight: 600;
                font-size: 14px;
                padding: 0 16px;
            }
            
            .post-caption {
                padding: 0 16px 8px;
                font-size: 14px;
            }
            
            .post-caption-username {
                font-weight: 600;
            }
            
            .post-comments {
                color: #8e8e8e;
                font-size: 14px;
                padding: 0 16px 8px;
            }
            
            .post-time {
                color: #8e8e8e;
                font-size: 10px;
                text-transform: uppercase;
                padding: 0 16px 16px;
            }
            
            .bottom-nav {
                position: fixed;
                bottom: 0;
                width: 100%;
                background-color: white;
                border-top: 1px solid #dbdbdb;
                display: flex;
                justify-content: space-around;
                padding: 10px 0;
                z-index: 100;
            }
            
            .bottom-nav-icon {
                width: 24px;
                height: 24px;
            }
            
            /* Responsive adjustments */
            @media (max-width: 767px) {
                .search-box {
                    display: none;
                }
                
                .instagram-container {
                    padding-top: 60px;
                    padding-bottom: 50px;
                }
                
                .post {
                    border-radius: 0;
                    border-left: none;
                    border-right: none;
                }
            }
            
            @media (min-width: 768px) {
                .bottom-nav {
                    display: none;
                }
                
                .instagram-container {
                    padding-top: 90px;
                }
            }
        </style>
        ''')
    
    # Navbar
    with ui.element('div').classes('navbar'):
        with ui.element('div').classes('navbar-content'):
            ui.image('/static/images/instagram-logo.png').classes('logo')
            ui.input('Search').classes('search-box')
            with ui.element('div').classes('nav-icons'):
                ui.image('/static/images/home.svg').classes('nav-icon')
                ui.image('/static/images/messenger.svg').classes('nav-icon')
                ui.image('/static/images/new-post.svg').classes('nav-icon')
                ui.image('/static/images/explore.svg').classes('nav-icon')
                ui.image('/static/images/like.svg').classes('nav-icon')
                ui.image('/static/images/avatar_self.jpg').classes('nav-icon post-avatar').style('width: 24px; height: 24px;')
    
    # Main container
    with ui.element('div').classes('instagram-container'):
        # Stories
        with ui.element('div').classes('stories-container'):
            for story in get_sample_stories():
                with ui.element('div').classes('story'):
                    with ui.element('div').classes('story-avatar-container'):
                        ui.image(story['avatar']).classes('story-avatar')
                    ui.label(story['username']).classes('story-username')
        
        # Posts
        for post in get_sample_posts():
            with ui.element('div').classes('post'):
                with ui.element('div').classes('post-header'):
                    ui.image(post['avatar']).classes('post-avatar')
                    ui.label(post['username']).classes('post-username')
                    ui.label('•••').classes('post-more')
                
                ui.image(post['image']).classes('post-image')
                
                with ui.element('div').classes('post-actions'):
                    with ui.element('div').classes('post-action-left'):
                        ui.image('/static/images/like.svg').style('width: 24px; height: 24px;')
                        ui.image('/static/images/comment.svg').style('width: 24px; height: 24px;')
                        ui.image('/static/images/share.svg').style('width: 24px; height: 24px;')
                    ui.image('/static/images/save.svg').style('width: 24px; height: 24px;')
                
                ui.label(f"{post['likes']} likes").classes('post-likes')
                
                with ui.element('div').classes('post-caption'):
                    ui.html(f"<span class='post-caption-username'>{post['username']}</span> {post['caption']}")
                
                ui.label(f"View all {post['comments']} comments").classes('post-comments')
                ui.label(post['time']).classes('post-time')
    
    # Bottom navigation (mobile only)
    with ui.element('div').classes('bottom-nav'):
        ui.image('/static/images/home.svg').classes('bottom-nav-icon')
        ui.image('/static/images/search.svg').classes('bottom-nav-icon')
        ui.image('/static/images/reels.svg').classes('bottom-nav-icon')
        ui.image('/static/images/shop.svg').classes('bottom-nav-icon')
        ui.image('/static/images/avatar_self.jpg').classes('bottom-nav-icon post-avatar').style('width: 24px; height: 24px; border-radius: 50%;')