from logging import raiseExceptions
from fastapi import Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm.session import Session

from .. import schemas, database, models, oauth2

router = APIRouter(prefix="/votes", tags=["Vote"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), user=Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with {vote.post_id} does not exist")
    vote_query = db.query(models.Vote).filter(models.Vote.user_id == user.id, models.Vote.post_id == vote.post_id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {user.id} has already voted for this post {vote.post_id}")
        new_vote =models.Vote(post_id=vote.post_id, user_id=user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "deleted vote"}
