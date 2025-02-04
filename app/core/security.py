
# async def get_token_user(
#     session: SessionDep,
#     authorization: HTTPAuthorizationCredentials = Depends(security),
# ):
#     token = authorization.credentials
#     # Use get_current_user to decode and validate the tokens
#     user_payload = get_current_user(session, token)
#     # Query the database for the token
#     query = select(TokenUser).where(TokenUser.id == token, TokenUser.is_active == True)
#     result = await session.execute(query)
#     db_token = result.scalar_one_or_none()
#     if (
#         db_token is None
#         or not bool(db_token.is_active)
#         or (str(db_token.user_id) != str(user_payload["id"]))
#     ):
#         raise HTTPException(status_code=401, detail="UserToken is inactive or invalid.")
#     return db_token.user_id


# async def add_token_user(user: User, session: AsyncSession) -> str:
#     await session.execute(
#         update(TokenUser).where(TokenUser.user_id == user.id).values(is_active=False)
#     )
#     await session.commit()
#     new_token = create_access_token(
#         str(user.id),
#         expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
#     )
#     new_token_db = TokenUser(id=str(new_token), user=user)
#     session.add(new_token_db)
#     await session.commit()
#     return new_token


# TokenDepUser = Annotated[str, Depends(get_token_user)]
