class gl:
    pkl_df_jobs_file = "pkl_df_jobs.pkl"
    pkl_df_selected_jobs = "pkl_df_selected_jobs.pkl"
    pkl_df_not_selected_jobs = "pkl_df_not_selected_jobs.pkl"
    pkl_df_tfidf_jobs = "pkl_df_tfidf_jobs.pkl"
    pkl_df_tfidf_selected_jobs = "pkl_df_tfidf_selected_jobs.pkl"
    pkl_df_tfidf_not_selected_jobs = "pkl_df_tfidf_not_selected_jobs.pkl"
    txt_resume = 'resume.txt'
    tfidf_file = "df_tfidf_jobs.csv"
    # column names for jobs dataframe
    id = "Id"
    title = "Title"
    body = "Body"
    body_cos = "Body_Cosine_Similarity"
    bullet_points = 'Bullet_Points'
    bullet_points_cos = "Bullet_Points_Cosine_Similarity"
    score = "Score"
    # flag for data source
    from_tfidf_file = False
    # tokens
    title_tokens = "Title_Tokens"
    body_tokens = "Body Tokens"
    bullet_point_tokens = 'Bullet_Point Tokens'