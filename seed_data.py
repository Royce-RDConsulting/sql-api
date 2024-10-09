from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, User, Post
from app.crud import create_user, create_post
from app.schemas import UserCreate, PostCreate
import random
from faker import Faker

# Create all tables
Base.metadata.create_all(bind=engine)

# Initialize Faker
fake = Faker()

def generate_users(num_users):
    return [
        {
            "username": fake.user_name(),
            "email": fake.email(),
            "password": fake.password(length=10)
        }
        for _ in range(num_users)
    ]

def generate_posts(num_posts):
    return [
        {
            "title": fake.sentence(nb_words=6, variable_nb_words=True),
            "content": fake.paragraph(nb_sentences=5, variable_nb_sentences=True)
        }
        for _ in range(num_posts)
    ]

def seed_data():
    db = SessionLocal()
    try:
        # Generate and create users
        users = generate_users(15)
        db_users = []
        for user_data in users:
            user = create_user(db, UserCreate(**user_data))
            db_users.append(user)
        print(f"Created {len(db_users)} users.")
        
        # Generate and create posts
        posts = generate_posts(45)
        for post_data in posts:
            user = random.choice(db_users)
            create_post(db, PostCreate(**post_data), user_id=user.id)
        print(f"Created 45 posts.")
        
        print("Data seeding completed successfully.")
    except Exception as e:
        print(f"An error occurred while seeding data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()