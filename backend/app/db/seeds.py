print('Please fill the seeds file')
from app.models.domain.items import Item
from app.models.domain.users import User
from app.models.domain.comments import Comment
from app.db.repositories.items import ItemsRepository
from app.db.repositories.users import UsersRepository
from app.db.repositories.comments import CommentsRepository
from app.db.repositories.profiles import ProfilesRepository    
from asyncpg import Connection


async def seed_items(conn: Connection) -> None:
    items_repo = ItemsRepository(conn)
    await items_repo.create_item(
        item=Item(
            title="Test Item",
            description="Test Description",
            price=100,
            quantity=10,
        ),
    )


async def seed_users(conn: Connection) -> None:
    users_repo = UsersRepository(conn)
    await users_repo.create_user(
        user=User(
            username="testuser",
            email="test@gmail.com",
            password="testpassword",
        ),
    )


async def seed_comments(conn: Connection) -> None:
    comments_repo = CommentsRepository(conn)
    profiles_repo = ProfilesRepository(conn)
    items_repo = ItemsRepository(conn)
    user = await profiles_repo.get_profile_by_username(username="testuser")
    item = await items_repo.get_item_by_slug(slug="test-item")
    await comments_repo.create_comment_for_item(
        item=item,
        user=user,
        comment=Comment(body="Test Comment"),
    )

