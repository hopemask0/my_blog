from fastapi import FastAPI
from app.infrastructure.db.session import engine
from app.infrastructure.db.models import Base, User, Post, Comment
from app.api.routes import post, comment, user
from app.infrastructure.db.session import SessionLocal
from fastapi.responses import JSONResponse 

app = FastAPI()


@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Welcome to My Blog API!"})


Base.metadata.create_all(bind=engine)


def fill_initial_data():
    db = SessionLocal()

    if not db.query(User).first():
        users = [User(username=f"user{i}") for i in range(1, 6)]
        db.add_all(users)
        db.commit()

    if not db.query(Post).first():
        users = db.query(User).all()
        posts = [Post(title=f"Post {i}", content=f"Content {i}", user_id=users[i % len(users)].id) for i in range(1, 6)]
        db.add_all(posts)
        db.commit()

    if not db.query(Comment).first():
        posts = db.query(Post).all()
        users = db.query(User).all()
        comments = []
        for i in range(1, 6):
            comments.append(Comment(
                post_id=posts[i % len(posts)].id,
                content=f"Comment {i}",
                user_id=users[i % len(users)].id
            ))
        db.add_all(comments)
        db.commit()

    db.close()


fill_initial_data()

app.include_router(post.router)
app.include_router(comment.router)
app.include_router(user.router)
